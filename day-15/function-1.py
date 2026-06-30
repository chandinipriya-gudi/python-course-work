'''def iseven(num):
    if num%2==0:
        return "even number"
    else:
        return "odd number"
print(iseven(14))
print(iseven(7))
print(iseven(6))
print(iseven(1))

n=int(input())#prime or not
def isprime(n):
    for i in range(2,n):
        if n%2==0:
            return f"{n}-not a prime number"
    return f"{n}prime number"
print(isprime(n))

def isprime(n):#all primes from 1 to n
    for num in range(2,n+1):
        for i in range(2,num):
            if num%2==0:
                break
        else:
            print(num,end=' ')

isprime(50)

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of {n}:{fact}")

factorial(5)
factorial(6)
factorial(8)
'''
