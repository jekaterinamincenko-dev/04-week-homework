import sys
from storage import load_list, save_list

def add_item(name, price):
    items = load_list()

    item = {
        "name": name,
        "price": float(price)
    }

    items.append(item)
    save_list(items)

    print(f"✓ Pievienots: {name} ({price} EUR)")

def list_items():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")

    for i, item in enumerate(items, start=1):
        print(f"  {i}. {item['name']} — {item['price']:.2f} EUR")

def total_items():
    items = load_list()

    total = sum(item["price"] for item in items)

    print(f"Kopā: {total:.2f} EUR ({len(items)} produkti)")

def clear_items():
    save_list([])
    print("✓ Saraksts notīrīts")

def main():
    if len(sys.argv) < 2:
        print("Komandas: add, list, total, clear")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print("Lietošana: python shop.py add Produkts Cena")
            return

        name = sys.argv[2]
        price = sys.argv[3]

        add_item(name, price)

    elif command == "list":
        list_items()

    elif command == "total":
        total_items()

    elif command == "clear":
        clear_items()

    else:
        print("Nezināma komanda")

if __name__ == "__main__":
    main()