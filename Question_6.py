# 6. Find how many number of times the substring occurs in the given string.

# > Input:  string = “PQRQRQRQ” substring = “QRQ”

# > Output: 3


string = "PQRQRQRQ" 
substring = "QRQ"

i,count, str_len = 0,0, len(string)-1
while i < str_len :
    
    if string[i] == substring [0]:
        temp_count = 1                  # temp_count is set 1 bcoz one char of str and sub str is already matched  

        for j in range(1,len(substring)):       # Looping through substring 
            if substring[j] == string[j+i]:     # Checking if the char of str and substr is matching or not
                temp_count += 1                 # If matched then increment count
        
        if temp_count == len(substring):        # Filtering as there can be some chars of str do match with substr but not all are matching so we cant count those as full match count 
            count += 1
    i += 1

print(count)


# Better Approach:

sub_str_len = len(substring)
str_len = len(string)

count = 0

for i in range(str_len - sub_str_len + 1):
    if string[i:i+sub_str_len] == substring:
        count+=1

print('Total occurance of sub-string',substring,'in',string,'is',count)
