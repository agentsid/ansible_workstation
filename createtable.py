import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="readytogo",
    database="test"
)

# Create a cursor object
cursor = cnx.cursor()

# Define the table creation query
table_query = """
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50),
  age INT
)
"""

# Execute the query
cursor.execute(table_query)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()






