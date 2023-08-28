# 4. Recursion:
# *> Create a recursive function which returns the n-th Fibonacci number.
# [Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]
# o Input: N=8
# o Output: 21

import time

n = int(input("Enter any number to get nth Fibonacci Number: "))

start = time.time()
fib_values = {}
def fib_recursive (num):
    if num < 2 :                                 
        return  num
    else:
        if num not in fib_values:
            fib_values[num] = fib_recursive(num - 1) + fib_recursive(num - 2 )
        return fib_values[num]

print(n,'th Fibbonacci number', fib_recursive(n))
end = time.time()
print(n,'Run time', end - start)


# *> Create a recursion function that calculate the sum of numbers present in the list. 
# o Input: numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
# o Output: 152

numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

def summation(numbers):  
    
    if len(numbers) == 0 :
        return 0
    
    else:
        return numbers[0] + summation(numbers[1:])

print("Answer = ", summation(numbers))