# Types of Function Arguments

# Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python, Let's explore them one by one.

# 1. Default Arguments

# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

# myFun(10)

# 2. Keyword Arguments

# In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.


# def student(fname, lname):
#     print(fname, lname)

# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks')

# 3. Positional Arguments

# In positional arguments, values are assigned to parameters based on their order in the function call.

# def sum(a,b):
#     return a+b
# print(sum(3,5))

# 4. Arbitrary Arguments

# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:
# '*'(args) using in non keyword argument.
# "**" using keyword arguments.
# def sum(*n):
#     s=0
#     for i in n:
#         s+=i
#     return s
# print(sum(10,4))