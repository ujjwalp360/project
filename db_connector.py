import mysql.connector

def connect_to_db():
    # Create a MySQL connection
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="ujjwal",
        database="stock"
    )
    return connection

def execute_query(connection, query, data=None):
    # Execute a MySQL query
    cursor = connection.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    connection.commit()
    return cursor

def fetch_data(cursor):
    # Fetch data from a cursor
    return cursor.fetchall()
