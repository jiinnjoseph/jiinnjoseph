import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)

conn=mydb.cursor()


cmd='Select * from contacts where id =%s'
val=(3,)
conn.execute(cmd,val)

for i in conn.fetchall():
    print(i)

