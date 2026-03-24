# 06 — Code Execution

Run sandboxed code (Python, JavaScript, Bash) securely in the cloud.

## What it does
- Execute arbitrary code without setting up a local environment
- Secure sandboxed execution — no host access
- Supports Python, JavaScript, Bash

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| Code Execute | POST /code_execute | $0.005 |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Bash example
./run-python.sh

# Python data analysis
python3 data-analysis.py
```
