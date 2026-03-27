a=[4,8,9,1,2]
def even(a):
    return(a%2==0)
f=filter(even,a)
print(list(f))