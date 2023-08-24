
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

temp_dict = {}
solution = []

for num in Numbers:
    if sum-num in temp_dict and [num, sum-num] not in solution and [sum-num, num] not in solution:
        solution.append([sum-num, num])
    else:
        temp_dict[num] = False
print(solution)



# Appraoach :

'''
sum = 12
lets say temp_dict = { 9:False, 4:Fasle } and solution = [] after two iterations

next num is 8
    if sum-num in temp_dict and [num, sum-num] not in solution and [sum-num, num] not in solution:
    
    1st condition: True
        12 - 8 is 4 which in temp_dict
    2nd condition and 3rd condition : True
        as [4,8] and [8,4] are not present in solutions list

hence we will append [4,8] to solutions
'''