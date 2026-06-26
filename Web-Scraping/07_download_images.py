import requests
import re
from urllib.parse import urljoin
import os

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers).text

pattern = r'<img[^>]+src="([^"]+)"'

images = re.findall(pattern, response)
print(f"Total images ={len(images)}")
no_of_images=int(input("Enter how many images you want to download: "))


if images:
    if os.path.exists("images") == False:
        os.mkdir("images") 
        os.chdir("images")
    else:
        os.chdir("images")
    for img in images[:no_of_images]:
        img_url=urljoin(url, img)
        response=requests.get(url=img_url).content
        image_name=img_url.split("/")[-1]
        with open(image_name,'wb') as image:
            image.write(response)
        print(f"Image {image_name} downloaded successfully")
else:
    print("No images found")
    
# print(type(img))