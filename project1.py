from bs4 import BeautifulSoup
import requests
url = "https://sipalaya.com"
response = requests.get(url)

if response.status_code == 200:
    print("Connected to the website successfully")
else:
    print("Failed to connect to the website")
    exit()

soup = BeautifulSoup(response.content, "html.parser")

items = soup.find_all('h6')


print("Items :")
for i, title in enumerate(items, 1):
    print(f"{i}. {title.text.strip()}")


with open("items.txt", "w") as file:
    for title in items:
        file.write(title.text.strip() + "\n")

print("items saved to 'items.txt'")