class Vehicle:
    def __init__(self,brand):
        self.b=brand

class Car(Vehicle):
    def __init__(self, brand,speed):
        super().__init__(brand)
        self.s=speed

class ElectricCar(Car):
    def __init__(self,brand,speed,batterycapacity):
        super().__init__(brand,speed)
        self.bt=batterycapacity
    def display(self):
        print('Brand :',self.b)
        print('Speed  :',self.s)
        print('Batter capacity :',self.bt)
       
brand=input('Enter the brand :')
speed=input('ENter the speed :')
batterycapacity=input('Enter the batter capacity :')


    
e=ElectricCar(brand,speed,batterycapacity)
e.display()
