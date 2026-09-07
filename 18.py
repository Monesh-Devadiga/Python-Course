# Getters Setters, Overloading & Overriding, Abstract Class

"""
#Getters and Setters
Getters and Setters are used to access and update the value of a private attribute of a class.
#Example: A class "Employee" has a private attribute "_salary". We can use a getter method to access the value of "_salary" and a setter method to update the value of "_salary".

class student:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.age = age

    def get_name(self): #getter method
        return self.__name

    def set_name(self, name): #setter method
        print("After new name setted ")
        self.__name = name  

s = student("John", 22)
print(s.get_name())  # Output: Monesh
s.set_name("Alice")
print(s.get_name())  # Output: Alice
s.set_name("Bob")
print(s.get_name())  # Output: Bob
"""

"""
#Overloading
Overloading is a feature in OOP that allows a class to have 
multiple methods with the same name but different parameters. 
This allows for more flexibility in how methods can be called and used.
#Example: A class "Calculator" has a method "add" that can take two or three parameters. If two parameters are passed, it adds them together. If three parameters are passed, it adds all three together.   
"""

"""
#Overriding
Overriding is a feature in OOP that 
allows a subclass to provide a specific implementation of a method that is already defined in its superclass. 
This allows the subclass to change or extend the behavior of the method.
#Example: A class "Animal" has a method "sound" that prints "Animal makes a sound". 
# A subclass "Dog" overrides the "sound" method to print "Dog barks". When the "sound" method is called on an instance of the "Dog" class, it will use the overridden method in the subclass instead of the method in the superclass.
"""

"""
#Abstract Class
An abstract class is a class that cannot be instantiated and is meant to be subclassed.

"""

