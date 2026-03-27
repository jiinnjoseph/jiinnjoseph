n=int(input('enter the number  '))
i=2
while i<=n:
    if n%i==0:
        break
    i+=1
if i==n:
    print('prime!! ')
else:
    print('not prime')
