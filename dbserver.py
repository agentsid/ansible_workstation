Here's an example Python script that uses the mysql-connector-python library to create a table in a MySQL container:

python
Copy code
import mysql.connector

# Connect to the MySQL container
cnx = mysql.connector.connect(user='root', password='ready2go',
                              host='172.20.0.5', port='3306',
                              database='test')

# Create a cursor to execute SQL statements
cursor = cnx.cursor()

# Define the SQL statement to create a table
create_table = """
    CREATE TABLE my_table (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        age INT,
        PRIMARY KEY (id)
    )
"""

# Execute the SQL statement to create the table
cursor.execute(create_table)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()