'''
Here you are given two series input one is arithmetic progression (A.P.) and another one is geometric progress (G.P.). 
In which, one of the terms is wrong. Your task is to find out the wrong term and replace it with correct term.

> Arithmetic progression: An arithmetic sequence is a sequence of numbers where the differences between every two consecutive terms is the same.
For example: 1, 2, 3, 4, 5, 6, 7, 8 is an A.P. as consecutive terms difference (2-1 = 3-2 = 4-3 = 5-4 = 6-5 = 7-6 = 8-7 = 1) is equal.

> Geometric progression: A geometric sequence is a special type of sequence where
 the ratio of every two successive terms is a constant.
 For example: 2, 4, 8, 16, 32, 64 is an G.P. ratio of every two successive (4/2 = 8/4 = 16/8 = 32/16 = 64/32 = 2) is constant.

> Input: One term wrong A.P. = [2, 5, 8, 11, 15, 17] One term wrong G.P. = [3, 9, 27, 81, 244, 729]
> Output: Correct A.P. = [2, 5, 8, 11, 14, 17] Correct G.P. = [3, 9, 27, 81, 243, 729]
'''
from math import sqrt

AP = [2, 5, 8, 11, 15, 17] 
def get_diff(AP):
    diff1 = AP[1] - AP[0]
    diff2 = AP[2] - AP[1]

    if diff1 == diff2:
        return diff1
    else:
        return AP[3] - AP[2]

        
diff = get_diff(AP)    
for i in range(1,len(AP)-1):
    if AP[i+1] - AP[i] != diff:
        AP[i] = (AP[i+1] + AP[i-1])//2

print("Correct Arithmetic Progression:",AP,"\n")


GP = [3, 9, 27, 81, 244, 729]
# GP = [2,4,8,16,32,64,128,255,512]
def get_ratio(GP):
    ratio1 = GP[1] / GP[0]
    ratio2 = GP[2] / GP[1]

    if ratio1 == ratio2:
        return ratio1
    else:
        return GP[3] / GP[2]

        
ratio = get_ratio(GP)    
for i in range(1,len(GP)-1):
    if GP[i+1] / GP[i] != ratio:
        GP[i] = round((GP[i+1] * GP[i-1])**0.5)

print('Correct Geometric Progresssion:',GP,'\n')


        