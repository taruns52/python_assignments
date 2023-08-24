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


# o Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5]
name_lengths = []
for i in names:
    name_lengths.append(len(i))
print("\nName lengths:", name_lengths,'\n')



# ---------------------------------------------------------------------------------------------------------

# o The three most frequent name lenghts are:
# 6 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] 
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']
# 2 names of length 8: ['Williams', 'Anderson']

dict = {}

# empty dictionary to store the frequency count for each element (key), 
# and its corresponding value is a list with all elements that have this key's value
for name in names:
    if len(name) in dict:
        dict[len(name)] += 1
    else:
        dict[len(name)] = 1


# empty dictionary to store ans in given format
ans = {}

# loop through the keys and values from above dictionary
# so that we can required answer in required format 
for length in sorted(dict.keys()):
    temp_names = []

    # get the number of times the current length occurs
    for name in names:
        if len(name)  == length:
            temp_names.append(name)
    
    # creating the dictioanry named ans to store ans
    ans[dict[length]] = {
        length: temp_names 
    }

# printing data in required format
print('\nThe three most frequent name lenghts are:', '\n',)
for x in ans:
    for key , value in ans[x].items():
        print('{} names of length {}: {}'.format(x, key, value))




# ---------------------------------------------------------------------------------------------------------

# o The three least frequent name lenghts are:
# 2 names of length 7: ['Johnson', 'Jackson']
# 2 names of length 8: ['Williams', 'Anderson']
# 4 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas']

ans = {}
rev_dict = sorted(dict.items(), key = lambda x: x[1])[:3]


# loop through the keys and values from above dictionary
# so that we can required answer in required format 
for values in rev_dict:
    temp_names = []

    # get the number of times the current length occurs
    for name in names:
        if len(name)  == values[0]:     #values[0] = length of name
            temp_names.append(name)
    
    # creating the dictioanry named ans to store ans
    ans[values[0]] = {
        values[1]: temp_names 
    }

    # format -> count of names of same length : { length of name : [names] }

# printing data in required format
print('\nThe three least frequent name lenghts are:\n',)
for x in ans:
    for key , value in ans[x].items():
        print('{} names of length {}: {}'.format( key,x, value))