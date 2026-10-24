from urllib.parse import urlencode
import requests

query = {"q": "What are the symptoms of high blood pressure?"}
url = f"http://localhost:8000/ask?{urlencode(query)}"

response = requests.get(url, timeout=10)
print(response.text)