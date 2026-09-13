#!/bin/bash
# Deploy remind.sh outside ~/Documents (TCC-protected) and (re)load the launchd job.
set -eu
REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST_DIR="$HOME/Library/Application Support/fantasyfootball"
PLIST="$HOME/Library/LaunchAgents/com.fantasyfootball.weeklyreminder.plist"

mkdir -p "$DEST_DIR" "$HOME/Library/Logs/fantasyfootball"
cp "$REPO/scripts/remind.sh" "$DEST_DIR/remind.sh"
chmod +x "$DEST_DIR/remind.sh"

cat > "$PLIST" <<XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>com.fantasyfootball.weeklyreminder</string>
	<key>ProgramArguments</key>
	<array>
		<string>/bin/bash</string>
		<string>$DEST_DIR/remind.sh</string>
	</array>
	<key>RunAtLoad</key>
	<false/>
	<key>StandardErrorPath</key>
	<string>$HOME/Library/Logs/fantasyfootball/reminder.log</string>
	<key>StandardOutPath</key>
	<string>$HOME/Library/Logs/fantasyfootball/reminder.log</string>
	<key>StartCalendarInterval</key>
	<array>
		<dict>
			<key>Hour</key><integer>18</integer>
			<key>Minute</key><integer>0</integer>
			<key>Weekday</key><integer>3</integer>
		</dict>
	</array>
</dict>
</plist>
XML

plutil -lint "$PLIST" >/dev/null
launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"
echo "✅ reminder installed -> $DEST_DIR/remind.sh  (Wednesdays 18:00)"
