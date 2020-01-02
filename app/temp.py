import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123#",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)