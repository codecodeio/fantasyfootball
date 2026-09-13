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
- 🦅 **The roster must always contain at least one Philadelphia Eagle.** Currently Goedert.

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

Yahoo has no open read API without OAuth, so capture is **agent-driven**, not a cron job:

1. In Claude Code, ask to capture the week. The agent opens
   `https://football.fantasysports.yahoo.com/f1/1396154/7` via the Chrome DevTools MCP
   (the browser profile stays logged in) and reads the roster table.
2. It writes `data/2026/weekly/wkNN.json` in the same shape as `wk01.json`.
3. Set `"complete": true` only once every game has finished (after Monday night).

⚠️ `wk01.json` was captured mid-Sunday and is **partial** — re-capture to finalise it.

If this lapses, the project is worthless. See `notes/capture.md` for the automation options
and their trade-offs.

## Files

| Path | Role |
|---|---|
| `data/<season>/league.json` | League settings, scoring, house constraints |
| `data/<season>/draft.json` | Every pick: proj, ADP, bye, Yahoo grade + post-draft standings |
| `data/<season>/weekly/wkNN.json` | Weekly projected vs actual, per player |
| `notes/<season>-draft-log.md` | Why each pick was made, and the hypotheses to score |
| `notes/capture.md` | How to keep the weekly data flowing; automation options |
| `scripts/analyze.py` | Projection accuracy, bias by position, lineup efficiency |
