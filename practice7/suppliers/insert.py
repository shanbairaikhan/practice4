import psycopg2
from config import load_config

def insert_vendor(vendor_name):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name,))
                vendor_id = cur.fetchone()[0]
                conn.commit()
                print(f"✅ Добавлен поставщик ID: {vendor_id} - {vendor_name}")
                return vendor_id
    except Exception as error:
        print(f"❌ Ошибка: {error}")

def insert_many_vendors(vendor_list):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, vendor_list)
                conn.commit()
                print(f"✅ Добавлено {len(vendor_list)} поставщиков")
    except Exception as error:
        print(f"❌ Ошибка: {error}")

if __name__ == '__main__':
    insert_vendor("3M Co.")
    
    vendors = [
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ]
    insert_many_vendors(vendors)