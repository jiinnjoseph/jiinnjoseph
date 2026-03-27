n=int(input('enter a number '))
sum=0
for i in range(len(str(n))):
        d=n%10
        sum+=d
print(sum)