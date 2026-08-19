# Lists Operations, Methods and Functions

#lists
from operator import index


items = ["bru", "sugar", "paste", "soap", "towel"]
# print(items)
    #output: ['bru', 'sugar', 'paste', 'soap', 'towel']

# print(items[0])  # Access first item
    #output: bru
# print(items[1:4])  # Access items from index 1 to 3
     #output: ['sugar', 'paste', 'soap']

#items2 = ["ab", 2, 3.5, True] #all data types can be stored in list
     #output: ['ab', 2, 3.5, True]

# items.pop()  # Remove last item
# print(items)
     #output: ['bru', 'sugar', 'paste', 'soap']

# items.append("shampoo")  # Add item to the end
# print(items)
     #output: ['bru', 'sugar', 'paste', 'soap', 'towel', 'shampoo']

# items.remove("sugar")  # Remove specific item
# print(items)
     #output: ['bru', 'paste', 'soap', 'towel']

# items.insert(2, "toothpaste")  # Insert item at index 2
# print(items)
     #output: ['bru', 'sugar', 'toothpaste', 'paste', 'soap', 'towel']

#indexing
# print(items[0])  # Access first item
     #output: bru
# print(items[1:4])  # Access items from index 1 to 3
     #output: ['sugar', 'toothpaste', 'paste']

# items.clear()  # Clear all items from the list
# print(items)  
    # Output: []

# items.sort()  # Sort the list in ascending order
# print(items)
     #output: ['bru', 'paste', 'soap', 'sugar', 'towel']

# items.sort(reverse=True)  # Sort the list in descending order
# print(items)
    #output: ['towel', 'sugar', 'soap', 'paste', 'bru']

# items[0] = "coffee"  # Change first item (bru changes to coffee)
# print(items)
#output: ['coffee', 'sugar', 'paste', 'soap', 'towel']

# len_items = len(items)  # Get the number of items in the list
# print("Number of items in the list:", len_items)
# #output: Number of items in the list: 5

# sum_items = sum([1, 2, 3, 4, 5])  # Get the sum of numeric items in the list
# print("Sum of numeric items in the list:", sum_items)   
# #output: Sum of numeric items in the list: 15

# index_of_sugar = items.index("sugar")  # Get the index of a specific item
# print("Index of 'sugar' in the list:", index_of_sugar)
# #output: Index of 'sugar' in the list: 1

#nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0])  # Access first sublist
#output: [1, 2, 3]
print(nested_list[1][2])  # Access item at index 2 of second sublist
#output: 6