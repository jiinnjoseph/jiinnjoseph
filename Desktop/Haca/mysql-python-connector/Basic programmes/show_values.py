import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)
conn=mydb.cursor()

cmd='Select * from contacts'
conn.execute(cmd)
rows=conn.fetchall()

for i in rows:
    print(i)

mydb.close()

