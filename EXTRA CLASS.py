#Use Debugger to practice loops and conditional statements

#Debugging is a process of finding and resolving bugs or defects that prevent correct operation of computer software or a system. In this exercise, we will practice using loops and conditional statements in Python.   

# i = 0
# while i < 5:
#     print(i, end = " ")
#     i += 1

for i in range(1, 2):
    for j in range(1, 11):
        print(f"{i} X {j} = {i * j}")