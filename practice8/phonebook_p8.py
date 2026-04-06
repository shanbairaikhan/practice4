import psycopg2
import csv

conn = psycopg2.connect(
    host = "localhost",
    database = "suppliers",
    user = "postgres",
    password = "arai260807"
    )

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS phonebook;")
cur.execute(" CREATE TABLE phonebook (id SERIAL PRIMARY KEY,name VARCHAR(100),phone VARCHAR(100));")

conn.commit()

def insert_from_csv():
    with open("contacts.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", row)
    conn.commit()
    print("Added successfully from CSV file!")


def insert_from_console():
    name = input("Enter the name: ")
    phone = input("Enter the phone: ")

    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()


def update_con():
    name = input("Enter the name for updating data: ")
    print("What do you want to change?")
    print("1.Name")
    print("2.Phone")

    choice = input("Enter your choice: ")
    if choice == "1":
        new_name = input("Enter a new name: ")
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_name, name))
        
    elif choice == "2":
        new_phone = input("Enter a new phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
        
    else:
        print("Wrong choice!")
        return
    
    conn.commit()

def delete_contacts():
    name = input("Enter the name for deleting: ")
    print("How do you want to delete?")
    print("1. With name")
    print("2. With phone")

    choice = input("Enter your choice: ")
    if choice == "1":
        name1 = input("Enter the name: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name1,))
    elif choice == "2":
        phone = input("Enter the phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Wrong choice!")
    conn.commit()

def search_contacts():
    print("1.View all contacts.\n2.Search with name.\n3.Search with phone prefix.")

    choice = input("Enter your choice: ")
    if choice =="1":
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
    elif choice == "2":
        name = input("Please enter the name for search: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))

        rows = cur.fetchall()
    elif choice == "3":
        prefix = input("Please enter the prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix+"%",))

        rows = cur.fetchall()
    
    else:
        print("Wrong choice!")
        return
    
    if rows:
        for row in rows:
            print(f"ID:{row[0]}, Name: {row[1]}, Phone: {row[2]},")
    else:
        print("Nothing found.")
try:
    while True:
        print("\n1.Insert data from a CSV file. \n2.Insert data from a console. \n3.Updating a contact's first name or phone number. \n4.Querying contacts with different filters (e.g. by name, by phone prefix). \n5.Deleting a contact by username or phone number")

        choice = input("Enter your choice: ")
        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_con()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contacts()
        else:
            print("Wrong choice!")

        cur.execute("SELECT * FROM phonebook;")
        print(cur.fetchall())
finally:
    cur.close()
    conn.close()
    print("Connection closed.")