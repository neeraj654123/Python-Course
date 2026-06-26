import requests
import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self,url):
        self.url=url
        self.user_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
        self.response =requests.get(url=self.url,headers=self.user_agent).text
        self.soup=BeautifulSoup(self.response,'lxml')
        
    def get_product_title(self):
        title= self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return 'Tag not found!'

    def get_product_price(self):
        price = self.soup.find("span",{"class":"a-price-whole"}).get_text().strip()
        if price is not None:
            return price
        else:
            return 'Tag not found!'
        
# device =PriceTracer('https://www.amazon.in/Samsung-Galaxy-Display-Storage-Tablet/dp/B0F29MZ848/ref=sr_1_3?crid=Y9BC5108AI56&dib=eyJ2IjoiMSJ9.P2uLX_75MhOuBnvCSiY9-ZiGgYrc68maKZ83iu34Qycuctp3OK-1q5J_f04ZIWPGkKhd0M-0agAoK8HLBN3eFidK8hIV8Rnbc9kQ_Pkf8jKM5b-oqWqS9Lu964zBvF4kR9FmDgjHBwLSjN4Zhapqqzb2Zdpn2xtVqtFuhLFQy6WDXC7yKj0IEHsPvRm1pqZT4MwHJoSQNGlrKQm0vfY3Nnmp1eY2YC0s-wbxp5sK7d4.uIngfX93kprSxLg8Q2LA5QDwyvAhtkoYC1aFapW5DHw&dib_tag=se&keywords=samsung%2Bgalaxy%2Bs10&nsdOptOutParam=true&qid=1782502488&sprefix=samsung%2Bgalaxy%2Bs10%2Caps%2C285&sr=8-3&th=1')
device=PriceTracer('https://www.amazon.in/dp/B0DY79DQQ5/ref=sspa_dk_detail_2?pd_rd_i=B0DY79DQQ5&pd_rd_w=CvbDv&content-id=amzn1.sym.cebd979a-4e06-4bc9-ba7d-b9887a34ed18&pf_rd_p=cebd979a-4e06-4bc9-ba7d-b9887a34ed18&pf_rd_r=BWX4BF1EF3DPHXP2W98M&pd_rd_wg=A8Pq1&pd_rd_r=325d9a57-c14d-4de8-8bdf-2fed14111367&aref=ssgXe8TKnx&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1')
print(device.get_product_title())
print(device.get_product_price())