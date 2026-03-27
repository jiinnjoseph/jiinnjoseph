class Person:
    def __init__(self,name):
        self.n=name
class Student:
    def __init__(self,mark):
        self.m=mark
        print('Mark is ; ',self.m)
class Result(Student):
    def __init__(self,name,mark):
        Person. __init__(self,name)
        Student. __init__(self,mark)
 
    def display(self):
        passing_mark=40
        if mark>=passing_mark: 
            print('You are pass !!')
        else:
            print('YOU ARE FAIL!!!')

name=input('Enter the name :')
mark=int(input('Enter the mark :'))


r=Result(name,mark)
r.display()
