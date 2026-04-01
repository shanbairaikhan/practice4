import psycopg2
from config import load_config

def update_vendor(vendor_id, vendor_name):
    sql = "UPDATE vendors SET vendor_name = %s WHERE vendor_id = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (vendor_name, vendor_id))
                conn.commit()
                print(f"✅ Обновлено {cur.rowcount} строк")
    except Exception as error:
        print(f"❌ Ошибка: {error}")

if __name__ == '__main__':
    update_vendor(1, "3M Corporation")