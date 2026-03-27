import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',

)

conn=mydb.cursor()

cmd="USE `Python`"
conn.execute(cmd)
mydb.close()


# OR directly add database name into the connect part.


import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'
)

conn=mydb.cursor()
mydb.close()

