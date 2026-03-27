
pin=4567
pin_user=int(input('enter you PIN '))
if pin==pin_user:
     print('Login Successfull')
else:
     print('lnvalid pin')
     exit()


class ATM:
    def __init__(self):
        self.Balance=0


    def display(choice):
       print('========= Welcome To ATM ==============')
       print('1.Add amount')
       print('2.Withdraw amount')
       print('3.Balance Check')
       print('4.Exit')
     
    def add_amount(self):
         amt=int(input('Enter the amount :'))
         self.Balance+=amt
         print('Total amount Is : ',self.Balance)
    def  withdraw_amount(self):
        withdraw=int(input('Enter the withdraw amount :'))
        if withdraw<self.Balance:
          self.Balance-=withdraw
          print('Amount Withdrawed Successfull!! New Balance is ',self.Balance)
        else:
            print('insufficient Balance ')
    def balance_check(self):
        print('Balance is :',self.Balance)
    def exit_atm(self):
        print('Thank You ')
        exit()

atm=ATM()
while True:
 atm.display()
 choice=int(input('Enter your Choice :'))
       
 if choice==1:
    atm.add_amount()
 elif choice==2:
    atm.withdraw_amount()
 elif choice==3:
    atm.balance_check()
 elif choice==4:
    atm.exit_atm()
 else:
    print('Invalid Input , Try Again!!!')