n=int(input('enter a number '))
sum=0
temp=n
while n>0:
    d=n%10
    
    f=1
    i=1
    while i<=d:
        f*=i
        i+=1
    sum+=f
    n//=10
if sum==temp:
     print('strong ')
else:
     print('NOT')