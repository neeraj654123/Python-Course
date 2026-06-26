import requests

url='http://127.0.0.1:8000/posts/'
params={
    'offset': '3',
    'page': '2'
    
    } 
response=requests.get(url=url,params=params,auth=("asus", "asus12345"))
# print(response.text)
print(response.url)
 