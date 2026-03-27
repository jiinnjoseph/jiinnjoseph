a=[1,2,5,7,"hello",4.7,"Hi",2,5]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
          break
    else:
        d.append(a[i])

print(d)


a=[1,2,5,7,"hello",4.7,"Hi",2,5]
d=[]
for i in a:
    if i not in d:
        d.append(i)
print(d)
