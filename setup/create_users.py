import psycopg2
from psycopg2 import sql

def create_user(dbname, user, password, new_user, new_password):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password)
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(sql.SQL(f"CREATE USER {new_user} WITH PASSWORD {new_password};"))

        cursor.execute(sql.SQL(f"GRANT CREATEDB TO {new_user};"))

    except psycopg2.Error as e:
        print(f"Erro ao criar usuário: {e}")

    finally:
        if conn:
            cursor.close()
            conn.close()

db_name = 'postgres'
user='postgres'
password='password'
new_user1 = 'user1'
new_password1 = 'password1'
new_user2 = 'user2'
new_password2 = 'password2'

create_user(db_name, user, password, new_user1, new_password1)
create_user(db_name, user, password, new_user2, new_password2)