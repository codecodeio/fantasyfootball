# Keeping the weekly data flowing

This project is only worth anything if a week gets captured every week. Manual capture will
lapse by Week 4 — assume that, and pick an option below deliberately.

## Option A — agent-driven browser read (what's in use now)

The Chrome DevTools MCP opens the team page in a logged-in Chrome profile and reads the roster
table directly. No credentials stored anywhere in this repo.

- ✅ Zero setup — it already works, and produced `wk01.json`.
- ✅ No Yahoo developer account, no tokens.
- ❌ **Requires a Claude Code session each week.** Cannot be scheduled or run headless.
- ❌ Breaks silently if the Yahoo session expires or the page markup changes.

**Verdict:** fine for now, will not survive the season on its own.

## Option B — Yahoo Fantasy Sports API (the durable answer)

Yahoo exposes a real read API over OAuth2. Once authorized, a script can pull the roster and
weekly stats headlessly, on a schedule, forever.

Setup, one time (~15 minutes, free):
1. Register an app at <https://developer.yahoo.com/apps/create/> — pick **Fantasy Sports · Read**.
2. Save the Client ID and Client Secret into `.env` (already gitignored).
3. Run the auth flow once in a browser; the refresh token persists after that.
4. `pip install yfpy` (or hand-roll it — the endpoint is
   `/fantasy/v2/league/nfl.l.1396154/teams;team_keys=.../roster/players/stats;type=week;week=N`).

- ✅ Scriptable, schedulable, no browser.
- ✅ Returns real stat lines, not scraped table text.
- ❌ Needs Matt to register the app — **this is the blocking step, and only Matt can do it.**
- ❌ Adds a dependency and a secret to manage.

**Verdict:** the right answer if this project is meant to last more than a month.

## Option C — schedule it

Once Option B works, wire it to the portfolio's existing scheduling pattern:

- **launchd**, matching `com.robinhood.papertrader` — runs locally, Tuesday ~09:00 after waivers
  process and every game is final.
- **aiguru cloud routine**, matching `robinhood-paper-report` — runs off-machine. Note a cloud
  routine *cannot* drive the local Chrome profile, so it requires Option B.

Tuesday morning is the right slot: Monday night games are final and waivers have run.

## Recommendation

Run **Option A** until the bye weeks start (Week 5), which buys time. Meanwhile do the Option B
registration once, then schedule it per Option C and stop thinking about it.

If none of that happens, capture at minimum **Week 17** — the season-end totals alone are enough
to score most of the hypotheses in `2026-draft-log.md`, even without the weekly detail.
