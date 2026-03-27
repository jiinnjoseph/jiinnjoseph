n=int(input('enter the number '))
i=2
while i<n:
   if n%i==0:
      break
   i+=1
if n==i and n>1:
   print('prime number')
else:
    print('not prime!!')