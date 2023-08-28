# 6. Find how many number of times the substring occurs in the given string.

# > Input:  string = “PQRQRQRQ” substring = “QRQ”

# > Output: 3

string = "PQRQRQRQ" 
substring = "QRQ"

sub_str_len = len(substring)
str_len = len(string)

count = 0

for i in range(str_len - sub_str_len + 1):
    if string[i:i+sub_str_len] == substring:
        count+=1

print('Total occurance of sub-string',substring,'in',string,'is',count)
