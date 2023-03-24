import pandas as pd
import pyodbc
import mysql.connector

# Import CSV
data = pandas.read_csv (r'~/docker_workstation/test.csv')   
df = pandas.DataFrame(data)

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('''
		CREATE TABLE Accenture (
            SN  int primary key,
            NAME nvarchar(50),
            Age int,
            city nvarchar(50),
			)
               ''')

# Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO products (product_id, product_name, price)
#                 VALUES (?,?,?)
#                 ''',
#                 row.product_id, 
#                 row.product_name,
#                 row.price
#                 )
conn.commit()