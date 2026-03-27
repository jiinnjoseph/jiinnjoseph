class Salary:


    def __init__(self,name,empcode,basic):

        self.n=name
        self.e=empcode
        self.b=basic



    def salary_slip(self):
        da=self.b* 0.10
        hra=da+ (0.5*da)
        pf=hra* 0.05
        total=self.b+hra+da-pf

        print('Name :',self.n)
        print('Empcode  :'  ,self.e)
        print('Basic salary  :',self.b)
        print('DA  :',da)
        print('hra  :',hra)
        print('pf    :',pf)
        print('Total salary      :',total)


name1=input('Enter the first employee name :')
empcode1=input('Enter the first employee code :')
basic1=int(input('enter the second employee basic salary :'))
name2=input('Enter the second employee name  :')
empcode2=input('Enter the second employee code :')
basic2=int(input('enter the second employee basic salary :'))
    
s1=Salary(name1,empcode1,basic1)
s2=Salary(name2,empcode2,basic2)

s1.salary_slip()

s2.salary_slip()
