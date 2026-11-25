#!/usr/bin/env python3
"""Start/sit audit: would a season-average check have changed any lineup call?

For every complete week, pair each starter with every *active* bench player
eligible for that slot. Each pair is a decision we made ("started S over B").
For each pair compare three orderings:

  proj   - Yahoo's weekly projection (what we lineup on)
  trail  - the player's season average to date (prior active weeks only, n>=3)
  actual - what happened

and report how often each signal picked the higher scorer, overall and for
close calls (projection gap <= CLOSE pts), where a tiebreaker could matter.

Caveats printed with the output: pairs inside one week share players, so
they are not independent; the sample is one roster, one season.

Usage: python3 scripts/startsit.py [season]
"""
import glob
import json
import os
import statistics as st
import sys

CLOSE = 2.0
MIN_HIST = 3
FLEX = {"RB", "WR", "TE"}
INACTIVE_STAT = {"Bye", "Out", "IR"}
INACTIVE_FLAG = {"O", "IR", "BYE"}

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(season):
    weeks = []
    for f in sorted(glob.glob(f"{ROOT}/data/{season}/weekly/wk*.json")):
        d = json.load(open(f))
        if d.get("complete"):
            weeks.append(d)
    return weeks


def positions(weeks):
    """Infer each player's position from the starting slots he has filled."""
    pos = {}
    for d in weeks:
        for p in d["players"]:
            if p["slot"] in ("QB", "RB", "WR", "TE", "K", "DEF"):
                pos.setdefault(p["player"], p["slot"])
    return pos


def active(p):
    return (p.get("actual") is not None and (p.get("proj") or 0) > 0
            and p.get("stat") not in INACTIVE_STAT
            and p.get("flag") not in INACTIVE_FLAG)


def eligible(bench_pos, slot):
    return bench_pos in FLEX if slot == "W/R/T" else bench_pos == slot


def pairs(weeks, pos):
    hist, out = {}, []
    for d in weeks:
        trail = {n: st.mean(h) for n, h in hist.items() if len(h) >= MIN_HIST}
        players = [p for p in d["players"] if active(p)]
        starters = [p for p in players if p["slot"] not in ("BN", "IR")]
        bench = [p for p in players if p["slot"] == "BN"]
        for s in starters:
            for b in bench:
                bp = pos.get(b["player"])
                if not bp or not eligible(bp, s["slot"]):
                    continue
                if s["player"] not in trail or b["player"] not in trail:
                    continue
                out.append(dict(week=d["week"], slot=s["slot"],
                                s=s["player"], b=b["player"],
                                sp=s["proj"], bp=b["proj"],
                                st=trail[s["player"]], bt=trail[b["player"]],
                                sa=s["actual"], ba=b["actual"]))
        for p in players:
            hist.setdefault(p["player"], []).append(p["actual"])
    return out


def score(rows, label):
    decided = [r for r in rows if r["sa"] != r["ba"]]
    n = len(decided)
    if not n:
        print(f"   {label}: no decided pairs")
        return
    proj_ok = sum((r["sp"] > r["bp"]) == (r["sa"] > r["ba"]) for r in decided)
    trail_ok = sum((r["st"] > r["bt"]) == (r["sa"] > r["ba"]) for r in decided)
    print(f"   {label:<34} n={n:>3}   proj right {proj_ok/n:5.0%}   "
          f"season-avg right {trail_ok/n:5.0%}")


def main():
    season = sys.argv[1] if len(sys.argv) > 1 else "2026"
    weeks = load(season)
    pos = positions(weeks)
    rows = pairs(weeks, pos)
    print(f"\n🔎 {season} start/sit audit — {len(weeks)} complete weeks, "
          f"{len(rows)} starter-vs-bench pairs (both active, eligible, ≥{MIN_HIST} prior games)\n")
    if not rows:
        return
    close = [r for r in rows if abs(r["sp"] - r["bp"]) <= CLOSE]
    defs = [r for r in rows if r["slot"] == "DEF"]
    score(rows, "all pairs")
    score(close, f"close calls (proj gap ≤ {CLOSE:g})")
    score([r for r in rows if r["slot"] != "DEF"], "players only (no DEF)")
    score(defs, "DEF only")

    dis = [r for r in rows if (r["sp"] > r["bp"]) != (r["st"] > r["bt"])
           and r["sa"] != r["ba"]]
    print(f"\n   Disagreements — projection and season average picked different players ({len(dis)}):")
    print(f"   {'wk':>2} {'slot':<5} {'started':<20} {'bench':<20} "
          f"{'proj':>11} {'season avg':>11} {'actual':>13}  right")
    for r in dis:
        who = "proj ✅" if (r["sp"] > r["bp"]) == (r["sa"] > r["ba"]) else "avg ✅"
        print(f"   {r['week']:>2} {r['slot']:<5} {r['s']:<20} {r['b']:<20} "
              f"{r['sp']:5.1f}/{r['bp']:<5.1f} {r['st']:5.1f}/{r['bt']:<5.1f} "
              f"{r['sa']:6.1f}/{r['ba']:<6.1f}  {who}")

    miss = [r for r in dis if r["ba"] > r["sa"]]
    print(f"\n   Calls the season average would have fixed: {len(miss)} "
          f"(bench outscored starter by {sum(r['ba']-r['sa'] for r in miss):.1f} pts total)")
    hurt = [r for r in dis if r["sa"] > r["ba"]]
    print(f"   Calls it would have broken:              {len(hurt)} "
          f"(starter beat bench by {sum(r['sa']-r['ba'] for r in hurt):.1f} pts total)")
    against = [r for r in rows if r["bp"] > r["sp"]]
    print(f"\n   Calls that went against the projection (bench projected higher) ({len(against)}):")
    for r in against:
        res = "✅ paid off" if r["sa"] > r["ba"] else ("❌ cost" if r["ba"] > r["sa"] else "= tie")
        print(f"   {r['week']:>2} {r['slot']:<5} started {r['s']:<20} ({r['sp']:.1f}) over "
              f"{r['b']:<20} ({r['bp']:.1f})  actual {r['sa']:.1f}/{r['ba']:.1f}  {res}")

    print("\n   ⚠️  Pairs within a week share players, so they are not independent; "
          "one roster, one season. Treat rates as directional.\n")


if __name__ == "__main__":
    main()
