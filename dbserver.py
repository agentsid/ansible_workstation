import pandas as pd
import mysql.connector

# Connect to the MySQL container
cnx = mysql.connector.connect(user='root', password='my_secret_password',
                              host='127.0.0.1', port='3306',
                              database='my_database')

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('cities.csv')

# Create a cursor to execute SQL statements
cursor = cnx.cursor()
show databases;
# Iterate over the rows in the DataFrame and execute an INSERT statement for each row
# for i, row in df.iterrows():
#     insert_row = f"INSERT INTO my_table (name, age) VALUES ('{row['name']}', {row['age']})"
#     cursor.execute(insert_row)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()






