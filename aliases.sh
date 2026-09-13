#!/usr/bin/env bash
# fantasyfootball — `ff` command. Enable: add  source <abs-path>/aliases.sh  to ~/.zshrc, then `refresh`.
export FANTASYFOOTBALL_DIR="/Users/matt/Documents/Development/Git/repos/fantasyfootball"

ff() {
  local cmd="${1:-help}"; [ $# -gt 0 ] && shift
  case "$cmd" in
    help|-h|--help)
      cat <<'EOF'
ff <command>:
  analyze [season]  score projections vs actuals (default 2026)
  draft [season]    show the draft record
  log [season]      open the decision log
  week <NN>         show a captured week
  remind            fire the Wednesday nudge now (test it)
  reminder-status   is the launchd job loaded?
  cd                cd into the project
  help              this list
EOF
      ;;
    analyze) python3 "$FANTASYFOOTBALL_DIR/scripts/analyze.py" "${1:-2026}" ;;
    draft)   python3 -m json.tool "$FANTASYFOOTBALL_DIR/data/${1:-2026}/draft.json" ;;
    log)     "${EDITOR:-open}" "$FANTASYFOOTBALL_DIR/notes/${1:-2026}-draft-log.md" ;;
    week)
      [ -z "${1:-}" ] && { echo "usage: ff week <NN>" >&2; return 1; }
      python3 -m json.tool "$FANTASYFOOTBALL_DIR/data/2026/weekly/wk$(printf '%02d' "$1").json" ;;
    remind)  bash "$FANTASYFOOTBALL_DIR/scripts/remind.sh" && echo "✅ reminder fired" ;;
    reminder-status)
      if launchctl list | grep -q com.fantasyfootball.weeklyreminder; then
        echo "✅ loaded — Wednesdays 18:00"
      else
        echo "❌ not loaded: launchctl load ~/Library/LaunchAgents/com.fantasyfootball.weeklyreminder.plist"
      fi ;;
    cd)      cd "$FANTASYFOOTBALL_DIR" ;;
    *)       echo "ff: unknown command '$cmd' (try: ff help)" >&2; return 1 ;;
  esac
}
