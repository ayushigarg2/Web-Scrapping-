# Made by Ayushi Garg
# This module fetches the price from the amazon links 

import requests
from bs4 import BeautifulSoup

# Headers For Amazon Fetching

h = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
 

def fetch_data(url):
    try:
        # Fetching The Amazon URL
        r = requests.get(url, headers=h, timeout=5)

        # Converting Fetched Page to HTML document
        soup = BeautifulSoup(r.content, 'html.parser')

        price = soup.find(id="corePriceDisplay_desktop_feature_div").find( class_="a-price-whole").text.strip()

        # Remove the comma from the price, and convert to integer
        price = eval(price.replace(",", ""))

        # Fetch Name
        name = soup.find("h1", class_="a-size-large a-spacing-none").text.strip()
        return name, price

    except:
        return "Error", -1
