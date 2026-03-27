import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)
conn=mydb.cursor()

# cmd='update contacts set Address= %s where id =%s'
# val=('Ernakulam',2,)
# conn.execute(cmd,val)

# mydb.commit()
# mydb.close()

cmd1='Alter table contacts modify column id int'
conn.execute(cmd1)