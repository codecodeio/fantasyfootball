# 2026 season log — every week, every move

The running history of **what changed and why**, one entry per week for the whole season.
`2026-draft-log.md` scores the *draft*; this file scores the *in-season management*, so at
season's end the same question can be asked of both: was the thinking right, or did it just
happen to work?

**How to keep it:** fill in the week's section after each capture. Keep each reason to 1–2
sentences, and record the argument *against* a move where one exists so a lucky call can't
later be mistaken for a good one.

> **Opponent labels are the Yahoo team id** (Team 01 = team 1 … Team 12 = team 12; ours is id 7),
> per the anonymisation policy in the README. ⚠️ `draft.json`'s `league_totals` uses a *different*
> scheme — draft-time projection rank — so `Team NN` there is **not** the same team as `Team NN`
> here. Never join the two on the label.

## Season scoreboard

Regular season is **weeks 1–14**; weeks 12–14 rematch weeks 1–3. Playoffs are weeks 15–17 (top 6).

| Wk | Date | Opponent | Proj | Actual | Opp | Result |
|---:|---|---|---:|---:|---:|---|
| 1 | 2026-09-13 | Team 02 | 109.52 | 95.16 | 106.02 | **L** |
| 2 | 2026-09-20 | Team 01 | 103.59 | — | — | pending |
| 3 | 2026-09-27 | Team 04 | — | — | — | — |
| 4 | 2026-10-04 | Team 05 | — | — | — | — |
| 5 | 2026-10-11 | Team 09 | — | — | — | — |
| 6 | 2026-10-18 | Team 08 | — | — | — | — |
| 7 | 2026-10-25 | Team 12 | — | — | — | — |
| 8 | 2026-11-01 | Team 06 | — | — | — | — |
| 9 | 2026-11-08 | Team 10 | — | — | — | — |
| 10 | 2026-11-15 | Team 03 | — | — | — | — |
| 11 | 2026-11-22 | Team 11 | — | — | — | — |
| 12 | 2026-11-29 | Team 02 *(rematch, wk 1)* | — | — | — | — |
| 13 | 2026-12-06 | Team 01 *(rematch, wk 2)* | — | — | — | — |
| 14 | 2026-12-13 | Team 04 *(rematch, wk 3)* | — | — | — | — |
| 15 | 2026-12-20 | TBD | — | — | — | 🏆 playoffs R1 |
| 16 | 2026-12-27 | TBD | — | — | — | 🏆 playoffs R2 |
| 17 | 2027-01-03 | TBD | — | — | — | 🏆 final |
| 18 | 2027-01-10 | — | — | — | — | off (league ends wk 17) |

**Record: 0–1.** Running lineup efficiency: 76.7% (1 complete week).

⚠️ The `Proj` column is not one consistent measure, because Yahoo shows several. Week 1's 109.52
is the plain sum of the nine starters' projections. Week 2's 103.59 is the *blended* figure — eight
starters' projections plus the Lions' −2.00 actual — because their game was already final at
capture. Yahoo separately displayed 110.66 (the pure projection sum, ignoring the DEF result).
`analyze.py` never reads this column; it scores the per-player `proj` values.

**Every opponent appears exactly once before week 12.** Team 03 is a real opponent here (week 10) —
note that `draft.json` has *no* Team 03, because its labels are projection rank and rank 3 is ours.
That is the clearest illustration of why the two label schemes must never be joined.

## Season ledger — roster transactions

| Date | Wk | Type | In | Out | Cost |
|---|---|---|---|---|---|
| 2026-09-19 | 2 | Add / drop | Harrison Butker (KC, K) | Romeo Doubs (NE, WR) | Free agent — no waiver claim spent |

**Trades: none.** The draft log carries a standing recommendation to trade an RB for a WR (1st in
projected RB points, 10th in WR). Deadline **2026-11-28**, league vote.

## Bye-week planner

Current roster byes, and whether the position is covered.

| Wk | On bye | Covered? |
|---:|---|---|
| 5 | McMillan (WR), Butker (K) | ✅ Pineiro covers K; Pickens + Pierce at WR |
| 6 | Jones (RB), **Lions (DEF)** | ⚠️ **No backup DEF — must stream week 6** |
| 8 | McCaffrey (RB), Black (RB), Shough (QB), Pineiro (K) | ✅ Lamar at QB, Butker at K; RB thins to Hall/Jones/Lloyd |
| 10 | Goedert (TE) | ✅ Fannin covers |
| 11 | Fannin (TE), Lloyd (RB) | ✅ Goedert covers |
| 13 | Lamar (QB), Hall (RB), Pierce (WR) | ✅ Shough covers QB |
| 14 | Pickens (WR) | ✅ McMillan + Pierce |

**The one real hole is week 6 DEF.** Everything else is covered by the draft's bye-spread rule
(H4). Dropping Doubs removed the only week-11 WR bye, which no longer matters now that no WR
is on bye that week.

