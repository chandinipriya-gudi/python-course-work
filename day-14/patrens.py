'''n=int(input())#A
for r in range(n):
    for c in range(n):
        if r==0 or r==n//2 or c==0 or c==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())#B
for r in range(n):
    for c in range(n):
        if r==0 or r==n//2 or c==0 or c==n-1 or r==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())#X
for r in range(n):
    for c in range(n):
        if r==c or r==n-c-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())#G
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or r==0 or (r==n-1 and c<=m) or (r>=m and c==m) or (c>=m and r==m) or (r>=m and c==n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())#H
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or r==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
n=int(input())#I
m=n//2
for r in range(n):
    for c in range(n):
        if r==0 or r==n-1 or c==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    
n=int(input())#J
m=n//2
for r in range(n):
    for c in range(n):
        if r==0 or (r==n-1 and c<=m) or c==m or (c==0 and r>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
   
n=int(input())#Y
m=n//2
for r in range(n):
    for c in range(n):
        if (r==c and r<=m)or r+c==n-1  :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
   
n=int(input())#k
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or (r==m and c<=m)or (c+r==n-1 and r<=m) or (c==r and c>=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())#m
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or (c==r and r<=m) or (c+r==n-1 and r<=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
n=int(input())#w
m=n//2
for r in range(n):
    for c in range(n):
        if c==0 or c==n-1 or (c==r and r>=m) or (c+r==n-1 and r>=m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
