import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root123#",
    database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT users.name AS users, products.name AS favorite FROM users INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)

result = mycursor.fetchall()

for i in result:
    print(i)