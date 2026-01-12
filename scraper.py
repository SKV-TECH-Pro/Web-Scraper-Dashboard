import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

URL = "https://example.com/product-page"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_price():
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # ⚠️ Update this selector based on real website
    price_text = soup.find("span", class_="price").get_text()
    price = float(price_text.replace("$", "").replace(",", ""))

    return price


def save_price(price):
    file_exists = os.path.isfile("prices.csv")

    data = {
        "date": [datetime.now()],
        "price": [price]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "prices.csv",
        mode="a",
        header=not file_exists,
        index=False
    )


if __name__ == "__main__":
    price = get_price()
    save_price(price)
    print(f"Saved price: ${price}")