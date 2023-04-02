# import required libraries
import mysql.connector

# Connect to the MySQL container
cnx = mysql.connector.connect(user='root', password='ready2go',
                              host='127.0.0.1', port='3306')

# Create a cursor to execute SQL statements
cursor = cnx.cursor()

# Execute the SHOW DATABASES statement
cursor.execute("SHOW DATABASES")

# Fetch all the results
results = cursor.fetchall()

# Print the database names
for db in results:
    print(db[0])

# Close the cursor and connection
cursor.close()
cnx.close()