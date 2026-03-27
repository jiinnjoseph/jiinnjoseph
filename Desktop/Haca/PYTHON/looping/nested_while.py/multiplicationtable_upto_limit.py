n=int(input('enter the limit '))
i=1
while i<=n:
    j=1
    while j<=10:
        m=j*i
        print(f'{j}*{i}={m}')
        j+=1
    print()
    i+=1