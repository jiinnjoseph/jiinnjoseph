import numpy as ny
import pandas as pd
import matplotlib.pyplot as pyt

read=pd.read_csv('Ev.csv')

group=read.groupby('city_zone')['vehicles_charged'].mean()

array1=ny.array(group.index)
array2=ny.array(group.values)

pyt.figure(figsize=(8,5))

xfont = {'family': 'sans-serif', 'size': 13,'color':'red','weight':'bold'}
yfont = {'family': 'serif', 'size': 13,'color':'red','weight':'bold'}
Titlefont={'family': 'serif', 'size': 18,'color':'violet','weight':'bold'}
pyt.xlabel('Zone of EV Charging Station ',fontdict=xfont)
pyt.ylabel('Number of Vehicles',fontdict=yfont)
pyt.title('Average Usage stats for EV stations ',fontdict=Titlefont)
colours = ['#4E79A7','#59A14F','#F28E2B','#E15759','#B07AA1']

# pyt.bar(array1,array2, color=colours)
pyt.plot(array1,array2,color='skyBlue')
pyt.scatter(array1,array2)
# pyt.grid()
pyt.tight_layout()
# pyt.subplot()
pyt.show()