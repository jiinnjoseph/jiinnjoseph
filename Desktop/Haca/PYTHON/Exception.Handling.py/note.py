# =================== Python Exception Handling ============


# Python Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.

# Basic Example: Handling Simple Exception:

# Here’s a basic example demonstrating how to catch an exception and handle it gracefully

n = 10
try:
    res = n / 0
except ZeroDivisionError:
    print("Can't be divided by zero!")

# Explanation: Dividing a number by 0 raises a ZeroDivisionError. The try block contains code that may fail and except block catches the error, printing a safe message instead of stopping the program.

# Difference Between Errors and Exceptions::: 

# Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

# Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
# Example: This example shows the difference between a syntax error and a runtime exception


# Syntax Error (Error)
# n=int(input('Enter the number' )): # Missing closing parenthesis
try:
   res = n / 0
except ZeroDivisionError:
      print("Can't divide by 0")


# Difference Between Errors and Exceptions::


# Errors and exceptions are both issues in a program, but they differ in severity and handling. Let's see how:

# Error: Serious problems in the program logic that cannot be handled. Examples include syntax errors or memory errors.
# Exception: Less severe problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
# Example: This example shows the difference between a syntax error and a runtime exception.

# Syntax Error (Error)
print("Hello world")  # Missing closing parenthesis

# ZeroDivisionError (Exception)
n = 10
res = n / 0

# Syntax and Usage:: 

# Python provides four main keywords for handling exceptions: try, except, else and finally each plays a unique role. Let's see syntax:

# try:
#       # Code 
# except SomeException:
#       # Code 
# else:
#      # Code 
# finally:
#     # Code 

# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.


try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete ")