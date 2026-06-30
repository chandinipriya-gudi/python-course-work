def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)
n=int(input("enter the n:"))
print(sumofn(9))
