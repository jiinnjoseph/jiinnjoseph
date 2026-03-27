import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'
)

mycursor= mydb.cursor()
#  show database

mycursor.execute('show databases')
for db in mycursor:
    print(db)

mydb.close()