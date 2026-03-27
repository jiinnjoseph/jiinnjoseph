from functools import reduce
a=[1,3,2,1,4,8,9,1,2,45,89,22]
r=reduce(lambda x,y: (x) if x>y else (y),a)
print(r)