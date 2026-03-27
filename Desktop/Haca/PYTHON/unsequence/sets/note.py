# # Set

# # Sets are used to store multiple items in a single variable.

# # Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# # A set is a collection which is unordered, unchangeable*, and unindexed.

# # * Note: Set items are unchangeable, but you can remove items and add new items.

# # Sets are written with curly brackets.


# # Set items are unordered, unchangeable, and do not allow duplicate values.

# # Get the Length of a Set:

# # To determine how many items a set has, use the len() function.


#  s={1,2,3,4,5,'a','b','c',1,2}

# 1.  add()
# s.add()
# print(s)

# 3.pop()
# s.pop()
# print(s)

# 4.remove()
# s.remove(1)
# print(s)

# print(1 in s)
# for i in s:
#     print(i)
# print(s[0])
# print(len(s))

s={1,2,3,4,5,'a','b','c',1,2}
s1={'apple','cherry','bananna'}



# 2.union
# s3=s.union(s1)
# print(s3)


# 3.intesection update
# s.intersection_update(s1)
# print(s)

# 4.intesection
# s3=s.intersection(s1)
# print(s3)

# 5.symmetric differece update
s.symmetric_difference_update(s1)
print(s)