# Testing connection
import mysql.connector

# Creating connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123#",
    database="mydatabase"
)

# Creating database
mycursor = mydb.cursor()

#   Database created
# mycursor.execute("CREATE DATABASE mydatabase")

#   Show all database
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

#   Creating tables inside the database
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#   Checking if table exist
mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)