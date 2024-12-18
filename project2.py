import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import base64

url = "https://sipalaya.com/"

response = requests.get(url)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

img_tags = soup.find_all('img')

os.makedirs('rato_satta_images', exist_ok=True)

for img in img_tags:
    img_url = img.get('src')
    if not img_url:
        continue

    if img_url.startswith('data:image'): 
       
        metadata, base64_data = img_url.split(',', 1)
        img_format = metadata.split(';')[0].split('/')[1]
        img_data = base64.b64decode(base64_data)

       
        img_name = f"image_{img_tags.index(img)}.{img_format}"
        with open(os.path.join('rato_satta_images', img_name), 'wb') as f:
            f.write(img_data)
        print(f"Downloaded Base64 image as {img_name}")
    else:  
        img_url = urljoin(url, img_url)

        img_name = os.path.basename(img_url.split('?')[0])  

        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            with open(os.path.join('rato_satta_images', img_name), 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded {img_name}")
        else:
            print(f"Failed to download {img_name}. Status code: {img_response.status_code}")

print("Image scraping and downloading completed.")