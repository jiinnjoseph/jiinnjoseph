w=str(input('Type a word '))
r=''
for i in w:
    r=i+r
if w==r:
    print('palindrome')
else:
    print('not palindrome ')