---

## Week 1 — **L** 95.16 to 106.02 (vs Team 02)

Post-draft roster, untouched. No adds, no drops, no lineup changes.

### Lineup as played

| Slot | Player | Proj | Actual | Δ |
|---|---|---:|---:|---:|
| QB | Lamar Jackson | 19.34 | 24.96 | +5.62 |
| RB | Christian McCaffrey | 17.45 | 11.30 | −6.15 |
| RB | Breece Hall | 14.24 | 18.80 | +4.56 |
| WR | George Pickens | 13.25 | 4.30 | −8.95 |
| WR | Tetairoa McMillan | 12.46 | 8.00 | −4.46 |
| TE | Harold Fannin Jr. | 8.68 | 3.10 | −5.58 |
| W/R/T | MarShawn Lloyd | 9.96 | 3.70 | −6.26 |
| K | Eddy Pineiro | 7.04 | 11.00 | +3.96 |
| DEF | Lions | 7.10 | 10.00 | +2.90 |
| | **Started** | **109.52** | **95.16** | **−14.36** |

### Bench

| Player | Pos | Proj | Actual | Δ |
|---|---|---:|---:|---:|
| Tyler Shough | QB | 18.36 | 25.20 | +6.84 |
| Dallas Goedert | TE | 7.85 | **21.70** | **+13.85** |
| Aaron Jones Sr. | RB | 7.78 | 10.00 | +2.22 |
| Alec Pierce | WR | 7.57 | 8.10 | +0.53 |
| Kaelon Black | RB | 3.48 | 7.50 | +4.02 |
| Romeo Doubs | WR | 8.14 | 0.00 | −8.14 |

**Optimal 124.10 · started 95.16 · 28.94 left on the bench · 76.7% efficiency.**
Optimal was Shough · Hall + McCaffrey · Pierce + McMillan · Goedert · Jones · Pineiro · Lions.

One decision decided it: **Goedert over Fannin was +18.60 against a 10.86 margin of defeat** — that
swap alone wins the week. Jones over Lloyd (+6.30) was real but not enough on its own.

---

## Week 2 — projected 103.59 vs 100.77 (vs Team 01) · result pending

| # | Move | Δ proj | Why |
|---|---|---:|---|
| 1 | **+ Butker / − Doubs** | — | Pineiro missed all three practices with an illness and SF said it would sign a practice-squad kicker; with no backup K, that slot risked a zero in a two-point matchup. Doubs was the weakest asset — 0.00 on 3 targets in week 1, 10% started. |
| 2 | **Goedert in, Fannin out** (TE) | +0.26 | Projections were tied, so usage broke it: Goedert 5 tgt / 77 yds on a winning offence, Fannin 3 tgt / 21 yds in a 10–34 loss. Not because Goedert scored 21.70 — two TDs supplied 12 of that and it won't repeat. |
| 3 | **Jones in, Lloyd out** (W/R/T) | +1.21 | Lloyd ran 2.8 ypc with zero receiving work; Jones beat his projection, scored, and catches passes in half-PPR. |
| 4 | **Butker in, Pineiro out** (K) | −0.61 | Safe default so an inactive Pineiro can't leave a zero. Reversible until ~2:55pm Sunday — if Pineiro is active, swap back for +0.61. |

**Why Butker specifically:** top FA kicker (7.61) *and* he kicks at 8:20pm, after the 4:25 SF game,
so the call waits for the injury news instead of guessing.

**What the drop cost:** bench is now 3 WRs deep for 2 WR + flex. The house bye rule still holds
(WR byes 14/5/13).

### Opponent snapshot — Team 01 (as of 2026-09-19 09:20)

| | Team 01 | Us |
|---|---:|---:|
| Record | 1–0 (6th) | 0–1 (11th) |
| Yahoo "orig proj" | 100.76 | 110.72 |
| Yahoo live proj | 100.76 | 98.72 |
| Win probability | **52% favourite** | 48% underdog |

⚠️ **We have drifted from favourite to underdog since the lineup was set.** At capture the blended
figure was 103.59 v 100.77; Yahoo's live projection now has us at 98.72. Their projection has not
moved — ours has. Worth a re-check before the 1:00pm kickoffs; if the drop traces to a player
downgrade rather than the DEF result, there may be another swap to make.

Their lineup is WR-strong (Chase, Samuel) against exactly our weakest position group — the draft
log's standing RB-for-WR trade recommendation is the structural answer to this matchup, and the
week 12 rematch is the reason to act on it before the 2026-11-28 deadline.

### 🚫 The slot lost before the weekend

Lions DEF finished **−2.00** Thursday night and locked, against the Bills — who give up the
**fewest** fantasy points to defences in the league. **The DEF decision has a Thursday deadline,
not a Sunday one**, and the Wednesday reminder's six-point checklist doesn't currently mention it.

