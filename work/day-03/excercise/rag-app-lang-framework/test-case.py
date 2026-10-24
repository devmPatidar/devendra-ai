import requests

response = requests.post(
	"http://localhost:8000/ask",
	json={"query": "What are the symptoms of high blood pressure?"},
	timeout=60,
)
response.raise_for_status()
print(response.json())