# 05 — Browser Automation

Automate browsers — screenshot, describe, and interact with web pages.

## What it does
- **screenshot-and-describe**: Takes a screenshot of any URL and describes it with GPT-4o Vision
- **form-automation**: Navigates a page and fills out a form using browser actions

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| Screenshot | POST /screenshot | $0.003 |
| Image Describe | POST /image/describe | $0.008 |
| Browser Automation | POST /browser/act | $0.005 |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Screenshot + describe
./screenshot-and-describe.sh https://iteratools.com

# Form automation
python3 form-automation.py
```
