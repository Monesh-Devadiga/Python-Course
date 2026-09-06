#Homework-1 Questions Solved - Tips and Tricks

# l = [1, 25, 71, 45, 3, 9]
# l.sort(reverse=True)
# print(l)

# import time
# i = 5 
# while i > 0:
#     print(i)
#     time.sleep(5)
#     i -= 1

#print number of vowels in a string
vowels = "aeiouAEIOU"
string = input("Enter a string: ")  
count = 0
for char in string:
    if char in vowels:
        print(char, end = " ")
        count += 1
print(f"\nNumber of vowels in the string: {count}")
