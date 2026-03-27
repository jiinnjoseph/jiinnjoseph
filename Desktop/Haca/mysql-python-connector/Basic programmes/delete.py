import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)
conn=mydb.cursor()

cmd=' delete from contacts where id =%s'
val=(2,)
conn.execute(cmd,val)

mydb.commit()
mydb.close()