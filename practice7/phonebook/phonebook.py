import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="raikhan26"
)
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS phonebook;
CREATE TABLE phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL UNIQUE
);
""")
conn.commit()
print("Table created")

def insert_from_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data added")

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added")

def update_contact():
    name = input("Enter name to update: ")
    print("1. Update name\n2. Update phone")
    choice = input("Choice: ")
    if choice == "1":
        new_name = input("New name: ")
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, name))
    elif choice == "2":
        new_phone = input("New phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Contact updated")

def search_contacts():
    print("1. View all\n2. Search by name\n3. Search by phone prefix")
    choice = input("Choice: ")
    if choice == "1":
        cur.execute("SELECT * FROM phonebook")
    elif choice == "2":
        name = input("Name: ")
        cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (f"%{name}%",))
    elif choice == "3":
        prefix = input("Prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"{prefix}%",))
    else:
        return
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

def delete_contact():
    print("1. Delete by name\n2. Delete by phone")
    choice = input("Choice: ")
    if choice == "1":
        name = input("Name: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    print("Contact deleted")

while True:
    print("\n1. Load CSV\n2. Add contact\n3. Update\n4. Search\n5. Delete\n6. Exit")
    choice = input("Choice: ")
    if choice == "1":
        insert_from_csv()
    elif choice == "2":
        insert_from_console()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        search_contacts()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break

cur.close()
conn.close()
print("Goodbye!")