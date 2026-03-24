#!/bin/bash
# Execute Python code in a secure sandbox
# Cost: $0.005 per execution
API_KEY="${ITERA_KEY:?Set ITERA_KEY}"

CODE='
import math, json
data = [1, 4, 9, 16, 25, 36, 49]
result = {
    "squares": data,
    "roots": [round(math.sqrt(x), 2) for x in data],
    "sum": sum(data),
    "mean": sum(data) / len(data)
}
print(json.dumps(result, indent=2))
'

echo "💻 Executing Python in sandbox... (\$0.005)"
curl -s -X POST https://api.iteratools.com/code_execute \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"language\": \"python\", \"code\": $(python3 -c "import json,sys; print(json.dumps(sys.stdin.read()))" <<< "$CODE")}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('output',''))"
