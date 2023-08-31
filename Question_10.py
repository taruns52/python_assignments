'''
Expression-1:
**_**
*___*
_____ 
*___*
**_**

'''
print("Expression-1")
global k 

k = 1
for j in range(2,-1,-1):
    print(j*'*' + k*'-' + j*'*')
    k += 2

k = 3
for j in range(1,3):
    print(j*'*' + k*'-' + j*'*')
    k -= 2


'''
Expression - 2:
__*__ 
_***_ 
***** 
_***_ 
__*__
'''
print("\nExpression-2")

k = 1
for j in range(2,-1,-1):
    print(j*'-' + k*'*' + j*'-')
    k += 2

k = 3
for j in range(1,3):
    print(j*'-' + k*'*' + j*'-')
    k -= 2



'''
Expression - 3:
* 
**
*_* 
*__* 
*****
'''
print("\nExpression-3")
for i in range(1,6):  
    if i%4 == 0 or i%3==0:
        print('*'+'-'*(i-2)+'*')
    else:
        print('*'*i)



'''
Expression - 4:
***** 
*___* 
*___* 
*___* 
*****
'''

print("\nExpression-4")
for i in range(6):
    if i%5 == 0:
        print('*'*5)
    else:
        print('*---*')




'''
Expression - 5:
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
print("\nExpression-5")
k = 1
for i in range(6):
    for j in range(i):
        print(k, end=' ')
        k += 1
    print()