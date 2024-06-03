import psycopg2
from datetime import datetime, timedelta
import numpy as np


def gen_data(start_date=datetime(2024, 1, 1, 0, 0, 0), days=10, min_interval=1):
    data = []
    total = int(24*days*60/min_interval)

    for _ in range(total):
        time = start_date
        wind = round(np.random.uniform(0, 25), 2)
        power = round(np.random.uniform(0, 5), 2)
        temperature = round(np.random.uniform(15, 25), 2)
        data.append((time, wind, power, temperature))
        start_date += timedelta(minutes=min_interval)

    return data


conn = psycopg2.connect(
    dbname="fonte",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        timestamp TIMESTAMP PRIMARY KEY,
        wind_speed REAL,
        power REAL,
        ambient_temperature REAL
    );
''')

data = gen_data()

cursor.executemany('''
    INSERT INTO data (timestamp, wind_speed, power, ambient_temperature)
    VALUES (%s, %s, %s, %s)
''', data)
    

conn.commit()
cursor.close()
conn.close()