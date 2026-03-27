import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='jinn',
    database='Python'
)
conn=mydb.cursor()

table='''create table contacts(
id int  ,
name varchar (100),
address varchar(100),
phone_number BIGINT)'''

conn.execute(table)

mydb.close()

