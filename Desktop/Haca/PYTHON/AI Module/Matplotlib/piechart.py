import numpy as ny
import pandas as ps
import matplotlib.pyplot as plt


def student_book():
    m1=int(input('Enter the mark of first student:'))
    m2=int(input('Enter the second student mark:'))
    m3=int(input('Enter the third student mark:'))
    
    b=ny.array([m1,m2,m3])
    d=ps.DataFrame(b,columns=['Marks'])
    labells=['student 1','student 2','student 3']
    plt.pie(b,labels=labells)
    plt.show()

student_book()
