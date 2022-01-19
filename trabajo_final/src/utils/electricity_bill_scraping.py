import requests
from bs4 import BeautifulSoup

def scrap():
    page = requests.get("http://www.tarifadeluz.com")
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

    rows = soup.select("table tbody tr")

    prices = []
    for row in rows:
        columns = row.select("td")
        price_cell = columns[1]
        price = price_cell.select("font")[0].text.replace(" ", "")

        prices.append(float(price))

    return prices

