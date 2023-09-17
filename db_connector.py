import mysql.connector

def connect_to_db():
    # Create a MySQL connection
    connection = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
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
