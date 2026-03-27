class Person:
    def __init__ (self,name,age):
        self.n=name
        self.a=age

class Student(Person):
    def __init__ (self,name,age,mark):
        super(). __init__(name,age)
        self.m=mark
    def display(self):
        print('========== Mark Details ==========')
        print('Student name :',self.n)
        print('Age :',self.a)
        print('Mark is :',self.m)


name=input('Enter the name :')
age=int(input('Enter the age :'))
mark=int(input('Enter the mark :'))


s=Student(name,age,mark)

s.display()


