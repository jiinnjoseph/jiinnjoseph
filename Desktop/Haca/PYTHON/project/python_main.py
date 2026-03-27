import numpy as ny
import pandas as pd
import matplotlib.pyplot as pyt


class Frame:

    def __init__(self):
        self.xfont = {'family': 'sans-serif', 'size': 13,'color':'red','weight':'bold'}
        self.yfont = {'family': 'serif', 'size': 13,'color':'red','weight':'bold'}
        self.Titlefont={'family': 'serif', 'size': 18,'color':'blue','weight':'bold'}
        self.colours= ['#4E79A7','#59A14F','#F28E2B','#E15759','#B07AA1']

    def read(self):
          read_data=pd.read_csv('Ev.csv')
          return read_data
    
    def group(self,read_data):
        group=read_data.groupby('city_zone')['vehicles_charged'].count()

        array1=ny.array(group.index)
        array2=ny.array(group.values)
        return array1,array2


    def show_bar(self,array1,array2):

     pyt.figure(figsize=(8,5))
     pyt.xlabel('Zones of EV Charging Stations ',fontdict=self.xfont)
     pyt.ylabel('Number of Vehicles ',fontdict=self.yfont)
     pyt.title('Average Usage Stats of EV Stations ',fontdict=self.Titlefont)  
     pyt.bar(array1,array2,color=self.colours)
     pyt.show()

    def show_plot(self,array1,array2):
        pyt.xlabel('Zones of EV Charging Stations ',fontdict=self.xfont)
        pyt.ylabel('Number of Vehicles ',fontdict=self.yfont)  
        pyt.title('Average Usage Stats of EV Stations ',fontdict=self.Titlefont)         
        pyt.plot(array1,array2,color='red')
        pyt.scatter(array1,array2)
        pyt.show()

f=Frame()
data=f.read()
array1,array2=f.group(data)

f.show_bar(array1,array2)
f.show_plot(array1,array2)