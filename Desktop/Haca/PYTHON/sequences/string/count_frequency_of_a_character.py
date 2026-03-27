w=str(input('enter the word '))
f=str(input('enter the character '))
count=0
for i in w:
    if f == i:
     count+=1
print(f"the total count of {f} in {w} is ",count)