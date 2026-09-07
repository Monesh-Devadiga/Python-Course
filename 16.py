# Constructor, self keyword, optional parameters

"""
#Example:
class Human:
    def __init__(self, name):
        self.name = name  # instance attribute

    #function for walking
    def walk(self):
        print(f"{self.name} is walking.")
#now create obj to that class and call the function
person1 = Human("Alice")
person1.walk()             #output: Alice is walking.
person2 = Human("Bob")
person2.walk()             #output: Bob is walking.
"""

"""
#Constructor is a special method in Python classes that is automatically called when an object of the class is created. It is defined using the __init__() method and is used to initialize the attributes of the object.
#self is a reference to the current instance of the class and is used to access the attributes and methods of the class. It is passed as the first parameter to all instance methods in Python classes.
self is compulsory in def

#here person1 and person2 are multiple objects of the Human class
"""

"""
#Optional parameters in Python classes are parameters that have default values. If a value is not provided the default value will be used.
#Example:
class Employee:
    def __init__(self, name, salary=50000):  # salary is an optional parameter with a default value of 50000
        self.name = name    
        self.salary = salary
    
e1 = Employee("John")  # salary will take the default value of 50000
e2 = Employee("Jane", 60000)  # salary will take the provided value
print(f"Salary of {e1.name} is:")  # output: John
print(e1.salary)  # output: 50000
print(f"Salary of {e2.name} is:")  # output: Jane
print(e2.salary)  # output: 60000
"""




