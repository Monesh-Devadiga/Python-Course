# Tuples and Sets Operations & Difference

#tuples: immutable, ordered, allows duplicates
    # faster than lists, used for fixed data, can be used as dictionary keys
#   gender = ("male", "female", "other")  # Tuple
# print(gender)

# print(gender[0])  # Access first item
# print(gender[1:3])  # Access items from index 1 to 2

# gender.count("male")  # Count occurrences of "male"
# print(gender.count("male"))  # Output: 1

# # gender.append("non-binary")  # This will raise an error because tuples are immutable    

#gender_list = list(gender)  # Convert tuple to list
# gender_list.append("non-binary")  # Now we can add an item
# print(gender_list)  # Output: ['male', 'female', 'other', 'non-binary']

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple_sum = tuple1 + tuple2  # Concatenate tuples
# # print(tuple_sum)  # Output: (1, 2, 3, 4, 5, 6)

# tuple_mul = tuple1 * 2  # Repeat tuple
# # print(tuple_mul)  # Output: (1, 2, 3, 1, 2, 3)

#print("male" in gender)  # Check membership, 
#Output: True  

#print(gender.count("female"))  # Output: 1


#---------------------------------------------------
#---------------------------------------------------
#sets: mutable, unordered, no duplicates
#collections of unique items, used for membership testing, removing duplicates, mathematical operations like union, intersection, difference
#its unordered, so indexing and slicing are not possible, but you can iterate through the set using a loop
fruits = {"apple", "banana", "cherry"}  # Set   
fruits2 = {"kiwi", "mango"}  # Set
#print(fruits)  # Output: {'banana', 'cherry', 'apple'}

#fruits.add("orange")  # Add item to the set
#print(fruits)  # Output: {'banana', 'cherry', 'apple', 'orange'}

#union_set = fruits.union({"kiwi", "mango"})  # Union of sets
#print(union_set)  # Output: {'banana', 'cherry', 'kiwi', 'apple', 'mango', 'orange'}

#intersection_set = fruits.intersection({"banana", "kiwi"})  # Intersection of sets
#print(intersection_set)  # Output: {'banana'}

#fruits.remove("banana")  # Remove item from the set
#print(fruits)  # Output: {'cherry', 'apple'}   
#fruits2.discard("kiwi")  # Remove item from the set, no error if item not found
#print(fruits2)  # Output: {'mango'}
# fruits.clear()  # Clear all items from the set
# #print(fruits)  # Output: set()
# fruits.add("apple2")  # Add item to the set
# print(fruits)  # Output: {'banana', 'cherry', 'apple'}
# fruits.add("banana")  # Add item to the set 
# print(fruits)  # Output: {'banana', 'cherry', 'apple'}  # No duplicates allowed

# fruits.add("strawberry")  # Add item to the set
# print(fruits)  # Output: {'banana', 'cherry', 'apple', 'strawberry'}

#fruits.pop()  # Remove and return an arbitrary item from the set
#print(fruits)  # Output: {'banana', 'cherry', 'apple'} 


"""
Difference between List, Tuple and Set

| Feature     | List               | Tuple             | Set            |
| ----------- | ------------------ | ----------------- | -------------- |
| Ordering    | Ordered            | Ordered           | Unordered      |
| Mutability  | Mutable            | Immutable         | Mutable        |
| Duplicates  | Allows duplicates  | Allows duplicates | No duplicates  |
| Indexing    | Supports indexing  | Supports indexing | No indexing    |
| Operations  | List operations    | Tuple operations  | Set operations |
| Common Uses | General collection | Fixed data        | Unique items   |

"""