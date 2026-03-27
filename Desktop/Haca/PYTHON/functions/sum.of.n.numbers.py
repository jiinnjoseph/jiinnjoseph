
def sum_n(*n):
    num=[]
    l=int(input('enter the number limit'))  
    s=0
    for i in range(l):
        numbers=int(input('enter the number'))
        num.append(numbers)
    for i in num:
        s+=i
    return s
print(sum_n())