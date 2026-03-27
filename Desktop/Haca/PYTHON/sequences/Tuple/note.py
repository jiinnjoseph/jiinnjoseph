# # Tuple


# # Tuples are used to store multiple items in a single variable.

# # Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# # A tuple is a collection which is ordered and unchangeable.

# # Tuples are written with round brackets.   

# eg:
# a = ("apple", "banana", "cherry")
# print(a)


# Tuple Items

# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# ordered 
# unchangeable

# Tuble are allow duplicates.

# length of a tuple:

# a = ("apple", "banana", "cherry")
# a=len(a)


# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple

# thistuple = ("apple")
# print(type(thistuple))

# Tuple Items - Data Types    

# Tuple items can be of any data type:

# Example
# String, int and boolean data types:

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)

# A tuple can contain different data types:

# tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor

# It is also possible to use the tuple() constructor to make a tuple.

# Example
# Using the tuple() method to make a tuple:

# Eg:
# a=tuple(('apple','banana','cherry'))
# print(a)

# modify tuple into other datatypes:


#         Normally tuple are non changeable; But some cases we can change tuple into list and modify what datatypes we want:
        
# eg:
# a=(1,2,3,4,'hi',7,'hello')
# a=(list(a))
# a.append('java')
# print(a)

