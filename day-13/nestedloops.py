'''n=int(input("enter the size:"))
m=int(input())
for r in range(n):
    for c in range(m):
        print('*',end=' ')
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(n):
        print(c%2,end=' ')
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(n):
        print((c+r)%2,end=' ')
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(n):
        if c+r>=n-1:
            print("1",end=' ')
        else:
            print("0",end=' ')

    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(n):
        print(int((c+r)>=n-1),end=' ')
    print()

n=int(input("enter the size:"))
count=1
for r in range(n):
    for c in range(n):
        print(str(count).zfill(2),end=' ')
        count+=1
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(r+1):
        print('*',end=' ')
    print()

n=int(input("enter the size:"))
count=1
for r in range(n):
    for c in range(r+1):
        print(str(count).zfill(2),end=' ')
        count+=1
    print()
   
n=int(input("enter the size:"))
for r in range(n):
    for c in range(n-r):
        print('*',end=' ')
    print()

n=int(input("enter the size:"))
ch=65
for r in range(n):
    for c in range(r+1):
        print(chr(ch),end=' ')
        ch+=1
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(n-r-1):
        print(' ',end=' ')
    for c in range(r+1):
        print('*',end=' ')
        
    print()

n=int(input("enter the size:"))
for r in range(n):
    for c in range(r):
        print(' ',end=' ')
    for c in range(n-r):
        print('*',end=' ')
        
    print()
    
n=int(input("enter the size:"))
for r in range(n):
    for c in range(n-r-1):
        print('',end=' ')
    for c in range(r+1):
        print('*',end=' ')
        
    print()
    '''
n=int(input("enter the size:"))
m=n//2
for r in range(n):
    
    if r<=m:
        for c in range(r+1):
            print('*',end=' ')
    else:
        for j in range(n-r):
            print('*',end=' ')
    print()


