w=str(input('enter a word'))
v="AEIOUaeiou"
new=' '
for i in w:
    if i not in v:
     new=new+i
print('The word without vowels is ',new)