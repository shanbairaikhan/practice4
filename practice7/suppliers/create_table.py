import psycopg2
from config import load_config

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ 
        CREATE TABLE IF NOT EXISTS parts (
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        """,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                conn.commit()
                print("✅ Таблицы созданы!")
    except Exception as error:
        print(f"❌ Ошибка: {error}")

if __name__ == '__main__':
    create_tables()