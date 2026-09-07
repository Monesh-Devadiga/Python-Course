"""
#Factorial of Number:
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

a = int(input("Enter num: "))
n = a
print(f"Input num is: {n}")
res = fact(n)
print(f"Factorial is: {res}")
"""

"""
#Fibonacci series: without recursion
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b

#Fibonacci series: with recursion
def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]

  fib_series = [0, 1]
  for _ in range(2, n):
    next_num = fib_series[-1] + fib_series[-2]
    fib_series.append(next_num)

  return fib_series
n = int(input("Enter the number of terms: "))
result = fibonacci(n)
print(f"Fibonacci series (first {n} terms):", result)
"""


"""
#Max of arr
def maximum(arr, i=0):
    if i == len(arr) - 1:
        return arr[i]

    return max(arr[i], maximum(arr, i + 1))

a = maximum([1, 2, 34, 5, 1185, 0.5, 8, 9])
print(f"max ele is: {a}") 
b = maximum([2])
print(f"max ele is: {b}") 
"""
