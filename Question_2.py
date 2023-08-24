# 2. You are given a list of person names. Your task is to find out the three most frequent and three least frequent names.

# Input:
# names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White']

# Output:
# o Names: ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
#             'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'] 
# o Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5]

# o The three most frequent name lenghts are:
# 6 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] 
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
# 2 names of length 8: ['Williams', 'Anderson']

# o The three least frequent name lenghts are:
# 2 names of length 7: ['Johnson', 'Jackson']
# 2 names of length 8: ['Williams', 'Anderson']
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']

names= ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
        'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White'] 

print('\n',names)

def name_len_dict(value):
    return [ name  for name in names if len(name) == value]      #values[0] = length of name , values[1] = count of names with same length


# o Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5]
name_lengths = [ len(name) for name in names ]
print("\nName lengths:", name_lengths,'\n')



# ---------------------------------------------------------------------------------------------------------

# o The three most frequent name lenghts are:
# 6 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] 
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
# 2 names of length 8: ['Williams', 'Anderson']

most_frequent_names = {}

# empty dictionary to store the frequency count for each element (key), 
# and its corresponding value is a list with all elements that have this key's value
for name in names:
   most_frequent_names[len(name)] = most_frequent_names.get(len(name), 0) + 1

# empty list to store ans in given format
ans = []

# loop through the keys and values from above dictionary
# so that we can required answer in required format 
for length in sorted(most_frequent_names.keys()):
    
    # get the number of times the current length occurs
    temp_names = name_len_dict(length)
    
    # appending to the list named ans to store and print required values
    ans.append([most_frequent_names[length], length,  temp_names ])

# printing data in required format
print('\nThe three most frequent name lenghts are:', '\n',)
for x in ans:
        print('{} names of length {}: {}'.format(x[0], x[1], x[2]))




# ---------------------------------------------------------------------------------------------------------

# o The three least frequent name lenghts are:
# 2 names of length 7: ['Johnson', 'Jackson']
# 2 names of length 8: ['Williams', 'Anderson']
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']

ans = []
rev_dict = sorted(most_frequent_names.items(), key = lambda x: x[1])[:3]


# loop through the keys and values from above dictionary
# so that we can required answer in required format 
for values in rev_dict:

    # get the number of times the current length occurs   
    temp_names = name_len_dict(values[0])   #values[0] = length of name , values[1] = count of names with same length

    # creating the dictioanry named ans to store ans
    ans.append([ values[1], values[0], temp_names ])
    

    # format of ans list -> [count of names of same length , length of name , [names] ]

# printing data in required format
print('\nThe three least frequent name lenghts are:\n',)
for x in ans:
    print('{} names of length {}: {}'.format( x[0],x[1],x[2]))
