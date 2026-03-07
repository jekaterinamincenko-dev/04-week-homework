import json
import os

FILE_NAME = "shopping.json"

def load_list():
    """Nolasa shopping.json. Ja fails neeksistē, atgriež tukšu sarakstu."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)