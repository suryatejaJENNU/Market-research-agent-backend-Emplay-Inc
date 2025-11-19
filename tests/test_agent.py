import requests
import json

# just putting some sample text to test the backend
payload = {
    "brief": "Find top AI telecom companies, analyze their news, and give full summary."
}

# calling my fastapi endpoint (local) – change url if needed
res = requests.post("http://127.0.0.1:8000/api/research", json=payload)

print("\nSTATUS CODE:", res.status_code)
print("-" * 60)

try:
    data = res.json()
    print(json.dumps(data, indent=2))
except Exception:
    print("SERVER DID NOT RETURN JSON")
    print("Raw response:")
    print(res.text)
