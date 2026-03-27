# abstraction means hide everything not needed  and shows everything needed

# like shows color and not not color code


# code:-

from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass  # Abstract method

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())


##just print Hello