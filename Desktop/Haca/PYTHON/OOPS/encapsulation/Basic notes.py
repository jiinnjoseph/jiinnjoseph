# is an object-oriented programming concept that involves bundling data (attributes) and methods
#  that operate on that data within a single unit, a class

# 1.public
# 2.private
# 3.protected

# Public: Default, accessible anywhere.
# Protected: Indicated by a single underscore (_variable), signaling internal use.
# Private: Indicated by a double underscore (__variable), intended for use only within the class.


# private and public examples

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name          # public attribute --> can directly acess
#         self.__salary = salary    # private attribute  -->cannot directly acess and do not prints
#         self._salary = salary     #protected attribute -->

# emp = Employee("Fedrick", 50000)
# print(emp.name)       
# print(emp.__salary)
# print(emp._salary)


# public and protected Exaamples

class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Ross", 30)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass  cannot print directly