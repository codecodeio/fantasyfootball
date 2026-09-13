# Draft strategy

The method used in 2026, written down so it can be repeated, argued with, and scored against
results. Every rule here should end the season either confirmed or rejected — see the hypotheses
in `2026-draft-log.md`.

## Set these constraints *before* the draft

### 1. Bye rule
No two players at the **same position** may share a bye week. Handcuffs are exempt — a backup is
insurance, not a rotational starter.

Corollary for the bench: rank bench candidates by **bye spread, not raw projection**. A bench
player's job is to cover the weeks your starters are out. A high-projection body who sits on the
same bye as the starter he's meant to replace is worth nothing.

### 2. Favorite-team rule 🦅
**Pick one NFL team before the draft and guarantee at least one player from it.** The season is
more fun with someone to root for, and the cost is controllable *if you plan it*.

The method:

1. **Before the draft**, list every player from that team with projection and ADP.
2. For each, compute the real cost: `cost = (best player available at that ADP) − (this player's projection)`.
   Cost is *not* the player's projection — it's what you give up by taking them instead.
3. **Prefer the one who also fills a genuine roster need.** This is the whole trick. A favorite-team
   player who doubles as your TE2 or WR4 costs approximately **zero**.
4. Set a **maximum acceptable cost up front** — 25 season points (~1.5/week) is a reasonable ceiling.
5. 🚫 **Never take the premium option** (the team's RB1 or starting QB) purely to satisfy this.
   That is where the cost explodes, and it is always avoidable.
6. Queue two or three candidates, not one. They get drafted by other people.

**2026 case study — Eagles.** Six candidates existed:

| Player | Proj | ADP | Cost to take | Outcome |
|---|---|---|---|---|
| Barkley RB | 213.3 | 11.0 | very high | unreachable from slot 4 |
| Hurts QB | 296.1 | 55.0 | ~9–23 pts | 🚫 premium option, declined |
| D. Smith WR | 183.8 | 29.4 | ~0 (would've been WR2) | drafted by someone else |
| Eagles DEF | 110.9 | 124.5 | ~8 pts | drafted by someone else |
| **Goedert TE** | **121.6** | **104.2** | **~0 — was also TE2** | ✅ **taken at 100** |
| Lemon WR | 104.8 | 119.4 | ~0 | free, but roster filler |

**Lesson: the cheapest satisfying player is usually the one who also fills a bench need.**
Goedert covered Fannin's Week 11 bye *and* the Eagles rule in a single roster spot. Four of the six
candidates were gone before they could be taken — hence rule 6.

**Weekly corollary.** Starting a favorite-team player you'd enjoy watching is worth it when the
projection cost is small *and* their floor is no worse. Week 1 2026 is the worked example.
Goedert (7.93) in the flex over Lloyd (9.98) costs 2.05 projected points, but Goedert was started
in 47% of leagues against Lloyd's 29%, with a defined role versus an explicit committee. Against a
24-point projected lead, trading 2 points of median for a higher floor is roughly free in
win-probability terms. **Enjoyment is a real term in the objective function; just make sure you've
priced it.**

> ⚠️ **Unreconciled — this is the argument, not a record of what was started.** `wk01.json` was
> captured with **Lloyd** in the W/R/T slot and Goedert on the bench. Whether the swap was made
> before the 4:25 kickoff is unknown until Week 1 is re-captured. Do not cite Week 1 as evidence
> for this rule until the finalised capture settles it.

## In-draft rules

### 3. ADP sequencing — take the player who's leaving
When two targets are close in value, take the one whose **ADP will not survive to your next pick**.
Used at picks 21, 45, 69, 93 and 100 in 2026.

> Pick 21: Pickens (218.3, ADP 22.6) over Hall (218.9, ADP 34.3) — Hall survived to 28. Both acquired.

### 4. Compare bundles, not players
Never compare two players at one pick. Compare **what your roster looks like two picks from now**
under each branch. The TE-cliff call at pick 28 was decided this way: McBride + a ~186 RB beat
Hall + a ~156 TE by 5 points.

### 5. Wait on QB — unless a tier breaks
In a 1-QB, 4-pt-passing-TD league the QB gradient is nearly flat: QB5 to QB15 was 16 points in 2026.
Take a mid-tier QB late. **The exception is a genuine tier break that slides** — Lamar at 313.2 was
+26.6 over the next QB and fell 13 picks past ADP, which flipped the math.

### 6. Read the injury flag *and* the games-played column
A `Q` already priced into a projection is not a discount to fear — Hall's 218.9 was over 15 games,
not 16. An `O` is disqualifying regardless of how good the projection looks.

### 7. Bench points don't score
For the last bench spots, stop maximizing projection and start maximizing
`P(enters lineup) × value when starting`. This is why K. Black (54.3) beat R. White (133.7) — White
would have been RB5 and never started; Black starts the day McCaffrey sits.

### 8. K and DEF in the last two rounds, one each
The 2026 spread was **3.3 points across the top four kickers** and 14 across eight defenses.
Never roster two. Three teams in this league drafted a second K or DEF and finished with the two
worst WR corps and the worst RB corps in the league.

Split the K and DEF byes so you never have to stream both in the same week.
