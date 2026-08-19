"""
#input and output in python
#use print() function to display output
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")

age = input("Enter your age: ")
print("You are " + age + " years old.")
"""

boy=input("enter boy name: ")
bage=int(input("enter boy age: "))
girl=input("enter girl name: ")
gage=int(input("enter girl age: "))
#agediff= int(bage) - int(gage)
agediff= abs(bage - gage) #abs is used to get absolute value of difference between two numbers and avoids negative values 
#print("Age difference between " + boy + " and " + girl + ": " + str(agediff))
#print("Hello, " + boy + " loves " + girl + "!")
print(f"Age difference between {boy} and {girl}: {agediff}")
