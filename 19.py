# Menu Driven Programs | Simple Calculator

#simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    a = "Divide by zero is error!"
    if b == 0:
       return a
    else:
        return a/b
print("Simple Calculator Menu")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Divison")
print("5. Quit")
ch = int(input("Enter the choise:"))

if ch in {1, 2, 3, 4}:
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))

if ch == 1:
    print("Addition Result", add(a,b))
elif ch == 2:
    print("Substraction Result", sub(a,b))
elif ch == 3:         
    print("Multiplication Result", mul(a,b))
elif ch == 4:
    print("Divison Result", div(a,b))
elif ch == 5:
    print("Quitting")
    # exit()
else:
    print("Invalid Input choice! \nEnter valid Input")