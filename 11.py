#Comprehension | List Input | Loops Revision
n
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
