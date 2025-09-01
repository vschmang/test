import requests
url = "https://ipinfo.io"

response = requests.get(url, timeout=10)
print(response.text)