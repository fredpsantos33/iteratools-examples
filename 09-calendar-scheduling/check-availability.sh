#!/bin/bash
# Check Google Calendar availability
# Cost: $0.001 per check
# Requires: GOOGLE_SA_JSON (base64 service account JSON) or GOOGLE_OAUTH_TOKEN
API_KEY="${ITERA_KEY:?Set ITERA_KEY}"
CALENDAR="${1:-primary}"

echo "📅 Checking availability... (\$0.001)"
curl -s "https://api.iteratools.com/calendar/availability" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"google_service_account_json\": \"${GOOGLE_SA_JSON:-}\", \"calendar_id\": \"$CALENDAR\", \"days\": 7, \"slot_minutes\": 60}" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
free = d.get('free_slots', [])
print(f'Found {len(free)} free slots in the next 7 days:')
for slot in free[:5]:
    print(f'  🟢 {slot}')
if len(free) > 5:
    print(f'  ... and {len(free)-5} more')
"
