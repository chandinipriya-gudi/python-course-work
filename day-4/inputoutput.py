Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
chandini
name
'chandini'
name=input("enter your name")
enter your namechandini
name
'chandini'
age=int(input("enter your age:"))
enter your age:21
age
21
gap=float(input("enter your gap:"))
enter your gap:7.3
gap
7.3
name=list(input("enter the names")slip())
SyntaxError: invalid syntax. Perhaps you forgot a comma?
name=list(input("enter the names").slipt())
enter the nameschandini priya varshi
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    name=list(input("enter the names").slipt())
AttributeError: 'str' object has no attribute 'slipt'. Did you mean: 'split'?
name=list(map(input("enter the names").slipt()))
enter the nameschandini priya varshi
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    name=list(map(input("enter the names").slipt()))
AttributeError: 'str' object has no attribute 'slipt'. Did you mean: 'split'?
name=list(map(input("enter the names").split()))
enter the nameschandini priya varshi
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name=list(map(input("enter the names").split()))
TypeError: map() must have at least two arguments.
name=list((input("enter the names").split()))
enter the nameschandini priya varshi
names
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
name=list(input("enter the names").split())
enter the nameschandini varshi
name
['chandini', 'varshi']
['chandini', 'varshi']
['chandini', 'varshi']
name=tuple(input("enter the names").split())
enter the nameschandini varshi
name
('chandini', 'varshi')
name=set(input("enter the names").split())
enter the nameschandini varshi
name
{'chandini', 'varshi'}
marks
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    marks
NameError: name 'marks' is not defined. Did you mean: 'vars'?
marks=list(map(int,input().split()))
23 24 23 25
SyntaxError: multiple statements found while compiling a single statement
marks=list(map(int,input().split()))
23 24
SyntaxError: multiple statements found while compiling a single statement
marks = list(map(int,input().split()))
2 3
marks
[2, 3]
marks = list(map(int, input().split()))
23 24
marks
[23, 24]
marks=set(map(int(input().split()))
          23 24
          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
marks=set(map(int,input().split()))
          
23 24
marks
          
{24, 23}
marks=tuple(map(int,input().split()))
          
23 24
marks
          
(23, 24)
e=eval
          
e=eval(input())
          
2
e
          
2
typr(e)
          
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    typr(e)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(e)
          
<class 'int'>
e=eval(input))
SyntaxError: unmatched ')'
SyntaxError: unmatched ')'
SyntaxError: invalid syntax
a='python'
b=10
c=23.9
priny
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    priny
NameError: name 'priny' is not defined. Did you mean: 'print'?
print(a,b,c)
python 10 23.9
print'a='a,'b='b,'c='c)
SyntaxError: unmatched ')'
print('a='a,'b='b,'c='c)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a=',a,'b=',b,'c=',c)
a= python b= 10 c= 23.9
print('a=',a,'b=',b,'c=',c,sep='')
a=pythonb=10c=23.9
print('a=',a,'b=',b,'c=',c,sep=',')
a=,python,b=,10,c=,23.9
print('a=',a,'b=',b,'c=',c,sep='/n')
a=/npython/nb=/n10/nc=/n23.9
print('a=',a,'b=',b,'c=',c,sep='\n')
a=
python
b=
10
c=
23.9
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	python	b=	10	c=	23.9
>>> print('a=',a,'b=',b,'c=',c,sep='\n\n\n')
a=


python


b=


10


c=


23.9
>>> print('a=',a,'b=',b,'c=',c,end='@#$')
a= python b= 10 c= 23.9@#$
>>> print('a=',a,'b=',b,'c=',c,end='\n\n\n')
a= python b= 10 c= 23.9


>>> print(f'a={a} b={b} c={c}')
a=python b=10 c=23.9
>>> print(f'a={b} b={b} c={a}')
a=10 b=10 c=python
>>> print('a=%s b=%d c=%f'%(a,b,c))
a=python b=10 c=23.900000
>>> print('a={} b={} c={}'.format(a,b,c))
a=python b=10 c=23.9
>>> print('a={3} b={0} c={1}'.format(a,b,c))
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print('a={3} b={0} c={1}'.format(a,b,c))
IndexError: Replacement index 3 out of range for positional args tuple
>>> print('a={2} b={0} c={1}'.format(a,b,c))
a=23.9 b=python c=10
