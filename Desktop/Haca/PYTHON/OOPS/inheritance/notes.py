# ========================== Inheritance in Python ================================


# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). In this article, we'll explore inheritance in Python.

# Example: Here, we create a parent class Animal that has a method info(). Then we create a child classes Dog that inherit from Animal and add their own behavior.




class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
d.info()      # Inherited method
d.sound()

# =============== super() Function ==================

# super() function ------>.  Is used to call the parent class’s methods. In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. This way, the child class can leverage the functionality of the parent class.

# Example: Here, Dog uses super() to call Animal’s constructor




# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Buddy", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method



# =========== Types of Python Inheritance ===============


# 1. Single Inheritance


# In single inheritance, a child class inherits from just one parent class.


class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def show_role(self):
        print(self.name, "is an employee")

emp = Employee("Sarah")
print("Name:", emp.name)
emp.show_role()


# 2. Multiple Inheritance::


# In multiple inheritance, a child class can inherit from more than one parent class.

# Example: This example demonstrates Employee inheriting properties from two parent classes: Person and Job.




class Person:
    def __init__(self, name):
        self.name = name

class Job:
    def __init__(self, salary):
        self.salary = salary

class Employee(Person, Job):  # Inherits from both Person and Job
    def __init__(self, name, salary):
        Person.__init__(self, name)
        Job.__init__(self, salary)

    def details(self):
        print(self.name, "earns", self.salary)

emp = Employee("Jennifer", 50000)
emp.details()


# 3. Multilevel Inheritance::


# In multilevel inheritance, a class is derived from another derived class (like a chain).

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def show_role(self):
        print(self.name, "is an employee")

class Manager(Employee):  # Manager inherits from Employee
    def department(self, dept):
        print(self.name, "manages", dept, "department")

mgr = Manager("Joy")
mgr.show_role()
mgr.department("HR")

# 4. Hierarchical Inheritance::

# In hierarchical inheritance, multiple child classes inherit from the same parent class.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "works as an employee")

class Intern(Person):  
    def role(self):
        print(self.name, "is an intern")

emp = Employee("David")
emp.role()

intern = Intern("Eva")
intern.role()


# 5. Hybrid Inheritance ::

# Hybrid inheritance is a combination of more than one type of inheritance

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, project_name):
        self.project_name = project_name

class TeamLead(Employee, Project):  # Hybrid Inheritance
    def __init__(self, name, project_name):
        Employee. __init__(self, name)
        Project. __init__(self, project_name)

    def details(self):
        print(self.name, "leads project:", self.project_name)

lead = TeamLead("Sophia", "AI Development")
lead.role()
lead.details()