### Did the opponent drive these decisions?

**The fantasy opponent (Team 01) changed the *threshold*, not the *picks*.** The matchup projected
102.73 vs 100.77 before any changes, and that 1.96-point margin is why marginal upgrades were worth
making at all. But no player was chosen *because of* Team 01.

**The NFL defences did *not* drive these calls, and at week 2 they shouldn't.** Two reasons.

**1. The projection already contains the matchup.** Rotowire's weekly numbers are opponent-adjusted
— that is what makes them weekly rather than seasonal. Goedert 8.35 and Fannin 8.09 are *post*-
matchup figures, so benching Goedert because TB is soft against TEs would count the matchup twice.

**2. The points-against table is one game per team, and is often circular.** Washington ranked
3rd-worst against TEs entering week 2 on a line of 4 rec / 77 yds / 2 TD / 21.70 — that is
*Goedert's own week 1 game*, and nothing else. Pittsburgh "allows the fewest to WRs" off a single
game in which one target went to a receiver. These are not defensive properties yet; they are a
list of who each defence happened to face.

| Player | Faces | Rank vs position | Worth |
|---|---|---|---|
| Aaron Jones (started) | @ CHI | 7th most to RBs | 1 game — directional only |
| MarShawn Lloyd (benched) | @ NYJ | 2nd fewest to RBs | 1 game — directional only |
| Romeo Doubs (dropped) | vs PIT | Fewest to WRs | 1 game, and PIT faced 1 WR target |
| Harrison Butker (started) | vs IND | 4th most to Ks | 1 game — directional only |
| Lions (locked, −2.00) | @ BUF | Fewest to DEFs | Confirmed the hard way |
| Goedert (started) | @ TEN | 12th most to TEs | Argues for Fannin — overruled |
| Fannin (benched) | @ TB | 4th most to TEs | Argues for Fannin — overruled |

⚠️ **Correction to an earlier version of this file**, which labelled these "✅ confirms". That
overstated them. Jones-over-Lloyd was called the best-supported move on NYJ ranking 31st against
RBs — but Minnesota ranks 32nd partly *because Lloyd's own 3.70 is in their column*. The move still
looks right on usage; the matchup evidence for it was partly circular.

**The TE swap went against the matchup table deliberately.** Fannin has the friendlier draw. He was
benched anyway because Rotowire projects Goedert higher *despite* that draw, and because Fannin's
3 targets came in a 10–34 loss — a script where Cleveland threw constantly. Not being involved when
your team is forced to pass is worse than a low target count in a normal game. **If Fannin outscores
Goedert, examine this first.**

---

## Week 3 — 2026-09-27
*Not yet played. Byes: none.*

## Week 4 — 2026-10-04
*Not yet played. Byes: none.*

## Week 5 — 2026-10-11
*Not yet played. Byes: McMillan (WR), Butker (K) — Pineiro covers K.*

## Week 6 — 2026-10-18
*Not yet played. Byes: Jones (RB), **Lions (DEF)**.*
⚠️ **No backup DEF rostered — stream one by Thursday.**

## Week 7 — 2026-10-25
*Not yet played. Byes: none.*

## Week 8 — 2026-11-01
*Not yet played. Byes: McCaffrey (RB), Black (RB), Shough (QB), Pineiro (K).*
RB thins to Hall / Jones / Lloyd for two starting spots plus flex.

## Week 9 — 2026-11-08
*Not yet played. Byes: none.*

## Week 10 — 2026-11-15
*Not yet played. Byes: Goedert (TE) — Fannin covers.*

## Week 11 — 2026-11-22
*Not yet played. Byes: Fannin (TE), Lloyd (RB) — Goedert covers.*

## Week 12 — 2026-11-29
*Not yet played. Byes: none.* **Trade deadline passed 2026-11-28.**

## Week 13 — 2026-12-06
*Not yet played. Byes: Lamar (QB), Hall (RB), Pierce (WR) — Shough covers QB.*

## Week 14 — 2026-12-13
*Not yet played. Byes: Pickens (WR).* Last week before the playoffs.

## Week 15 — 2026-12-20 · 🏆 Playoffs round 1
*Not yet played. Top 6 teams qualify.*

## Week 16 — 2026-12-27 · 🏆 Playoffs round 2
*Not yet played.*

## Week 17 — 2027-01-03 · 🏆 Final
*Not yet played.* ⚠️ **Capture this week at minimum**, even if the season's logging lapses.

## Week 18 — 2027-01-10
*League ends week 17. No fantasy games.*

---

## Template for a week entry

```
## Week N — <result / projected X vs Y> (vs Team NN)

| # | Move | Δ proj | Why (1–2 sentences) |

Matchup influence — fantasy opponent: threshold or selection?
                    NFL defences: driven, or merely confirmed?
Points left on the bench: optimal / started / efficiency
The argument against the call, where one exists.
```
