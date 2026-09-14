import os
import json
import urllib.request

token = os.environ["TELEGRAM_BOT_TOKEN"]

url = f"https://api.telegram.org/bot{token}/getUpdates"

with urllib.request.urlopen(url) as response:
    data = json.load(response)

print(json.dumps(data, indent=2, ensure_ascii=False))
