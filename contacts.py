import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contact(name, phone):
    contacts = load_contacts()

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    save_contacts(contacts)

    print(f"✓ Pievienots: {name} ({phone})")

def list_contacts():
    contacts = load_contacts()

    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return

    print("Kontakti:")
    for i, c in enumerate(contacts, start=1):
        print(f"  {i}. {c['name']} — {c['phone']}")

def search_contacts(query):
    contacts = load_contacts()

    results = []
    for c in contacts:
        if query.lower() in c["name"].lower():
            results.append(c)

    print(f"Atrasti {len(results)} kontakti:")

    for i, c in enumerate(results, start=1):
        print(f"  {i}. {c['name']} — {c['phone']}")

def main():
    if len(sys.argv) < 2:
        print("Komandas: add, list, search")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print('Lietošana: python contacts.py add "Vārds Uzvārds" "+371 XXXXXXXX"')
            return
        name = sys.argv[2]
        phone = sys.argv[3]
        add_contact(name, phone)

    elif command == "list":
        list_contacts()

    elif command == "search":
        if len(sys.argv) != 3:
            print('Lietošana: python contacts.py search "vārds"')
            return
        query = sys.argv[2]
        search_contacts(query)

    else:
        print("Nezināma komanda. Izmanto: add, list, search")

if __name__ == "__main__":
    main()