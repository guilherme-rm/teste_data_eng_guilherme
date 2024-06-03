import os
import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': 'localhost',
    'port': '5432'
}

db = 'fonte'
try:
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(sql.SQL(f"CREATE DATABASE {db};"))

except Exception as err:
    print(f'ERROR : {err}')

finally:
    cursor.close()
    conn.close()
