import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn'
)

conn=mydb.cursor()
cmd='Create database Python'
conn.execute(cmd)

mydb.close()