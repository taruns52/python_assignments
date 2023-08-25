# 6. Find how many number of times the substring occurs in the given string.

# > Input:  string = “PQRQRQRQ” substring = “QRQ”

# > Output: 3


string = "PQRQRQRQ" 
substring = "QRQ"

i,count, str_len = 0,0, len(string)-1
while i < str_len :
    
    if string[i] == substring [0]:
        k = i+1
        temp_count = 1

        for j in range(1,len(substring)):
            if substring[j] == string[k]:
                temp_count += 1
            k +=1
        
        print('temp_count', temp_count)
        if temp_count == len(substring):
            count += 1
    i += 1

print(count)