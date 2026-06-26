import requests

url ='https://picsum.photos/seed/helloworld/500/300'
user ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=user)
# print(type(response.content))
pic=response.content
f= open('picsum.photos','wb')
f.write(pic)