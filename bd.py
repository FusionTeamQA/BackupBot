import psycopg2

from config_db import host, user, password, db_name

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name)

    with connection.cursor() as cursor:
        cursor.execute()
        "SELECT version();"
        print(f"Server version: {cursor.fetchone()}")



except Exception as _ex:
    print("Error connect", _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("asd")
