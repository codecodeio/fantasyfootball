#!/usr/bin/env python3
"""Score Yahoo's projections and our lineup decisions against reality.

Usage:  python3 scripts/analyze.py [season]

Reads data/<season>/draft.json and data/<season>/weekly/wk*.json.
Honest reporting: small samples are flagged, never smoothed over.
"""
import json
import sys
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent.parent
STARTERS = {"QB", "RB", "WR", "TE", "W/R/T", "K", "DEF"}
MIN_SAMPLE = 4  # weeks below this get an explicit small-sample warning


def load(season):
    base = ROOT / "data" / str(season)
    draft = json.loads((base / "draft.json").read_text())
    weeks = []
    for f in sorted((base / "weekly").glob("wk*.json")):
        weeks.append(json.loads(f.read_text()))
    return draft, weeks


def scored(week):
    """Players with a real actual value this week."""
    return [p for p in week["players"] if p.get("actual") is not None]


def projection_accuracy(weeks):
    rows = [(p["player"], p["slot"], p["proj"], p["actual"])
            for w in weeks for p in scored(w)]
    if not rows:
        return None
    errs = [a - pr for _, _, pr, a in rows]
    by_pos = {}
    for _, slot, pr, a in rows:
        pos = "FLEX" if slot == "W/R/T" else ("BN" if slot == "BN" else slot)
        by_pos.setdefault(pos, []).append(a - pr)
    return {
        "n": len(rows),
        "mae": mean(abs(e) for e in errs),
        "bias": mean(errs),
        "by_pos": {k: {"n": len(v), "bias": mean(v)} for k, v in sorted(by_pos.items())},
        "worst": [r for r in sorted(rows, key=lambda r: r[3] - r[2]) if r[3] < r[2]][:3],
        "best": [r for r in sorted(rows, key=lambda r: r[2] - r[3]) if r[3] > r[2]][:3],
    }


def lineup_efficiency(weeks):
    """Points left on the bench: could a bench player have beaten a starter?"""
    out = []
    for w in weeks:
        done = scored(w)
        starters = [p for p in done if p["slot"] in STARTERS]
        bench = [p for p in done if p["slot"] == "BN"]
        if not starters or not bench:
            continue
        actual = sum(p["actual"] for p in starters)
        # crude: best bench score vs worst starter score (same-week, ignores position rules)
        gain = max(0.0, max(b["actual"] for b in bench) - min(s["actual"] for s in starters))
        out.append({"week": w["week"], "started": round(actual, 2), "left_on_bench": round(gain, 2)})
    return out


def main():
    season = sys.argv[1] if len(sys.argv) > 1 else "2026"
    draft, weeks = load(season)
    complete = [w for w in weeks if w.get("complete")]
    partial = [w for w in weeks if not w.get("complete")]

    print(f"\n🏈 {draft['season']} — projection vs reality\n")
    print(f"   Weeks captured: {len(weeks)}  ({len(complete)} complete, {len(partial)} partial)")
    if len(complete) < MIN_SAMPLE:
        print(f"   ⚠️  Small sample — {len(complete)} complete week(s). Treat everything below as directional only.")

    acc = projection_accuracy(weeks)
    if not acc:
        print("\n   ❌ No scored players yet. Run a capture after games finish.\n")
        return

    print(f"\n📊 Projection accuracy  (n={acc['n']} player-weeks)")
    print(f"   Mean absolute error : {acc['mae']:.2f} pts")
    sign = "over" if acc["bias"] < 0 else "under"
    print(f"   Bias                : {acc['bias']:+.2f} pts  (Yahoo projects {sign})")

    print("\n   By slot:")
    for pos, d in acc["by_pos"].items():
        flag = "  ⚠️ n<4" if d["n"] < MIN_SAMPLE else ""
        print(f"     {pos:<6} n={d['n']:<3} bias {d['bias']:+7.2f}{flag}")

    for label, key in (("📉 Biggest misses (proj → actual)", "worst"), ("📈 Biggest beats", "best")):
        if acc[key]:
            print(f"\n   {label}:")
            for name, slot, pr, a in acc[key]:
                print(f"     {name:<24} {pr:6.2f} → {a:6.2f}  ({a - pr:+.2f})")

    eff = lineup_efficiency(weeks)
    if eff:
        print("\n🪑 Lineup efficiency")
        for e in eff:
            note = "✅ optimal" if e["left_on_bench"] == 0 else f"❌ {e['left_on_bench']:.2f} left on bench"
            print(f"     wk{e['week']:<3} started {e['started']:6.2f}   {note}")

    print("\n🧪 Hypotheses — see notes/{}-draft-log.md; score these at season end.\n".format(draft["season"]))


if __name__ == "__main__":
    main()
