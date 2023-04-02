# import required libraries
import mysql.connector

# Connect to the MySQL container
cnx = mysql.connector.connect(user='root', password='ready2go',
                              host='127.0.0.1', port='3306')

# Create a cursor to execute SQL statements
cursor = cnx.cursor()

# Define the CREATE TABLE statement
create_table = """
CREATE TABLE test (
    id INT(11) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT(11),
    PRIMARY KEY (id)
)
"""

# Execute the SHOW DATABASES statement
#cursor.execute("SHOW DATABASES")
cursor.execute(create_table)

# Commit the changes
cnx.commit()

# Fetch all the results
# results = cursor.fetchall()

# Print the database names
# for db in results:
#     print(db[0])

# Close the cursor and connection
cursor.close()
cnx.close()