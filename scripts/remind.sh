#!/usr/bin/env bash
# Wednesday-evening nudge to review + alter the fantasy lineup.
# Waivers process game-time Tuesday, so Wednesday evening is the first clean
# window to set the coming week's lineup. Fired by launchd:
#   ~/Library/LaunchAgents/com.fantasyfootball.weeklyreminder.plist
set -u

TEAM_URL="https://football.fantasysports.yahoo.com/f1/1396154/7"
LOG_DIR="$HOME/Library/Logs/fantasyfootball"
mkdir -p "$LOG_DIR"

# NFL week: anchored to Tue 2026-09-08, the day before the Week 1 prep window.
week=$(python3 -c "
from datetime import date
d = (date.today() - date(2026, 9, 8)).days
print(max(1, min(18, d // 7 + 1)))
" 2>/dev/null || echo "?")

title="🏈 Fantasy — Week ${week} setup"
msg="Review lineup, waivers and injuries. Waivers cleared yesterday."

# Notify. -e is safer than a here-doc for quoting; failure must not kill the job.
osascript -e "display notification \"${msg}\" with title \"${title}\" sound name \"Submarine\"" 2>>"$LOG_DIR/remind.log" || true

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] reminded — week ${week}"
  echo "    team: $TEAM_URL"
  echo "    checklist:"
  echo "      1. injuries / O and Q flags on every starter"
  echo "      2. bye weeks — see notes/2026-draft-log.md for the season map"
  echo "      3. waiver adds (no acquisition limits in this league)"
  echo "      4. flex: best projection, weighing floor when favoured"
  echo "      5. favorite-team rule — PHI player rostered? (draft-strategy.md rule 2)"
  echo "      6. capture last week: data/2026/weekly/wkNN.json"
} >> "$LOG_DIR/remind.log"

exit 0
