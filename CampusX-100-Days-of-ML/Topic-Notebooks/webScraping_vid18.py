"""import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Grab the price
    price_element = soup.find("p", class_="price_color")
    price = price_element.text

    # 2. Grab the title
    link_element = soup.find("a", title= True)
    title = link_element["title"]

    print(f"Book: {title} | Price: {price}")

else:
    print("Something went wrong.")"""


"""import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    books = soup.find_all("articles", class_= "product_pod")
    for book in books:
        price_element = book.find("p", class_="price_color")
        link_element = book.find("a", title=True)

        price = price_element.text
        title = link_element["title"]

        print(f"Book: {title} | Price: {price}")
        
else:
    print("Something went wrong.")"""

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Grab all 20 book chunks
    books = soup.find_all("article", class_="product_pod") 
    
    # Loop through each chunk to extract details
    for book in books:
        price_element = book.find("p", class_="price_color")
        link_element = book.find("a", title=True) 
        
        price = price_element.text
        title = link_element["title"]
        
        print(f"* {title} | Price: {price}")
else:
    print("Something went wrong.")



# range(1, 51) gives us numbers from 1 up to 50
for page_num in range(1, 51):
    # The 'f' at the start lets us put {page_num} right into the text
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(url)