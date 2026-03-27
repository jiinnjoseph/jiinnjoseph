
class User:

   def __init__(self,username,password):
        self.username=None
        self.password=None
      
   def register(self):
        print('======= REGISTRATION ========')
        self.username=username
        self.password=password
        print('Registration Successfull !!!')

   def login(self):
        print('========== LOGIN ==========')
        login_name=input('Enter the User name :')
        login_pass=int(input('Enter the password :'))
        if login_name==self.username and login_pass==self.password:
            print('Login Successfull !!!!')
            return True
        else:
            print('Incorrect Username or Password !!!')
            return False

class Product:   

   def __init__(self,name,price):
       self.name=name
       self.price=price


class Cart:

   def __init__(self):
      self.items=[]

   def add_to_cart(self,product):
     self.items.append(product)
     print(f'{product.name} added to cart Succesfully !!!!')

   def view_cart(self):
       if len(self.items)==0:
          print('Your  cart is Empty !!!!')
       else:
          total=0
          for item in self.items:
             print('===== Available Products ======= ')
             print(f'{item.name}\t {item.price}')
             total+= item.price
             print('Total Amount is :',item.price)


class EcommerceSystem():
   def __init__(self):
       self.u=User(username,password)
       self.c=Cart()

       self.products=[
              Product('Laptop',50000),
              Product('Phone',20000),
              Product('Headphones',2000)  
             ]
       

   def view_products(self):
      print('====== Available Products ======= ')
      i=1
      for item in self.products:
         print(f'{i}.{item.name} - {item.price}')
         i+=1
   
   def add_product(self):
       self.view_products()   
       product_number=int(input('Select Product Number '))
       product_number-=1
       product=self.products[product_number]
       self.c.add_to_cart(product)
   
   def start(self):
       self.u.register()
       if self.u.login():
         self.menu()

   def menu(self):
       while True:
         print('\n\n====== Your Options ====== ')
         print('1.View Products\n2. Add Products\n3. View Cart\n4. Exit')
         choice=int(input('Enter Your Choice '))
         if choice==1:
          self.view_products()
         elif choice==2:
          self.add_product()
         elif choice==3:
          self.c.view_cart()
         elif choice==4:
          print('Thank you for shopping !!!')
         else:
          print('Invalid Choice ')


username=input('Create  the Username :')
password=int(input('Create  the password :'))
u=User(username,password)
e=EcommerceSystem()
e.start()