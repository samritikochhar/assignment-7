import requests
response = requests.get("https://api.forismatic.com/api/1.0/")
print(response.contents)