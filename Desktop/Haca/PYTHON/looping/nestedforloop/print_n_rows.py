n=int(input('enter the row limit '))
k=0
for i in range(1,n+1):
    print()
    for j in range(i):
        k+=1
        print(k,end=" ")
print()