import requests
url="http://127.0.0.1:8000/"
respone =requests.get(url=url)
print(respone.text)
print(type(respone.text))