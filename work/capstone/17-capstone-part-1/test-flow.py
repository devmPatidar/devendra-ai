import os

import requests

url = "http://localhost:7860/api/v2/workflows"
payload = {
    "flow_id": "c42c5361-a87a-4746-80aa-18910a8815e4",
    "input_value": "windows password policy!"
}
headers = {
    "Content-Type": "application/json",
    "x-api-key": "sk-qNz-70oQVfAE8wvyRadRAVpwVDbfBtxcj_ivZNHx_Ow",
}

response = requests.post(url, json=payload, headers=headers)
response.raise_for_status()
result = response.json()

# The text reply is in output.text:
print(result["output"]["text"])