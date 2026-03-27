class Father:
    def __init__(self,father_name,father_occupation):
        self.fn=father_name
        self.fo=father_occupation
        

class Mother:
    def __init__(self,mother_name,mother_occupation):
        self.mn=mother_name
        self.mo=mother_occupation

class Child(Father,Mother):
    def __init__(self,father_name,father_occupation,mother_name,mother_occupation):
        Father. __init__(self,father_name,father_occupation)
        Mother. __init__(self,mother_name,mother_occupation)

    def display(self):
        print('====== Family Details ==========')
        print('Father name  :',self.fn)
        print('Father Occupation  :',self.fo)
        print('Mother name   :',self.mn)
        print('Mother Occupation  :',self.mo)


father_name=input('Enter the Father name  ')
father_occupation=input('Enter the father Occupation  ')
mother_name=input('Enter the Mother name   ')
mother_occupation=input('Enter the mother Occupation  ')


c=Child(father_name,father_occupation,mother_name,mother_occupation)
c.display()





        