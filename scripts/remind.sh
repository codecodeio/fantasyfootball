#!/bin/bash
# Wednesday-evening nudge to review + alter the fantasy lineup.
# Waivers process game-time Tuesday, so Wednesday evening is the first clean
# window to set the coming week's lineup.
#
# NOTE: this runs from ~/Library/Application Support/fantasyfootball/, NOT from
# the repo. A new launchd label has no TCC grant for ~/Documents and cannot
# prompt for one, so executing from there fails with EPERM (exit 126).
# Install/refresh the deployed copy with:  ff install-reminder
set -u

TEAM_URL="https://football.fantasysports.yahoo.com/f1/1396154/7"
LOG_DIR="$HOME/Library/Logs/fantasyfootball"
mkdir -p "$LOG_DIR"

PY=""
for c in /usr/bin/python3 /opt/homebrew/bin/python3 /usr/local/bin/python3; do
  [ -x "$c" ] && { PY="$c"; break; }
done

if [ -n "$PY" ]; then
  week=$("$PY" -c "
from datetime import date
d = (date.today() - date(2026, 9, 8)).days
print(max(1, min(18, d // 7 + 1)))
" 2>/dev/null) || week="?"
else
  week="?"
fi

title="🏈 Fantasy — Week ${week} setup"
msg="Review lineup, waivers and injuries. Waivers cleared yesterday."

/usr/bin/osascript -e "display notification \"${msg}\" with title \"${title}\" sound name \"Submarine\"" \
  2>>"$LOG_DIR/remind.log" || true

{
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] reminded — week ${week}"
  echo "    team: $TEAM_URL"
  echo "    1. injuries / O and Q flags on every starter"
  echo "    2. bye weeks — notes/2026-draft-log.md has the season map"
  echo "    3. waiver adds (no acquisition limits in this league)"
  echo "    4. flex: best projection, weighing floor when favoured"
  echo "    5. favorite-team rule — PHI player rostered? (draft-strategy.md rule 2)"
  echo "    6. capture last week -> data/2026/weekly/wkNN.json"
} >> "$LOG_DIR/remind.log"

exit 0
