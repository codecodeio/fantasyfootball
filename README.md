# fantasyfootball

Season record and decision post-mortem for Matt's Yahoo fantasy team **Tuchus Puchus**
(2026 Fantasy Family Football, 12-team half-PPR).

Tracks what was drafted, why, and whether it worked — so next year's draft runs on evidence.

Part of Matt's `codecodeio` portfolio, orchestrated by [aiguru](https://github.com/codecodeio/aiguru).

## Setup

```bash
python3 scripts/analyze.py 2026     # no dependencies — stdlib only
```

## What's here

- **`data/2026/draft.json`** — all 15 picks with projection, ADP, bye and Yahoo grade
- **`notes/2026-draft-log.md`** — the reasoning behind every pick, plus 5 hypotheses to score
- **`data/2026/weekly/`** — projected vs actual, week by week
- **`scripts/analyze.py`** — projection accuracy, bias by position, points left on the bench
- **`notes/draft-strategy.md`** — the repeatable draft method, including the favorite-team rule

Weekly review is driven through a logged-in Chrome session (read *and* write — Yahoo's API is
read-only), nudged by a launchd reminder every Wednesday at 18:00.

## Status

Season in progress. Week 1 captured (partial). Yahoo projected finish: **3rd of 12**.
