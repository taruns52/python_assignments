# 4. Recursion:
# *> Create a recursive function which returns the n-th Fibonacci number.
# [Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...]
# o Input: N=8
# o Output: 21



n = int(input("Enter any number to get nth Fibonacci Number: "))

fibo_values = {}

# def fib_recursive (num):
#     if num < 2 :                                  #commented this function as it was unable to return 60th fibo no and used below one.
#         return  num
#     else:
#          fib_recursive(num - 1) + fib_recursive(num - 2 )




                    # --------------------------------------------------------------------------------------------

# o Also, check if your recursive function is able to return the Fibonacci value at 60th or 90th term? 
# If no, then check the concept of memoization for Fibonacci in recursive way.


def fib_recursive(n):
    if n <= 1:
        answer = [n, 0]
        return answer
    else:
        tmp = fib_recursive(n-1)
        answer = [tmp[0] + tmp[1], tmp[0]]
        return answer
        
print(n,'th Fibbonacci number', fib_recursive(n))


                    # --------------------------------------------------------------------------------------------

# *> Create a recursion function that calculate the sum of numbers present in the list. 
# o Input: numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]
# o Output: 152

numbers = [23, 44, 5, 67, 1, 1, 2, 4, 5]

def summation(total=0, numbers=[], index = -1):  
    
    if index < 0 :
        return total
    
    else:
        return summation(total+numbers[index], numbers, index-1)

print("Answer = ", summation(0, numbers, len(numbers)-1))