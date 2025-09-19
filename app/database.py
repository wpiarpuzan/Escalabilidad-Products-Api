from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import time
import psycopg2
import os

#Se cambia esta configuracion por la de postgresql
#engine = create_engine(
#    "sqlite:///db/products.db",
#    connect_args={"check_same_thread": False},
#    pool_size=50,
#    max_overflow=0
#)

# Esperar a que PostgreSQL esté listo
def wait_for_postgres():
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
            print("Waiting for PostgreSQL...")
            time.sleep(2)

wait_for_postgres()

engine = create_engine(
    "postgresql://admin:adminpass@postgres:5432/products_db",
    pool_size=50,
    max_overflow=0
)

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()

def init_db():
    if os.getenv("INIT_DB") == "true":
        Base.metadata.create_all(bind=engine, checkfirst=True)
