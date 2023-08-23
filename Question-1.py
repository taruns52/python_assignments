# 1. Create a list of 10 numbers and show the 5 different operations options to the user on screen. The 5 different operations are as following,
# A. Length of the list
# B. Display first 3 numbers
# C. Display sum of odd numbers
# D. Number of duplicate numbers
# E. Display list without duplicate numbers

# Input:
# numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

# Output:
# If user select option A:
# o Length of the list: 10 

# If user select option B:
# o First 3 numbers: [2, 4, 5] 

# If use select option C:
# o Sum of odd numbers: 14 

# If user select option D:
# o Number of duplicate numbers: 2 # (2, 5 repeats in the list) 

# If user select option E:
# o List without duplicate numbers: [2, 3, 4, 12, 44, 1, 3]



# Solution:

numbers = [2, 4, 5, 2, 12, 44, 5, 1, 2, 3]

print("\n To select one of the following options just type 'A' or 'B' likewise....... \n")

print(" A. Length of the list")

print(" B. Display first 3 numbers")

print(" C. Display sum of odd numbers")

print(" D. Number of duplicate numbers")

print(" E. Display list without duplicate numbers \n")

choice = input("Type Here: ")

print("You have choosen option",choice)

# A. Length of the list
if choice.lower() == 'a' :
    print(f"Length of your list is {len(numbers)} ")

# B. Display first 3 numbers
elif choice.lower() == 'b':
    print ("Your first three numbers are ", end=" ")
    for x in numbers[:3]:
        print(x, end=" ")

# C. Display sum of odd numbers
elif choice.lower() == 'c':
    count=sum([i if i%2==1 else 0 for i in numbers])
    print('Sum of all odd numbers is:',count )

# D. Number of duplicate numbers  
elif choice.lower() == 'd':
    dups = []
    count = 0
    for num in numbers:
        if num in dups:
            count += 1
        dups.append(num)

    print ('Number of duplicates in arr',numbers,'is',count,'\n')


# E. Display list without duplicate numbers
elif choice.lower() == 'e':
    print('List without duplicate numbers:',list(set(numbers)) )
