import psycopg2
from psycopg2 import sql
import vars
db_params = {
    'dbname': 'postgres',
    'user': vars.user,
    'password': vars.password,
    'host': vars.host,
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
