n=int(input('enter a  number.'))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n//=10
print("your value is:",r)