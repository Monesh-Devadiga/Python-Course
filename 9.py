#While Loops | Break and Continue| Nested Loops

#while loops are used to execute a block of code repeatedly 
    # as long as a condition is true.

"""
syntax:
    # while condition:
    #     code block

    Eg:
    from altair import condition
    while condition:
        print("This will print as long as the condition is true.")
"""

is_failed = True
i=1
#while is_failed:
#while i<=5:
# while is_failed and i<=5:
#     print(f"Try {i}st attempt failed. Retrying...")
#     i+=1
#     #break  # Exit the loop after the first iteration for demonstration purposes
# print("All attempts failed. Please try again later.")

"""
#with continue statement, we can skip the current iteration and move to the next iteration of the loop  
#with break statement, we can exit the loop entirely, regardless of the condition.
while is_failed:
    if i%2 != 0: #is not even
        i+=1
        continue  # Skip the rest of the loop and go to the next iteration
    print(f"Try {i}st attempt failed. Retrying...")
    i = i + 1
    if i > 50:
        break  # Exit the loop after 5 attempts
print("All attempts failed. Please try again later.")
"""


"""
#login example
pin="1234"
input_pin=input("Enter your pin: ")
while input_pin != pin:
    print("Incorrect pin. Please try again.")
    input_pin=input("Enter your pin: ")
print("Pin accepted. Access granted.")
"""


"""
#login example with limited attempts
pin="1234"

attempts=1
while True:
    input_pin=input("Enter your pin: ")
    if input_pin == pin:
        print("Pin accepted. Access granted.")
        break
    else:
        print("Incorrect pin. Please try again.")
        attempts+=1
        if attempts>3:
            print("Too many incorrect attempts. Access denied.")
            break
"""

