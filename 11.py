#Comprehension  |  List Input  |  Loops Revision

"""  
#loop in list
l=[1,2,3,4,5]
total=0
for num in l:
    total+=num
print(total)
"""

"""
#loop in dictonaries
st_mark={"manu":85, "rahul":85, "abhi":67}
for st,mark in st_mark.items():
    print(f"{st} - {mark}")
    print(st)
    #print(mark)
"""

"""
#list Comprehension
l=[x for x in range(1,6)]       #same as l= [1,2,3,4,5]
dl = [item*2 for item in l]
print(dl)   #to doubling the values
dl = [item**2 for item in l] #square
print(dl)   
"""
"""
l=[x for x in range(1,11)]       #same as l= [1,2,3,4,5,6,7,8,9,10]
even_dl = [item*2 for item in l if item%2]
print(l)
print(even_dl)   #to doubling the values of even numbers from l
"""

"""
#for dict
city_popul={
    "Mangalore":65,
    "Blr":92,
    "Mys":53,
    "Udupi":60
}
lar_cit={key:value for key,value in city_popul.items() if value>60}
print(f"The most populated cities: \n {lar_cit}")
"""

"""
#convert to list
s="this is a computer"
print(s)
l = s.split()
print(l)
"""

"""
x = input("Enter list of int:").split()
print(f"Given input in list type: {x}")
l = [int(num) for num in x]
print(f"converted to int {l}")
"""

#=======
#---------------------------------------------------------
#Looping through lists
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)    

# numbers = [1, 2, 3, 4, 5]
# total = 0
# for num in numbers:
#     total += num
# print(f"The total sum of numbers in the list is: {total}")

#----------------------------------------------------------------------
#Looping through dictionaries
# student_marks = {"manu": 85, "rahul": 85, "abhi": 67}
# for student, mark in student_marks.items():       
#     print(f"{student} - {mark}")

# for mark in student_marks.values():   #printing only values     
#     print(f"{mark}")

# for student in student_marks.keys():       
#     print(f"{student} - {student_marks[student]}") #printing only keys and values using keys() method

#range function
# for i in range(5):
#     print(i)  #prints 0 to 4
# for i in range(1, 6):
#     print(i)  #prints 1 to 5

#in lists
# students = ["manu", "rahul", "abhi"]
# # for i in range(len(students)):
# #     print(f"{i} - {students[i]}")  #prints index and value of list
# marks = [85, 85, 67]
# # for i in range(len(marks)):
# #     print(f"{i} - {marks[i]}")  #prints index and value of list

# student_marks = {}
# # for i in range(len(students)): #total length of students list
# #     student_marks[students[i]] = marks[i]
# # print(student_marks)  #prints dictionary with keys and values from two lists

# for i in range(1,2): #specifying the range to loop through only the first index of the list
#     student_marks[students[i]] = marks[i]
# print(student_marks)  #prints dictionary with keys and values from two lists

#-----------------------------------------------------------------------
#List Comprehension
#l = [1, 2, 3, 4, 5 ]
#to create  l u can use list comprehension as follows:
l = [x for x in range(1, 6)]  #creates a list of numbers from 1 to 5

# dl = [item*2 for item in l]  #doubles the values in the list
# print(dl)  #prints [2, 4, 6, 8,10]
# dl = [item**2 for item in l]  #calculates the square of each value in the list
# print(dl)  #prints [1, 4, 9, 16, 25]

# dl = [item*2 for item in range(len(l))]  #doubles the values in the list
# print(dl)  

#only even numbers from the list (or any condition for the elements of list)
# even_dl = [item*2 for item in l if item%2==0]
# print(even_dl)

#for strings
# fruits = ["apple", "banana", "cherry"]
# cl = [item.upper() for item in fruits]  #converts all the strings in the list to uppercase
# print(cl)  #prints ['APPLE', 'BANANA', 'CHERRY']

# cl =[item[1] for item in fruits]  #prints the second character of each string in the list
# print(cl)  #prints ['p', 'a', 'h']

#-----------------------------------------------------------------------
#dictionary comprehension
# names = ["manu", "rahul", "abhi"]
# d = {name: len(name) for name in names}  #creates a dictionary with names as keys and their lengths as values
# print(d)  #prints {'manu': 4, 'rahul': 5, 'abhi': 4}

# city_population = {
#     "Mangalore": 65,
#     "Bengaluru": 85,
#     "Mysore": 45
# }
# # large_cities = {city: population for city, population in city_population.items() if population > 60}  #creates a dictionary with cities having population greater than 60
# # print(large_cities)  #prints {'Mangalore': 65, 'Bengaluru': 85}
# # highest_population_city = {city: population for city, population in city_population.items() if population == max(city_population.values())}  #creates a dictionary with the city having the highest population
# # print(highest_population_city)  #prints {'Bengaluru': 85}
# most_populated_city = {city: population for city, population in city_population.items() if population > 60}  #creates a dictionary with the city having the highest population
# print(most_populated_city)  #prints {'Mangalore': 65, 'Bengaluru': 85}

#------------------------------------------------------------------------
#Inputting a list of integers from the user and converting them to a list of integers
x = input("Enter a list of integers separated by spaces: ").split()  #splits the input string into a list of strings
print(f"Given input in list type: {x}")  #prints the list of strings
l = [int(num) for num in x]  #converts the list of strings to a list of integers
print(f"Converted to int: {l}")  #prints the list of integers

