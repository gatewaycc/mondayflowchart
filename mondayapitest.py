import json
import urllib.request

response = requests.get("https://api.monday.com/v2")
print(response.status_code)