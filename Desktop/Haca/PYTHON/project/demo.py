cb= {}
while True:
    print('1. add ')
    print ('2. display ')
    print ('3. update ' )
    print ('4. Delete ')
    print ('5. Exit')
    ch=int(input('Enter your choice: '))
    if ch==1:
        name=input('enter your name' )
        phone=input( 'enter your mobile number' )
        cb[name]=phone
        print(cb)
    elif ch==2:
        for i in cb.keys() :
            print(f'{name}\t{phone}')
    elif ch==3:
        name=int(input('enter your name: '))
        if name in cb:
            new_phone=input('enter your phone number')
            cb[name]=new_phone
            print(cb)
        else:
            print('not exist')
        print(cb)
    elif ch==4:
        name_delete=input('enter the name of the contact' )
        if name_delete in cb:
            delete=int(input(f'if you want to delete {name_delete} in your contacts press 1\nexit press 2'))
            if delete==1:
             del cb[name_delete]
             print(cb)
            elif delete==2:
             break
            else:
             print('invalid input ')
    elif ch==5:
        print('exit')
        break
    else:
        print('invalid input')