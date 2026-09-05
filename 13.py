# Lambda Functions, Recursion, args and kwargs

# def add(*args):
#     return sum(args)
# a = add(1, 2, 3, 4)  # Returns 10
# print(a)  # Output: 10

# def add(*args):
#     return type(args)  # Returns the type of args, which is a tuple
# a = add(1, 2, 3, 4)  
# print(a)  

# def add(**args):
#     return type(args)  # Returns the type of args, which is a tuple
# a = add(x=1, y=2, z=3)  
# print(a)  
#----------------------------------------------------------------------------------------------
#args and kwargs
#args
# def add(*args):
#     return sum(args)

#kwargs
# def add(**kwargs):
#     return sum(kwargs.values())

#----------------------------------------------------------------------------------------------
#Lambda Functions
# add = lambda x, y: x + y
# a = add(5, 3)  # Returns 8
# print(a)  # Output: 8

# square = lambda x: x**2
# b = int(input("Enter a number: ")) # Returns 16
# print(square(b))  # Returns 256

# students = [
    
#     {'name': 'Alice', 'age': 20},
#     {'name': 'Bob', 'age': 22},
#     {'name': 'Charlie', 'age': 19}
# ]
#students.sort() #Error: '<' not supported between instances of 'dict' and 'dict' 
                # Therefore use Lambda function to sort the list of dictionaries based on a specific key, such as 'age' or 'name'.

# students.sort(key=lambda x: x['age'])
# print(students)  # Output: Ascending order -- [{'name': 'Charlie', 'age': 19
# students.sort(key=lambda x: x['age'], reverse=True)  # Sorts in descending order based on age
# print(students)

#----------------------------------------------------------------------------------------------
# Recursion
#Factorial of a number using recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1) 

# fact = int(input("Enter a number: "))  # Returns 120
# print(factorial(fact))  # Output: 120

#----------------------------------------------------------------------------------------------
#Nested Functions
# def outer_function(x):   
#     def inner_function(y):
#         return y + 1
#     return inner_function(x)  # Returns 6

# a = int(input("Enter a number: "))  # Returns 5
# b = outer_function(a)  
# print(b)  # Output: 6


