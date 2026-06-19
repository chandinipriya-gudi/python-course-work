'''i=1
while i<=10:
    print(i)
    i+=1

i=30
while i<=50:
    print(i)
    i+=2

i=10
while i>=1:
    print(i)
    i-=1

number=5
while True:
    n=int(input("guess the number:"))
    if number==n:
        print("your guess id correct")
        break
    else:
        print("incorrect,try again")
'''
l=[1,3,4,0,5,6,0,5,0,30,5,3,0,5,7,20,0,0,0,0,0,4]
while 0 in l:
    l.remove(0)
print(l)
