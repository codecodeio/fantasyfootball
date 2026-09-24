# CLAUDE.md — fantasyfootball

Guidance for Claude Code in this repo. Read before changing code.

## What this project is

A season-long record of Matt's Yahoo fantasy football team (**Tuchus Puchus**, league `1396154`)
built to answer one question: **were the draft-day decisions actually right?** It stores the draft
record, weekly projected-vs-actual results, and the reasoning behind each pick, then scores that
reasoning against reality so next year's draft is run on evidence instead of instinct.

"Done" for a season = every week captured, `scripts/analyze.py` run, and the hypotheses in
`notes/<season>-draft-log.md` marked confirmed or rejected.

This is a standalone git repo (`fantasyfootball`, GitHub: `codecodeio/fantasyfootball`). It lives as a
sibling under `repos/` and is orchestrated by **aiguru** — see `../aiguru/brain/projects.md`.

## League facts (do not re-derive — read `data/2026/league.json`)

- **12 teams, half-PPR** (0.5/rec), **4-pt passing TD**, −1 INT, −2 fumble lost, fractional scoring.
- Roster: `QB · WR · WR · RB · RB · TE · W/R/T · K · DEF` + 6 BN + 2 IR = **15 drafted**.
- Matt drafted from **slot 4 of 12**; picks 4, 21, 28, 45, 52, 69, 76, 93, 100, 117, 124, 141, 148, 165, 172.
- Waivers: continual rolling list, processed game-time Tuesday, **no acquisition limits**.
- Trade deadline **2026-11-28**; trades go to league vote.

### House constraints Matt plays by
- 🚫 **No two players at the same position may share a bye week.** (Handcuffs are exempt — a backup
  is not a rotational starter. Black/McCaffrey both bye 8 by deliberate choice.)
- 🦅 **Favorite-team rule: the roster must always hold ≥1 player from the chosen team** (2026: PHI,
  satisfied by Goedert at zero cost because he doubles as TE2). Budget for it before the draft and
  never pay the premium option — the method is `notes/draft-strategy.md` rule 2.

## House conventions (inherited from aiguru)

- **Python does math, Claude does the API** — deterministic scripts compute; the agent
  handles anything needing an MCP/LLM (e.g. reading the Yahoo page via Chrome DevTools MCP).
- **Emoji status prefixes** in interactive output: ✅ ❌ 🚫 🌐.
- **Commit + push promptly;** keep branches in sync; never leave uncommitted edits at the
  end of a turn.
- **Honest reporting** — show the downside next to the upside; **flag small samples**; don't
  oversell. `analyze.py` warns below 4 complete weeks; keep that behaviour.
- A short **CLI dispatcher** (`aliases.sh`) is the front door for routine commands.

## Running

```bash
python3 scripts/analyze.py 2026     # score projections + lineup decisions
ff analyze                          # same, via the dispatcher
```

No dependencies — standard library only. No build, no tests yet.

## Capturing a week

**Decision: browser, not the API** — Yahoo's API is read-only and cannot set a lineup.
Capture and lineup changes are both **agent-driven** through the Chrome DevTools MCP:

1. In Claude Code, ask to capture the week. The agent opens
   `https://football.fantasysports.yahoo.com/f1/1396154/7` via the Chrome DevTools MCP
   (the browser profile stays logged in) and reads the roster table.
2. It writes `data/2026/weekly/wkNN.json` in the same shape as `wk01.json`.
3. Set `"complete": true` only once every game has finished (after Monday night).

✅ `wk01.json` and `wk02.json` are final (`complete: true`). `wk03.json` is a pre-game capture
and is still **partial** — re-capture after Monday night (PHI @ CHI).

A launchd job nudges Matt every **Wednesday 18:00** (`com.fantasyfootball.weeklyreminder`).
It reminds; it does not act. See `notes/capture.md` for the full rationale.

⚠️ **The job must not execute from this repo.** `~/Documents` is TCC-protected and a new
launchd label has no grant for it — running from here fails with `Operation not permitted`
(exit 126) and cannot prompt. `scripts/install-reminder.sh` deploys the script to
`~/Library/Application Support/fantasyfootball/` and points the plist there. **Edit
`scripts/remind.sh`, then run `ff install-reminder` to redeploy** — editing the repo copy
alone changes nothing.

## Weekly review — rules that prevent known mistakes

Each of these cost points or produced a wrong answer once. Follow them before touching a lineup.

1. **DEF and any Thursday-game starter lock on Thursday night.** Week 2's DEF slot was lost before
   the weekend — the Lions finished −2.00 and could not be changed by Saturday. **Set DEF by
   Wednesday**, which is exactly why the nudge fires Wednesday 18:00.
2. **Weekly projections are already opponent-adjusted.** Rotowire bakes the matchup in, so adding
   a points-against rank on top double-counts it. Never bench a higher projection *because* the
   lower one has a friendlier defence.
3. **Points-against ranks are one game per team before ~week 6, and are often circular.** Entering
   week 2, Washington ranked 3rd-worst against TEs solely because of Goedert's own week 1 line;
   Minnesota ranked 32nd against RBs partly because Lloyd's dud was in their column. Use matchup
   as a tiebreaker only when projections are within ~1 point, the sample is real, and the spread is
   large — most reliably for streaming DEF and K.
4. **When projections are near-tied, break the tie on usage, not on last week's points.** Targets,
   carries, route share and offence quality repeat; a two-TD spike does not. Starting Goedert
   because he scored 21.70 would be outcome bias — starting him on 5 targets against Fannin's 3 is
   the defensible version.
5. **Reload before reading `my_proj`.** After a lineup edit Yahoo's AJAX recompute rebuilds the
   total from projections alone and discards finished-game actuals. See `notes/capture.md`.
6. **Read the matchup page, not the standings page**, for projections and win probability:
   `/f1/1396154/matchup?week=N&mid1=7`. Standings interleaves both teams into one flat text column
   and is easy to misattribute. Confirm which side is ours with the players-remaining count.
7. **`Team NN` means different teams in different files.** Weekly files and the season log use the
   **Yahoo team id** (ours is 7). `draft.json`'s `league_totals` uses **draft-time projection rank**
   — it has no Team 03 because rank 3 is ours. Never join the two on the label.
8. **Week 6 has no DEF.** The Lions are on bye and there is no backup — stream one, by Thursday.

## Files

| Path | Role |
|---|---|
| `data/<season>/league.json` | League settings, scoring, house constraints |
| `data/<season>/draft.json` | Every pick: proj, ADP, bye, Yahoo grade + post-draft standings |
| `data/<season>/weekly/wkNN.json` | Weekly projected vs actual, per player |
| `notes/<season>-draft-log.md` | Why each pick was made, and the hypotheses to score |
| `notes/<season>-season-log.md` | **The week-by-week log** — one entry per week: moves, reasoning, result, byes |
| `notes/draft-strategy.md` | The repeatable draft method — constraints, ADP sequencing, favorite-team rule |
| `notes/capture.md` | How to keep the weekly data flowing; automation options |
| `scripts/analyze.py` | Projection accuracy, bias by position, lineup efficiency |
| `scripts/remind.sh` | Wednesday 18:00 macOS nudge (canonical copy; deployed outside the repo) |
| `scripts/install-reminder.sh` | Deploys the nudge + (re)loads the launchd job |
