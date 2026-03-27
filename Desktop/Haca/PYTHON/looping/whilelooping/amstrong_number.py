n=int(input('enter the number '))
l=len(str(n))
temp=n
s=0
while n!=0:
    d=n%10
    s+=d**l
    n//=10
if s==temp:
    print('amstong number ')
else:
    print('not amstrong!!')




