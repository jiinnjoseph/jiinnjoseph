from tabulate import tabulate
import mysql.connector


print('Hey User!!! Welcome to FitClub  online fitness app ')
print('Before Start ,You want to Register or  Login ')

username=None
passcode=None

username=input('Create Username :')
passcode=input('Create Password :')
print('Registration Succesfull!!')

login_username=input('Enter the Username :')
login_pass=input('Enter the password :')

if username==login_username and passcode==login_pass:
  print('Login Succesfull !!!')
else:
  print('Invalid Username or password ')
  exit()


db=mysql.connector.connect(
    host="Localhost",
    user="root",
    password="jinn",
    database='Project'
)
conn=db.cursor()

tab1='''create table if not exists services(
    ID    int auto_increment primary key,
    service varchar(100),
    category varchar(100),
    duration varchar(100),
    price_per_month int, 
    Trainer_name varchar(50))'''

conn.execute(tab1)

tab2='''create table if not exists members(
    MemberID int auto_increment primary key,
    Name varchar(100),
    Age int,
    Address  varchar(100),
    Email_ID varchar(50),
    service varchar(100),
    duration varchar(100),
    trainer_name varchar(100))'''

conn.execute(tab2)

cmd1='insert  ignore into services(service,category,duration,price_per_month,Trainer_name) values (%s,%s,%s,%s,%s)'

val1=[
  ('Yoga ','Personal Training','1 Month',3000,'Arjun'),
  ('Weight Loss','Diet','3 Months',2000,'Arun'),
  ('Personal Trainer','Workout','6 Months',2500,'Sagar'),
  ('Basic Workout+Cardio','Workout','8 Months',2000,'Sahal'),
  ('Basic Workout(Without Cardio)','Workout','8 Months',1500,'Sam')]

conn.executemany(cmd1,val1)
db.commit()


print("\n====== Welcome to FitClub =======")
print("\nLet's Re-Build Together!!!")

while True:

 print("\n\nHere's our  services  :")
 print("\n 1. Create a Membership    ")
 print("2. View  our Services   ")
 print("3. View  Membership Details ")
 print("4. Change your Membership ")
 print("5. Cancel  Membership  ")
 print('6. Exit App ')
 ch=int(input('Please choose your need :'))

 if ch==1:
    print('\n\nwelcome to FitClub Fitness app ')
    name=input('\nEnter your name  :')
    age=int(input('Enter your age  :'))
    address=input('Enter your address :')
    Email=input('Enter your email id :')

    print("\nHere's our Services for you  :")
    conn.execute('select * from services ')
    rows=conn.fetchall()
    columns=[i[0] for i in conn.description]
    print(tabulate(rows,headers=columns,tablefmt="grid"))

    user_item=int(input('Enter the Preferred category ID : '))
    cmd=('select service,duration,Trainer_name from services where ID=%s ')
    conn.execute(cmd,(user_item,))
    menu=conn.fetchone()
    db.commit()

    if menu:
     service,duration,Trainer_name=menu
     ser_cmd='insert ignore into members (Name,age,Address,Email_ID,service,duration,Trainer_name) values (%s,%s,%s,%s,%s,%s,%s)'
     ser_val=(name,age,address,Email,service,duration,Trainer_name)
     conn.execute(ser_cmd,ser_val)    
     db.commit()
     print('Your Membership Succesfully created !!!')
    else:
     print('Invalid ID number, Check your Input !!!')

 elif ch==2:
   
   print("Here's our Membership Details : ")
   print("\nHere's our Services for you  :")
   conn.execute('select * from services ')
   rows=conn.fetchall()
   columns=[i[0] for i in conn.description]
   print(tabulate(rows,headers=columns,tablefmt="grid"))

 elif ch==3:
   
   search=input('Enter your Membership ID :')
   print("\nHere's your Membership Details :")
   cmd1=('select * from members where MemberID=%s')
   conn.execute(cmd1,(search,))
   rows=conn.fetchall()
   columns=[i[0] for i in conn.description]
   print(tabulate(rows,headers=columns,tablefmt="grid"))

 elif ch==4:
   search=int(input('enter your Membership ID '))
   print("\nHere's your Membership Details :")
   cmd1=('select * from members where MemberID=%s')
   conn.execute(cmd1,(search,))
   rows=conn.fetchall()
   columns=[i[0] for i in conn.description]
   print(tabulate(rows,headers=columns,tablefmt="grid"))

   print('\nIf you want to Change this Membership Plan press 1 or exit press 2')
   edit=int(input('\nEnter your choice :'))
   if edit==1:
     print("\nHere's our membership plans :")
     print("\nHere's our Services for you  :")
     conn.execute('select * from services ')
     rows=conn.fetchall()
     columns=[i[0] for i in conn.description]
     print(tabulate(rows,headers=columns,tablefmt="grid"))

     edit_id=int(input('Enter the memberID you are looking for :'))
     cmd2=('select service,duration,Trainer_name from services where ID=%s')
     val2=(edit_id,)
     conn.execute(cmd2,(edit_id,))
     edit=conn.fetchone()
     if edit:
       service,duration,Trainer_name=edit
       edit_cmd=('update  members set service=%s,duration=%s,Trainer_name=%s where MemberID=%s')
       edit_val=(service,duration,Trainer_name,search)
       conn.execute(edit_cmd,edit_val)
       db.commit()
       print('\nYour Membership Plan changed Succesfully!!')
     else:
       print('Change action Failed !!!')
   elif edit==2:
     print('Return to Main menu ')
     
 elif ch==5:
      print('\nAre You Sure Want to Cancel the Membership ??')
      print("\nNB:ONCE YOU CANCEL THIS,IT CAN'T UNDO")

      delete=int(input('if you really wat to cancel this membership press 1 or exit press 2'))
      if delete==1:
       search=int(input('enter your Membership ID :'))
       delete_cmd='delete from members where MemberID =%s'
       delete_val=(search,)
       conn.execute(delete_cmd,delete_val)
       db.commit()
       print('your Membership Deleted Succesfully!!!')
      elif delete==2:
        print('Deletion action Cancelled ')

 elif ch==6:
       print('Thank you for choosing FitClub Fitness app !!! Take care ')
       break
 else:
   print('Invalid Input!! Check your Options carefully !!!')
   
db.close()