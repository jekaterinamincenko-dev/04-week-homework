import sys
from storage import load_list, save_list, get_price, set_price
from utils import calc_line_total, calc_grand_total, count_units


def ask_price(name):
    """Prasa lietotājam cenu."""
    while True:
        try:
            price = float(input("Ievadi cenu: > "))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("❌ Cenai jābūt pozitīvam skaitlim.")


def resolve_price(name):
    """Nosaka cenu: no datubāzes vai prasa lietotājam."""
    price = get_price(name)

    if price is None:
        print("Cena nav zināma.")
        price = ask_price(name)

        set_price(name, price)
        print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")

        return price

    print(f"Atrasta cena: {price:.2f} EUR/gab.")

    choice = input("[A]kceptēt / [M]ainīt? > ").strip().lower()

    if choice == "m":
        price = ask_price(name)
        set_price(name, price)
        print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")

    return price


def add_item(name, qty):
    items = load_list()

    try:
        qty = int(qty)
        if qty <= 0:
            raise ValueError
    except ValueError:
        print("❌ Daudzumam jābūt pozitīvam veselam skaitlim.")
        return

    price = resolve_price(name)

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

    print(f"Kopā: {grand_total:.2f} EUR ({units} vienības, {len(items)} produkti)")


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
            print("Lietošana: python shop.py add Produkts Daudzums")
            return

        name = sys.argv[2]
        qty = sys.argv[3]

        add_item(name, qty)

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