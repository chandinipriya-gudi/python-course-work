#a
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i == m:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#b
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or i == m or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#c
'''
n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
        if j==0  or i==0  or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#d
'''
n=int(input("Enter number:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0  or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#e
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0  or i==0 or i == m or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#f
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0  or i==0 or i == m :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#g
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or(i==n-1 and j<=m) or (j==m and i>=m) or(i==m and j>=m) or (j==n-1 and i>=m): 
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#h
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i == m:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#i
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j == m:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#j
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m or (i==n-1 and j<=m )or (j==0 and i>=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#y
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and i<=m) or i+j==n-1 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#k
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or (i==m and j<=m) or (i+j==n-1 and i<=m) or (i==j and i>=m):
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#t
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if   i==0 or j==m:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#u
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#l
'''
n=int(input("Enter number:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#w
'''
n=int(input())
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or (c==r and r>=m) or (c+r==n-1 and r>=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#m
'''
n=int(input())
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or (c==r and r<=m) or (c+r==n-1 and r<=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#n
'''
n=int(input())
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or c==r   :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#p
'''
n=int(input("Enter the size:"))
m=n//2
for i in range(n):                     
    for j in range(n):
        if j==0 or (j==n-1 and i<=m) or i==0 or i==m:     
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()
'''
#s
'''
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if  (i==0 )or i==n-1  or (j==0 and i<=m) or i==m  or (j==n-1 and i>=m) :   #S 
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()
'''
#q
'''
n=int(input())
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or (i==j and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#v
'''
n=int(input(":"))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==n+m-1 and i>=m):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#X
'''
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:     
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()
'''
#z
'''
n=int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):                   
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ' ,end=' ')
    print()
'''
#r
#R
n=int(input('Enter Size: '))
for i in range(n):
    for j in range(n):
        if j==0 or (j==n-1 and i<=n//2) or i==0 or i==n//2 or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
