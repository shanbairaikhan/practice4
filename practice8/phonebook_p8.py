import psycopg2
from config import load_config

def main():
    config = load_config()
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                print("=== Testing PostgreSQL Functions ===\n")
                
                print("1. Adding contacts...")
                cur.execute("CALL upsert_contact(%s, %s)", ('Arai', '87771234567'))
                cur.execute("CALL upsert_contact(%s, %s)", ('Arai2', '87771234568'))
                cur.execute("CALL upsert_contact(%s, %s)", ('Arai3', '87771234569'))
                cur.execute("CALL upsert_contact(%s, %s)", ('Arai4', '87771234560'))
                conn.commit()
                print("   Contacts added\n")
                
                print("2. Searching contacts with '8777':")
                cur.execute("SELECT * FROM search_contacts(%s)", ('8777',))
                for row in cur.fetchall():
                    print(f"   Name: {row[0]}, Phone: {row[1]}")
                
                print("\n3. Pagination (first 2 contacts):")
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (2, 0))
                for row in cur.fetchall():
                    print(f"   ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                
                print("\n4. Inserting multiple contacts:")
                cur.execute("CALL insert_many_contacts(%s, %s)", (['John', 'Jane'], ['123456', '654321']))
                conn.commit()
                print("   Contacts inserted\n")
                
                print("5. All contacts:")
                cur.execute("SELECT * FROM phonebook")
                for row in cur.fetchall():
                    print(f"   ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                
                print("\n6. Deleting contact 'Arai3':")
                cur.execute("CALL delete_contact(%s, %s)", ('Arai3', None))
                conn.commit()
                print("   Contact deleted\n")
                
                print("7. Final contacts:")
                cur.execute("SELECT * FROM phonebook")
                for row in cur.fetchall():
                    print(f"   ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()