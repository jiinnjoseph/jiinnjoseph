import numpy as ny
import pandas as pd
import matplotlib.pyplot as pyt


class Frame:

    def __init__(self):

        self.xfont = {'family':'serif','size':13,'color':'red','weight':'bold','style':'italic'}
        self.yfont = {'family':'serif','size':13,'color':'blue','weight':'bold','style':'italic'}
        self.titlefont = {'family':'serif','size': 18,'color':'green','weight':'bold','style':'italic'}
        self.colours = ['#4E79A7','#59A14F','#F28E2B','#E15759','#B07AA1']

    def read(self):
        data = pd.read_csv('Ev.csv')
        return data

    def group(self,data):
        group = data.groupby('city_zone')['vehicles_charged'].count()

        array1 = ny.array(group.index)
        array2 = ny.array(group.values)

        return array1,array2


    def show_bar(self,array1,array2):

        pyt.figure(figsize=(10,6))

        bars = pyt.bar(array1,array2,
                       color=self.colours,
                       edgecolor='black',
                       linewidth=1.2)

        pyt.xlabel('Zones of EV Charging Stations',fontdict=self.xfont)
        pyt.ylabel('Number of Vehicles Charged',fontdict=self.yfont)
        pyt.title('EV Charging Station Usage by Zone',fontdict=self.titlefont)

        pyt.grid(axis='y', linestyle='--', alpha=0.6)

        for bar in bars:
            height = bar.get_height()
            pyt.text(bar.get_x() + bar.get_width()/2,
                     height + 1,
                     int(height),
                     ha='center',
                     fontsize=11,
                     fontweight='bold',
                     color='brown')

        pyt.tight_layout()
        pyt.show()


    def show_plot(self,array1,array2,):

        pyt.figure(figsize=(10,6))

        pyt.plot(array1,array2,
                 marker='o',
                 linestyle='-',
                 linewidth=3,
                 markersize=8,
                 color='red')

        pyt.scatter(array1,array2, s=100,color='blue',edgecolor='yellow')

        pyt.xlabel('Zones of EV Charging Stations',fontdict=self.xfont)
        pyt.ylabel('Number of Vehicles Charged',fontdict=self.yfont)
        pyt.title('EV Charging Station Usage Trend by Zone',fontdict=self.titlefont)

        pyt.grid(True, linestyle='--', alpha=0.6,color='blue')

        pyt.tight_layout()
        pyt.show()

f = Frame()

data = f.read()

array1,array2 = f.group(data)

f.show_bar(array1,array2)
f.show_plot(array1,array2)