import json
import os

SHOP_FILE = "shopping.json"
PRICE_FILE = "prices.json"

# IEPIRKUMU SARAKSTS

def load_list():
    """Nolasa shopping.json. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(SHOP_FILE):
        return []

    with open(SHOP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(SHOP_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

# CENU DATUBAZE

def load_prices():
    if not os.path.exists(PRICE_FILE):
        return {}

    with open(PRICE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_prices(prices):
    with open(PRICE_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)


def get_price(name):
    prices = load_prices()
    return prices.get(name)


def set_price(name, price):
    prices = load_prices()
    prices[name] = price
    save_prices(prices)