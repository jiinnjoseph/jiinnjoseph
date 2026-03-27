# def fact(n):
#     if n<=1:
#         return n
#     else:
#         return n*fact(n-1)
# f=fact(5)
# print(f)




def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n=int(input('Enter a number limit : '))

for i in range(n):
    print(fib(i), end=' ')




n=int(input('Enter the limit :'))
f=0
s=1

for i in range(n):
    print(f,end=' ')
    f,s=s,f+s
