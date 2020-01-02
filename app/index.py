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
#
#   Database created
# mycursor.execute("CREATE DATABASE mydatabase")

#   Show all database
# mycursor.execute("SHOW DATABASES")
# for i in mycursor:
#     print(i)

#   Creating tables inside the database
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#   Checking if table exist
# mycursor.execute("SHOW TABLES")
# for i in mycursor:
#     print(i)

#   Altering table
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#   Inserting records
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Harsh", "Ahmedabad")
# mycursor.execute(sql,val)

#   commit is required to make changes otherwise no changes are made to the table
# mydb.commit()
# print(mycursor.rowcount, "record inserted")

#   Inserting multiple data
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('Urvish','Dakor'),
#     ('Stallone','Ahmedabad'),
#     ('Srushti','Baroda'),
#     ('Tithi','Vallabh Vidyanagar')
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"was inserted")

#   Selecting data from table
# mycursor.execute("SELECT name FROM customers")
# myresult = mycursor.fetchall() # mycursor.fectchone() to fetch single value
#
# for i in myresult:
#     print(i)

#   Where clause
# sql = "SELECT * FROM customers WHERE address LIKE '%a%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall() # mycursor.fectchone() to fetch single value
#
# for i in myresult:
#     print(i)

#   To prevent from SQL injection end the query using %s placeholder
# sql = "SELECT * FROM customers WHERE address = %s ORDER BY name DESC"
# adr = ("Ahmedabad", )
# mycursor.execute(sql,adr)
# myresult = mycursor.fetchall() # mycursor.fectchone() to fetch single value
#
# for i in myresult:
#     print(i)

#   Deleting the record
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Navsari", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

#   Delete the table
# sql = "DROP TABLE customers"
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)

#   Update Table
# sql = "UPDATE TABLE customers SET address = '' WHERE address = ''"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")
#
# sql = "INSERT INTO client (name, location) VALUES (%s, %s)"
# val = ('C1', 'L1')
# # sql = "SELECT * FROM client"
# mycursor.execute(sql,val)
# mydb.commit()
# print("Record added ",mycursor.rowcount)
#
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

#   Join Operations
# sql = "SELECT users.name AS users, products.name AS favorite FROM users INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
#
# result = mycursor.fetchall()
#
# for i in result:
#     print(i)