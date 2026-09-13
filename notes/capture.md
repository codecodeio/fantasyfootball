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

## Option B — Yahoo Fantasy Sports API (the durable answer, but gated)

Yahoo exposes a read API over OAuth2. Once authorized, a script can pull the roster and weekly
stats headlessly, on a schedule.

⚠️ **This is no longer self-serve.** As of 2026 Yahoo requires a formal application reviewed by
the Fantasy Sports team; `developer.yahoo.com/fantasysports/guide/` now redirects to
`sports.yahoo.com/developer`. Applications that are "incomplete or lack sufficient detail will be
closed without further communication," and the approval timeline is not published.

Apply at <https://sports.yahoo.com/developer/access/>. The submission asks for:

- **Product description** — what you're building.
- **Data needs** — which Fantasy data you require.
- **User base** — expected users in the first 3–6 months, and whether it's personal / single-league
  use. Say plainly that this is personal, one league, one team.
- **Client ID** — only if you already have a Yahoo Developer Network app; otherwise blank.

Access is **read-only by default** (write access is not currently offered), which is all this
project needs.

📋 **Attribution is mandatory if approved.** You must display *"Fantasy data provided by Yahoo
Fantasy"* with a link back to Yahoo Fantasy, using their official logo unmodified. **This is a real
obligation for a public repo and any article** — it goes in the README, not just the code.

- ✅ Scriptable, schedulable, no browser. Real stat lines, not scraped table text.
- ❌ **Approval required, timeline unknown, and it may be declined.** Only Matt can submit it.
- ❌ Adds a dependency, a secret to manage, and an attribution requirement.

Once credentials exist: store them in `.env` (already gitignored), run the three-legged OAuth
handshake once in a browser, and the refresh token persists. `yfpy` and `yahoofantasy` are the
maintained Python wrappers; the raw endpoint shape is
`/fantasy/v2/league/nfl.l.1396154/teams;team_keys=.../roster/players/stats;type=week;week=N`.

## Option C — schedule it

Once Option B works, wire it to the portfolio's existing scheduling pattern:

- **launchd**, matching `com.robinhood.papertrader` — runs locally, Tuesday ~09:00 after waivers
  process and every game is final.
- **aiguru cloud routine**, matching `robinhood-paper-report` — runs off-machine. Note a cloud
  routine *cannot* drive the local Chrome profile, so it requires Option B.

Tuesday morning is the right slot: Monday night games are final and waivers have run.

## Recommendation

**Submit the Option B application today** — the clock on approval starts when you send it, and it
costs nothing to be waiting. Assume it may be declined.

**Run Option A in the meantime**, and treat Week 5 (first byes) as the checkpoint. If there's no
approval by then, Option A plus a calendar reminder is the realistic plan, and that's fine — the
analysis works on whatever weeks exist.

If everything lapses, capture at minimum **Week 17**. Season-end totals alone answer most of the
hypotheses in `2026-draft-log.md`, even with no weekly detail.
