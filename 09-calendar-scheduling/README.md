# 09 — Calendar Scheduling

Google Calendar integration — check availability and schedule events automatically.

## What it does
- **check-availability**: Lists free time slots in the next N days
- **scheduling-agent**: Finds first available slot and creates a calendar event

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| Check Availability | GET /calendar/availability | $0.001 |
| Create Event | POST /calendar/event | $0.002 |

## Auth

Set one of:
- `GOOGLE_SA_JSON` — base64-encoded service account JSON (for server use)
- `GOOGLE_OAUTH_TOKEN` — OAuth2 access token (for user-facing apps)

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"
export GOOGLE_SA_JSON="$(base64 -w0 service-account.json)"

# Check free slots
./check-availability.sh primary

# Auto-schedule
python3 scheduling-agent.py
```
