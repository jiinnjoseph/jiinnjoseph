from functools import reduce
a=[2,3]
r=reduce(lambda x,y:x*y,a)
print(r)