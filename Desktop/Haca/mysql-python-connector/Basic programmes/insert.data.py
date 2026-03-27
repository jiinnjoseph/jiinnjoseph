import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)
#  insert data 

conn=mydb.cursor()

# cmd='insert into contacts(id,name,address,phone_number)values (%s,%s,%s,%s) '
# val=[
#     (2,'Anju','Kochi',9998887776),
#     (3,'Rahul','Calicut',8887776665),
#     (4,'Neha','Trivandrum',7776665554)
# ]
# conn.executemany(cmd,val)
# mydb.commit()

