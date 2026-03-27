n=int(input('enter the number series '))
oc=0
ec=0
while n!=0:
    d=n%10
    if d%2==0:
       ec+=1
    else:
      oc+=1
    n//=10
print('cound of odd numbers ',oc)   
print('cound of even numbers ',ec)