import json
import getpass
import psycopg


with open("db_config.json", "r", encoding="utf-8") as f:
    config = json.load(f)


username = input("Логин PostgreSQL: ").strip()
password = getpass.getpass("Пароль PostgreSQL: ")


with psycopg.connect(
    host=config["host"],
    port=config["port"],
    dbname=config["dbname"],
    user=username,
    password=password
) as conn:

    with conn.cursor() as cur:
        cur.execute("SELECT VERSION();")
        version = cur.fetchone()[0]


print("Версия PostgreSQL:")
print(version)