# Functions, Parameters, Local vs Global var

#Functions - are blocks of code that perform a specific task. They can take inputs (parameters) and return outputs.
# def greet(name):
#     # Local variable 'greeting' is defined within the function
#     greeting = f"Hello, {name}!"
#     return greeting
# print(greet("Alice"))

# #function to print table of a number
# def print_table(num):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")
# a = input("Enter number:")
# print_table(int(a))
# #print_table(5)  # Calling the function with a different number

#Functions - default parameters
# def greet(name="Guest"):
#     # Local variable 'greeting' is defined within the function
#     greeting = f"Hello, {name}!"
#     return greeting
# print(greet())  # Calls the function without an argument, using the default value

#---------------------------------------------
#Local vs Global Variables
# Local variable
# def print_values():
#     local_var = "I am a local variable"
#     print(local_var)  # This will work  
# print_values()

# # Global variable
# global_var = "I am a global variable"  
# def print_global():
#     print(global_var)  # This will work because global_var is defined in the global scope
# print_global()

