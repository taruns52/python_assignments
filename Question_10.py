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
n = int(input("Enter any number to dispaly Expression-1"))
n = n//2 + 1 if n%2!=0 else n//2
k = 1
for j in range(n,0,-1):
    print(j*'*' + k*'-' + j*'*')
    k += 2

k = k-4
for j in range(2,n+1):
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
n = int(input("Enter any number to dispaly Expression-4"))

n = n//2 + 1 if n%2!=0 else n//2
k = 1
for j in range(n,0,-1):
    print(j*'*' + k*'-' + j*'*')
    k += 2

k = k-4
for j in range(2,n+1):
    print(j*'*' + k*'-' + j*'*')
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
n = int(input("Enter any number to dispaly Expression-3"))
for i in range(1,n+1):  
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

n = int(input("Enter any number to dispaly Expression-4"))
for i in range(n+1):
    if i == 0 or i == n:
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
n =int(input('enter the no. of rows for Expression-5'))   #rows
k = 1
for i in range(n+1):
    for j in range(i):
        print(k, end=' ')
        k += 1
    print()