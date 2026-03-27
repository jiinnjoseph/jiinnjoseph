class Student:
    def __init__(self,name,mark):
        self.n=name
        self.m=mark

class Sports:
    def __init__(self,sportsscore):
        self.s=sportsscore

class Result(Sports):
    def __init__(self, name, mark,sportsscore):
      Student. __init__(self,name,mark)
      Sports. __init__(self,sportsscore)

      
    def display(self):
          print('======= Student Details ========')
          print( 'name :',self.n)
          print('mark :',self.m)
          print(' Sports Score :',self.s)
          print(' your Total mark :',self.m+self.s)


name=input('Enter your name :')
mark=int(input('Enter Your mark :'))
sportsscore=int(input('Enter the sports score :'))

r=Result(name,mark,sportsscore)
r.display()