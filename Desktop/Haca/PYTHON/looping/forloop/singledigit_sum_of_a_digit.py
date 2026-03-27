n=int(input('enter a number'))
sum=0
for i in range(len(str(n))):
               d=n%10
               sum+=d
               n//=10
SUM=0
for j in range(len(str(sum))):
             SUM+=sum%10
             sum//=10
print(SUM,'is the single unit of sum ')