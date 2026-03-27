# contact list


input('Hey user! welcome to Phonebook\nno contacts found\nadd atleat one contact to access the menu\npresss enter to proceed' )
n=int(input('How many contacts do you like to add??' ))

contact={}
for i in range(n):
     print(f'\nEnter the person details {i+1}') 
     name=input('enter the name ').capitalize()
     primarynumber=input('enter the primary number ')
     secondarynumber=input('enter the secondary number ')
     mailid=input('enter the mail id ')
     address=input('enter the address ')
     call_count=0

     contact[name]={'name':name,'primary number':[primarynumber],'secondary number':[secondarynumber] ,'mail id':mailid,'address':address,'call_count':call_count}
print(contact)
while True:
 value=int(input('press 1 for search a contact\npress 2 for Display all contacts\npress  3 for edit a contact \npress 4 for delete a contact\nPlease choose your option' ))
 if value==1:
   search=input('Enter the name of the contact \nname must be capitalized!! ')
   if search in contact:
    contact[search]['call_count']+=1
    print('The details of your contact:',contact[search])
   else:
    print('not found any contact!!!')
 elif value==2:
     new=dict(sorted(contact.items()))
     print('All contacts sorted alphabetically is :',new)
 elif value==3:
   search=input('Enter the name of the contact \nname must be capitalized!! ')
   if search in contact:
    contact[search]['call_count']+=1
    print('The details of your contact:',contact[search])
    edit=int(input('to add a phone number press 1\nto remove primary number press 2 \nchoose your option' ))
   if edit==1:
    number_add=input('enter the contact number')
    new_number=list[number_add]
    contact[search]['additional phone number']=number_add
    print(contact[search])
   elif edit==2:
      new1=contact[search]
      number_remove=new1.pop('primary number ')
      print('new contact list is :',contact[search])
   else:
      print('incorrect one.check your options!! ')
 elif value==4:
   search=input('Enter the name of the contact \nname must be capitalized!! ')
   if search in contact:
    contact[search]['call_count']+=1
    delete=int(input('if you want to delete the contact,press 1 '))
    if delete==1:
       del contact[search]
       print(contact)
    else:
        print('incorrect input!!!')
 else:
   print('Input value is incorrect,Check properly and try again!!! ')
   