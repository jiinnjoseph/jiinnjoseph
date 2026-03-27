n=int(input('enter the number '))
r=0
temp=n
while n!=0:
    d=n%10
    r=r*10+d
    n//=10
if r==temp:
    print('palindrome')
else:
    print('not palindrome')