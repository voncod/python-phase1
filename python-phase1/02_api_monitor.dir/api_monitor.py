import json

import requests
import yaml

with open("config.yaml") as file:
    config = yaml.safe_load(file)

api_url = config["api"]["url"]
timeout = config["api"]["timeout"]

report = {
    "url": api_url,
    "status": "unhealthy",
    "http_status": None,
    "items_received": 0
}

try:
    response = requests.get(
            api_url,
            timeout=timeout
    )
    response.raise_for_status()

except requests.Timeout:
    print("Request timed out.")
    exit()

except requests.HTPPError:
    print("HTTP Error:", response.status_code)
    exit()

except requests.RequestExcepetion:
    print("Request failed.")
    exit()

data = response.json()

report["status"] = "healthy"
report["http_status"] = response.status_code
report["items_received"] = len(data)

with open("health_report.json", "w") as file:
    json.dump(report, file, indent=4)

