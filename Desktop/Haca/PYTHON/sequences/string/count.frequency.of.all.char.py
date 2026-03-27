w=str(input('enter the word'))
j=' '
for i in w:
     if w.count(i)>1  and i not in j:
      j+=i
print(j)