# 08 — GitHub Agent

Automate GitHub workflows — search repositories and create issues programmatically.

## What it does
- **repo-analyzer**: Search GitHub for repos matching a query, ranked by stars
- **create-issue**: Create a GitHub issue in any repo via the API

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| GitHub Search | GET /github/search | $0.001 |
| GitHub Issue | POST /github/issue | $0.002 |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Search repos
python3 repo-analyzer.py

# Create issue
./create-issue.sh owner/repo "Bug: something is broken" "Steps to reproduce..."
```
