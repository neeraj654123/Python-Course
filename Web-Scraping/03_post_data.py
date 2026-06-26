import requests

url='http://127.0.0.1:8000/posts/'
payload={
    'title': 'Greating',
    'content': 'Hello everyone',
    }
response=requests.post(url=url,data=payload,
    auth=("asus", "asus12345"))
print(response.text)
