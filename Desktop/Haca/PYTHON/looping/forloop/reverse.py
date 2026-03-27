n=int(input('enter a number'))
r=0
for i in range(len(str(n))):
    d=n%10
    r=r*10+d
    n//=10
print("the reverse of the the entered number is ",r)