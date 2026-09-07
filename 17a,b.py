# 17 A
# Pillars of OOP = Abstraction & Encapsulation

"""
#Abstraction is the process of hiding the implementation details and showing only the functionality to the user. 
It helps to reduce programming complexity and effort.
#example: Accelarating the bike's speed by throttle, but we don't know how the engine works.

"""

"""
#Encapsulation is the process of wrapping the data (attributes) and code (methods) together as a single unit.
It helps to protect the data from outside interference and misuse.
#Examples: hiding finance detail of eployee from other employees, hiding the salary of employee from other employees.

"""
#---------------------------------------------------------------------------------------------------------------------------------------------
#17 B
# Pillars of OOP = Inheritance & Polymorphism

""" 
#Inheritance is the p rocess by which one class (child class) can inherit the properties and methods of another class (parent class).
It helps to promote code reusability and establish a relationship between classes.
#Example: A child class "Car" can inherit properties and methods from a parent class "Vehicle".

class Vehicle:
    def __init__(self, brand, model):   
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model) #super() is used to call the constructor of the parent class (Vehicle) to initialize the brand and model attributes.
        self.year = year

audi = Car("Audi", "A4", 2020)
print(audi.brand)  # Output: Audi
"""

"""
#Polymorphism is the ability of an object to take on many forms. 
It allows methods to do different things based on the object it is acting upon.
#Example: A method "area" can calculate the area of different shapes like circle, rectangle

class Shape:
    def area(self): 
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius 

class Rectangle(Shape):
    def __init__(self, width, height):  
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

cir1 = Circle(5)
rect1 = Rectangle(4, 6)

print(cir1.area())  # Output: 78.5
print(rect1.area())  # Output: 24
"""