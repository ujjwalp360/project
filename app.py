import streamlit as st
from db_connector import connect_to_db, execute_query, fetch_data

# Connect to the database
connection = connect_to_db()

# Streamlit app code
st.title('MySQL Database Web App')

# Example query
query = "SELECT * FROM stock;"
cursor = execute_query(connection, query)
data = fetch_data(cursor)

st.write("Data from MySQL:")
st.write(data)

# Close the database connection
connection.close()
