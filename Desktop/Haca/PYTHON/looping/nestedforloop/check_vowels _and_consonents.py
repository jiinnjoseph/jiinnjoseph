a=str(input('Enter the word '))
v="AEIOUaeiou"
vc=0
cns=0
for i in a:
    if i in v:
        vc+=1
    else:
        cns+=1
print(' the vowel count of the word is ',vc)
print('the consonence count of the word is ',cns)