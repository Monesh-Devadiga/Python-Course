#Dictionaries Operations, Methods and Functions 

#Dictionaries: mutable, unordered, 
# key-value pairs
#can be created using curly braces {} or 
# the dict() function
birthdays = {
    "Alice": "1990-01-01",
    "Bob": "1990-02-02",
    "Charlie": "1990-03-03"
}
print(birthdays)  # Output: {'Alice': '1990-01-01', 'Bob': '1990-02-02', 'Charlie': '1990-03-03'}
# fruits = {
#     "apple": 5,
#     "banana": 2.0,
#     "cherry": 3.0
# }

# print(birthdays)  # Output: {'Alice': '1990-01-01', 'Bob': '1990-02-02', 'Charlie': '1990-03-03'}   
# print(fruits)  # Output: {'apple': 5, 'banana': 2.0, 'cherry': 3.0} 

#print(birthdays["Alice"])  # Access value by key, Output: 1990-01-01    
#print(fruits["apple"])  # Access value by key, Output: 5

#accessing values using get() method
# print(birthdays.get("Bob"))  # Output: 1990-02-02
# print(birthdays.get("David", "data Not found"))  # Output: data Not found 

#adding new key-value pair
# birthdays["David"] = "1990-04-04"  # Add new key  
# print(birthdays)  # Output: {'Alice': '1990-01-01', 'Bob': '1990-02-02', 'Charlie': '1990-03-03', 'David': '1990-04-04'}    

#updating existing key-value pair
#birthdays["Alice"] = "1991-01-01"  # Update existing key  
#print(birthdays)  # Output: {'Alice': '1991-01-01', 'Bob': '1990-02-02', 'Charlie': '1990-03-03', 'David': '1990-04-04'}  

#removing key-value pair
#del birthdays["Charlie"]  # Remove key-value pair by key       
#print(birthdays)  # Output: {'Alice': '1991-01-01', 'Bob': '1990-02-02', 'David': '1990-04-04'}   

#removing key-value pair using pop() method
#birthdays.pop("Bob")  # Remove key-value pair by key using pop() method    
#print(birthdays)  # Output: {'Alice': '1991-01-01', 'David': '1990-04-04'}

#methods
#print(birthdays.keys())  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
#print(birthdays.values())  # Output: dict_values(['1990-01-01
#print(birthdays.items())  # Output: dict_items([('Alice', '1990-01-01'), ('Bob', '1990-02-02'), ('Charlie', '1990-03-03')])

#print(birthdays.update({"Alice": "1989-02-03"}))  # Update existing key-value pair
#print(birthdays)  # Output: {'Alice': '1989-02-03', 'Bob': '1990-02-02', 'Charlie': '1990-03-03'}   
#print(birthdays.get("Alice"))  # Output: 1989-02-03

#to add total number of key-value pairs in the dictionary
#print(len(birthdays))  # Output: 3







