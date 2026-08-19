#For Loops | Range, Enumerate | Nested Loops 

#for loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.  

"""
#Range
for i in range(5,10):  # Iterate over a sequence of numbers from 5 to 9
    print(i)  # Output: 5, 6, 7, 8, 9

#alternatives
for i in range(5,10,2):  # Iterate over a sequence of numbers from 5 to 9
    print(i, end="-")  # Output: 5, 7, 9
"""

# bag = ["a", "b", "c"]
# for b in bag:
#     print(b)


"""
#enumerate
name = "Vinayak"
for letter in enumerate(name):
    print(letter*3, end="\n") #prints with index

"""

"""
#print table for single table
for i in range(1,11):
    print(f"2 X {i} = {2*i}")
"""
#print table for all
for i in range(1,11):
    for j in range(1,11): 
        print(f"{i} X {j} = {i*j}")
    print("\n")
