# 5. You are given a list of numbers and your task is to find out the pairs that have sum equals n (provided during input).
#  No duplicate pair or similar pair should be in the output.
#  For example, if sum=12,

#     o [4, 8] can’t come twice in the output.
#     o Also, consider [4, 8] and [8, 4] as similar, so only [4, 8] have to come, not both.

# Input: Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8] o n = 12

#  Output: [[3, 9], [4, 8], [2, 10]]
# See here, each pair addition is equals to 12 i.e. (3+9=12, 4+8=12, 2+10=12)

sum = int(input("Enter Sum: "))

Numbers = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]

solution = []

for num in Numbers:
    if (
        sum - num in Numbers
        and [num, sum - num] not in solution
        and [sum - num, num] not in solution
    ):
        solution.append([sum - num, num])

print(solution)


# Appraoach :

"""
lets say, sum = 12

    if sum-num in Numbers and [num, sum-num] not in solution and [sum-num, num] not in solution:
    
    1st condition: True
        12 - 8 is 4 which in Numbers
    2nd condition and 3rd condition : True
        as [4,8] and [8,4] are not present in solutions list

hence we will append [4,8] to solutions



Expalnation:

Let's say sum = 12:

Here, instead of using a nested loop to iterate through all possible pairs of numbers, I use a more efficient approach.

Let's assume a is the current number you're iterating over. Now we have two values sum and a

Since a + b = sum <=> b = sum - a.

Now, we have calculated b based on the current value of a.

The key insight here is that if b exists in the list of Numbers, it means there is a pair of numbers that sums up to sum, and that pair is [a, b].

By using the condition sum - num in Numbers, I am checking if the calculated value of b is present in the Numbers list. 
If yes, then we have found a valid pair (a, b) that sums up to the desired sum.

We don't need to continue iterating through all possible values of b because you've found a match based on the presence of b in the Numbers list.
"""
