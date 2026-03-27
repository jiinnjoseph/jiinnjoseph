# #  AND condition.

# import mysql.connector

# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='jinn',
#     database='Python'

# )

# conn=mydb.cursor()


# cmd='Select * from contacts where id =%s and name=%s'
# val=(3,'Rahul',)
# conn.execute(cmd,val)

# for i in conn.fetchall():
#     print(i)

# #   OR condition >


import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'

)

conn=mydb.cursor()


cmd='Select * from contacts where id =%s or name=%s'
val=(3,'neha',)
conn.execute(cmd,val)

for i in conn.fetchall():
    print(i)


# # #  NOT condition >

# import mysql.connector

# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='jinn',
#     database='Python'

# )

# conn=mydb.cursor()


# cmd='Select * from contacts where not id =%s and  name=%s'
# val=(2,'Rahul',)
# conn.execute(cmd,val)

# for i in conn.fetchall():
#     print(i)


