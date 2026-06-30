'''def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("inner function: ",n)
    inner()
    print("outer function: ",n)
display()

def display():
    course='java fullstack'
    print("starting:",course)
    def change():
        nonlocal course
        course='python fullstack'
        print("updated:",course)
    change()
    print("final course:",course)
display()

#int,float,complex,str,tuple,bool =>imm=>values
#list,dict,set=>reference
def update(n):
    n=10
    print('Inside: ',n)
n=20
update(n)
print('Outside: ',n)


def update(n):
    n=4.5
    print('Inside: ',n)
n=2.3
update(n)
print('Outside: ',n)

def update(n):
    n=4+3j
    print('Inside: ',n)
n=2+3j
update(n)
print('Outside: ',n)

def update(n):
    n=n.upper()
    print('Inside: ',n)
n='python'
update(n)
print('Outside: ',n)

def update(n):
    n.append(40)
    print('Inside: ',n)
n=[10,20,30]
update(n)
print('Outside: ',n)


def update(n):
    n=n+(40,50)
    print('Inside: ',n)
n=(10,20,30)
update(n)
print('Outside: ',n)


def update(n):
    n.update({40,50})
    print('Inside: ',n)
n={10,20,30}
update(n)
print('Outside: ',n)

def update(n):
    n.update({4:40,5:50})
    print('Inside: ',n)
n={1:10,2:20,3:30}
update(n)
print('Outside: ',n)

def update(n):
    n=True
    print('Inside: ',n)
n=False
update(n)
print('Outside: ',n)

def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

def display(n):
    if n>10:
        return
 
    display(n+1)
    print(n)
display(1)
'''

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind],end='')
    display(s,ind+1)
    print(s[ind],end='')
display("python programming",0)

