''''from functools import reduce
l={'laptop':50000,'phone':100000,'charger':2000,'mouse':800}
res1=dict(map(lambda i:(i[0],i[l]+i[l]*0.18)l.items()))
print(resl)

def reels():
    l=['1..50','51..100','101..150','151..200','201..250','251..300']
    for i in range(len(l)):
        yield l[i]
r=reels()
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

def reels():
    l=['1..50','51..100','101..150','151..200','201..250','251..300']
    for i in range(len(l)):
        yield l[i]
r=reels()
while True:
    try:
        print(next(r))
    except StopIteration:
        break
   
def factors(n):
    return [i for i in range(1,n+1) if n%i==0]
def generators(res):
    for i in res:
        yield i
res=factors(30)
f=generators(res)
for i in range(len(res)):
    print(next(f))
 
'''
def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    elif n>2:
        res=[0,1]
        a,b=0,1
        for i in range(n-2):
            c=a+b
            res.append(c)
            a,b=b,c
        return res
def generators(res):
    for i in res:
        yield i
res=fib(13)
f=generators(res)
for i in range(len(res)):
    print(next(f))
