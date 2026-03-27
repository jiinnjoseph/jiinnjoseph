# w=input("enter a word")
# d=' '
# new=' '
# for i in range(len(w)):
#     for j in range(i+1,len(w)):
#         if w[i]==w[j]:
#             d=d+w[i]
#             break
# for i in w:
#      if i not in d:
#       new+=i
# print(new)

w=input('Enter the word ')
d=''
for i in w:
    if i not in d:
        d+=i
print(d)
