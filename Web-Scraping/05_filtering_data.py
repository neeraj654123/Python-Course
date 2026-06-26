import requests
from bs4 import BeautifulSoup
def Extract(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
    }
    response =requests.get(url=url,headers=headers).content
    soup = BeautifulSoup(response, 'lxml')
    tag=soup.find('div',{'id':'mp-right'})
    # print(tag)
    h=tag.find('ul')
    # h=tag.find('ul').find_all('li')
    # print(h)
    content =[li.text for li in h]
    print(content)
    
Extract('https://en.wikipedia.org/wiki/Main_Page')