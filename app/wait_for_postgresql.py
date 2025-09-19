# app/wait_for_postgres.py
import time
import psycopg2

while True:
    try:
        conn = psycopg2.connect(
            dbname="products_db",
            user="admin",
            password="adminpass",
            host="postgres",
            port="5432"
        )
        conn.close()
        print("PostgreSQL is ready.")
        break
    except psycopg2.OperationalError:
        print("Waiting for PostgreSQL to be ready...")
        time.sleep(2)
