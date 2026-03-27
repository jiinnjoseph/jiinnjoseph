n=int(input('enter a number '))
for i in range(0,n+1):
    for j in range(n,i,-1):
        print(j,end=" ")
    print()