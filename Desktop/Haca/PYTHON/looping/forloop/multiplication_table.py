# n=int(input('enter the  number'))
# for i in range(1,11):
#    if i!=0:
#         m=i*n
#         print(f'{i}*{n}={m}')

l=int(input('Enter the number limit :'))
for i in range(1,l+1):
    for j in range(1,11):
        m=i*j
        print(f'{i}*{j}={m}')
    print()