# fantasyfootball

Season record and decision post-mortem for Matt's Yahoo fantasy team **Tuchus Puchus**
(2026 Fantasy Family Football, 12-team half-PPR).

Tracks what was drafted, why, and whether it worked — so next year's draft runs on evidence.

Part of Matt's `codecodeio` portfolio, orchestrated by [aiguru](https://github.com/codecodeio/aiguru).

## Setup

None. Standard library only — no install, no dependencies, no build step.

```bash
python3 scripts/analyze.py 2026     # score projections vs actuals
```

`aliases.sh` defines an optional `ff` wrapper (`ff analyze`, `ff week 3`, …). It is **not** sourced
by default and nothing here requires it; source it from `~/.zshrc` only if you want the shorthand.

## What's here

- **`data/2026/draft.json`** — all 15 picks with projection, ADP, bye and Yahoo grade
- **`notes/2026-draft-log.md`** — the reasoning behind every pick, plus 5 hypotheses to score
- **`data/2026/weekly/`** — projected vs actual, week by week
- **`scripts/analyze.py`** — projection accuracy, bias by position, points left on the bench
- **`notes/draft-strategy.md`** — the repeatable draft method, including the favorite-team rule

Weekly review is driven through a logged-in Chrome session (read *and* write — Yahoo's API is
read-only), nudged by a launchd reminder every Wednesday at 18:00.

## A note on privacy

This is a family league. The other eleven managers are anonymised as `Team 01`–`Team 12`
throughout the data and history — only rank and points totals are kept, which is all the
analysis needs. Nothing is lost analytically.

## The season log

`notes/2026-season-log.md` is the week-by-week record — one entry for every week of the season,
with the moves made, the reasoning behind them, the result, and the bye-week planner. Start there
to see what happened and why.

## Status

Season in progress. Week 1 final (**L** 95.16–106.02, 76.7% lineup efficiency); week 2 captured
pre-game. Yahoo projected finish: **3rd of 12**.
