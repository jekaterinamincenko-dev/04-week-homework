import sys
from storage import load_list, save_list
from utils import calc_line_total, calc_grand_total, count_units


def add_item(name, qty, price):
    items = load_list()

    try:
        qty = int(qty)
        price = float(price)

        if qty <= 0 or price < 0:
            raise ValueError

    except ValueError:
        print("❌ Daudzumam jābūt pozitīvam veselam skaitlim un cenai jābūt skaitlim.")
        return

    item = {
        "name": name,
        "qty": qty,
        "price": price
    }

    items.append(item)
    save_list(items)

    total = calc_line_total(item)

    print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {total:.2f} EUR")


def list_items():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")

    for i, item in enumerate(items, start=1):
        line_total = calc_line_total(item)

        print(
            f"  {i}. {item['name']} × {item['qty']} — "
            f"{item['price']:.2f} EUR/gab. — {line_total:.2f} EUR"
        )


def total_items():
    items = load_list()

    grand_total = calc_grand_total(items)
    units = count_units(items)
    products = len(items)

    print(f"Kopā: {grand_total:.2f} EUR ({units} vienības, {products} produkti)")


def clear_items():
    save_list([])
    print("✓ Saraksts notīrīts")


def main():
    if len(sys.argv) < 2:
        print("Komandas: add, list, total, clear")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 5:
            print("Lietošana: python shop.py add Produkts Daudzums Cena")
            return

        name = sys.argv[2]
        qty = sys.argv[3]
        price = sys.argv[4]

        add_item(name, qty, price)

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