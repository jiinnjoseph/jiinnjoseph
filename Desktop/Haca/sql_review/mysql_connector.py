import mysql.connector

db=mysql.connector.connect(
    host='Localhost',
    user='root',
    password='jinn',
    database='review',
    auth_plugin= 'mysql_native_password'

)
conn=db.cursor()

cmd='select * from student_data'
conn.executemany(cmd)
row=conn.fetchall()

for i in row:
    print(i)

db.close()