from functools import reduce
n=int(input('enter a number'))
r=reduce(lambda x,y:x*y,range(1,n+1))
print(r)