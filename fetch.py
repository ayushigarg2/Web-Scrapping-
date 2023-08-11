# Made by Ayushi Garg
# This module fetches the price from the amazon links 

import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    # Headers For Amazon Fetching
    h = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    try:
        # Fetching The Amazon URL
        r = requests.get(url, headers=h, timeout=5)

        # Converting Fetched Page to HTML document
        soup = BeautifulSoup(r.content, 'html.parser')

        price = soup.find("div", class_="a-section a-spacing-none aok-align-center").find("span", class_="a-price-whole").text.strip()

        # Remove the comma from the price, and convert to integer
        price = eval(price.replace(",", ""))

        # Fetch Name
        name = soup.find("h1", class_="a-size-large a-spacing-none").text.strip()
        return name, price

    except:
        return "Error", -1
