n=int(input('enter a number '))
i=0
sum=0
while n!=0:
    d=n%10
    n//=10
    sum+=d
print(sum)