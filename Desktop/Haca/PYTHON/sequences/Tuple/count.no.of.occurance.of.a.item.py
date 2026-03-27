a=(50,'cherry',50,'apple',4,7,20,50)
a=list(a)
count=0
for i in a:
    if i==50:
        count+=1
print('the number of occurance of the item is ',count)