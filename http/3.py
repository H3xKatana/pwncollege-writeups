import requests


res=requests.get('http://localhost')

print(res.text)
