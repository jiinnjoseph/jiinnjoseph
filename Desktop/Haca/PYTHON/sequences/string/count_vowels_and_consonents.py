a=str(input('enter a word'))
v="AEIOUaeiou"
VC=0
cns=0
for i in a:
    if i in v:
        VC+=1
else:
      cns+=1
print(' the vowel count of the word is ',VC)
print('the consonence count of the word is ', cns)