# Keeping the weekly data flowing

**Decision (2026-09-13): use the browser, skip the Yahoo API.**

The Yahoo Fantasy Sports API is **read-only** — write access "is not currently available." It can
report the roster but cannot *set a lineup*, add a waiver claim, or drop a player. Since the whole
point of the Wednesday review is to **change** the team, a read-only API solves the smaller half of
the problem and still costs a reviewed application, a secret to manage, and a mandatory attribution
obligation.

Driving Chrome does both halves. So: Chrome.

## How capture + lineup changes work

The Chrome DevTools MCP drives a real logged-in Chrome profile, so it can read the roster table
*and* click through lineup edits, waiver adds and drops.

1. In Claude Code, from this repo, ask to run the weekly review.
2. The agent opens `https://football.fantasysports.yahoo.com/f1/1396154/7`, reads the roster,
   checks flags and byes, and proposes changes.
3. Approved changes get made in the browser.
4. The week is written to `data/2026/weekly/wkNN.json` in the shape of `wk01.json`.
5. Set `"complete": true` only once every game has finished.

- ✅ Read **and** write. No credentials in this repo, no third-party approval, no attribution terms.
- ✅ Already proven — it produced `wk01.json` and read the full draft board live.
- ❌ Requires a Claude Code session; cannot run headless or in the cloud.
- ❌ Breaks if the Yahoo session expires (just log in again) or the page markup changes.

✅ `wk01.json` and `wk02.json` are final (`complete: true`). `wk03.json` is a pre-game capture
and is still **partial** — re-capture after Monday night (PHI @ CHI).

## The weekly file shape — two traps

**1. `matchup.my_proj` is a live blend, not a pre-game projection.** Yahoo swaps a player's
projection for their actual score the moment their game ends, so `my_proj` drifts during the day
and **will not equal the sum of the `proj` column**. Week 2 shows it exactly — only the Thursday
DEF game had finished:

```
sum(proj) over 8 non-DEF starters   105.59
  + Lions  5.07 → −2.00              −7.07   (Thursday game final)
                                   = 103.59  = matchup.my_proj
```

The per-player `proj` values *are* stable pre-game numbers — those are what `analyze.py` scores.
Never compute projection accuracy from `my_proj`.

⚠️ **And don't trust `my_proj` straight after a lineup edit.** Yahoo's AJAX recompute rebuilds the
total from *projections only*, dropping the finished-game actuals it had already blended in. After
the week-2 swaps the header read **110.66** — that is 105.59 + the Lions' 5.07 pre-game projection,
silently discarding their −2.00 final. A hard reload corrected it to 103.59. **Always reload before
reading `my_proj` into a capture**, and sanity-check it against the sum of the `proj` column.

**2. `actual: null` means "not played yet", not "scored zero".** A real zero is `0.00` — Doubs in
Week 1. `analyze.py` keys on this distinction, so a capture that writes `0` for a pending player
silently corrupts the accuracy numbers.

## Driving the Yahoo UI — what works

**Where to read what.** Projections and win probability come from the **matchup** page,
`/f1/1396154/matchup?week=N&mid1=7`. Do *not* read them off the standings page: it interleaves
both teams' numbers into a single flat text column, which is easy to misattribute. The matchup page
also gives the opponent's full lineup. To confirm which side is ours, use the players-remaining
count rather than position on the page.

`Orig Proj` is frozen at the pre-kickoff projection; the adjacent figure swaps in real results as
they land. Week 2 showed both: 110.72 orig against 103.65 current, the 7.07 gap being the Lions'
5.07 projection replaced by their −2.00 actual.

**Changing a lineup.** Each roster row has a button labelled `Click here to edit <SLOT> <Player>`.
Click the *bench* player's button — the row highlights and every **legal destination turns green**.
Click the green target row and the swap posts immediately, confirming with a banner
("Moved X to TE - Benched Y"). There is no save step.

**Add/drop.** `/f1/1396154/addplayer?apid=<playerId>` opens the form with that player pre-selected;
each droppable player has a `—` button. In the accessibility tree **the drop button precedes its
player's name**, so verify against both ends of the list before clicking — the first entry belongs
to the first player, the last button to the last player. A confirmation page names both players
before anything is committed.

**Two things that block automation.** Script evaluation is refused on the fantasy pages as a
real-world transaction, so use snapshots plus click/navigate rather than `evaluate_script` when
editing. And snapshots of the roster page exceed the tool's token limit — they are written to a
file instead, so grep that file for `Click here to edit` to recover element ids.

**A stale browser holds the profile.** If the MCP reports "browser is already running for
`~/.cache/chrome-devtools-mcp/chrome-profile`", a Chrome from an earlier session still owns the
debugging pipe. Find the root process for that `--user-data-dir` and `kill -TERM` it — a graceful
quit flushes cookies, so the Yahoo login survives and no re-authentication is needed.

## The reminder

Because capture can't be automated end-to-end, the *nudge* is automated instead.

`scripts/remind.sh` fires a macOS notification every **Wednesday at 18:00** — waivers process
game-time Tuesday, so Wednesday evening is the first clean window to set the coming week's lineup.

| | |
|---|---|
| launchd job | `~/Library/LaunchAgents/com.fantasyfootball.weeklyreminder.plist` |
| Schedule | `Weekday 3`, `Hour 18` |
| Log | `~/Library/Logs/fantasyfootball/remind.log` |
| Deployed script | `~/Library/Application Support/fantasyfootball/remind.sh` |
| Manage | `ff install-reminder` · `ff reminder-status` · `ff remind` |

⚠️ **Gotcha — do not point the plist at this repo.** `~/Documents` is TCC-protected. A new launchd
label has no grant for it and cannot show a prompt, so it fails silently with `Operation not
permitted` (exit 126). This bit us on first install. Existing jobs like `com.robinhood.papertrader`
work only because they were approved back in August. The fix is to run from
`~/Library/Application Support/`, which `install-reminder.sh` handles. **After editing
`scripts/remind.sh`, run `ff install-reminder` or the change does nothing.**

The notification carries the NFL week number; the log records a six-point checklist (injuries,
byes, waivers, flex, favorite-team rule, capture last week).

**This is a nudge, not an agent.** It reminds Matt to open a session; it does not change the team.

## If it lapses anyway

Capture at minimum **Week 17**. Season-end totals alone answer most of the hypotheses in
`2026-draft-log.md`, even with no weekly detail.

## Why not the API (keep for the record)

If write access ever ships, revisit. Apply at <https://sports.yahoo.com/developer/access/> —
reviewed by Yahoo's Fantasy Sports team, timeline unpublished, incomplete applications closed
without communication. Approval carries a mandatory *"Fantasy data provided by Yahoo Fantasy"*
attribution with their unmodified logo, which would need to appear in the README and in any article.
