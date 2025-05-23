import requests

url = 'https://www.google.com'

response = requests.get(url)

response.encoding = 'utf-8'

print(response.text)

print(response.status_code)