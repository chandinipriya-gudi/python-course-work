Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
t
()
a=tuple()
a
()
type(a)
<class 'tuple'>
t=(1,2,3,4,5,6,7,8,9,10)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t=(1,)
t
(1,)
t
(1,)
t=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t+(1,2,3)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3)
t*3
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t/3
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t/3
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
t[0]
1
t[-1]
10
t[1:3]
(2, 3)
t[-1::-2]
(10, 8, 6, 4, 2)
t[-1::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
t
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
t[::-1]
(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
sum(t)
55
any(1,2,3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    any(1,2,3)
TypeError: any() takes exactly one argument (3 given)
count(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    count(1)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count(1)
1
t=(1,2,3,4,5,6,7,89,7,1,2,3,4,5,1,2,3,4,5)
t
(1, 2, 3, 4, 5, 6, 7, 89, 7, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t.count(2)
3
t.add()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    t.add()
AttributeError: 'tuple' object has no attribute 'add'
t.sum()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    t.sum()
AttributeError: 'tuple' object has no attribute 'sum'
sum(t)
154
t[-1:-5:-1]
(5, 4, 3, 2)
t[::-1]
(5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 7, 89, 7, 6, 5, 4, 3, 2, 1)
5 in t
True
99 in t
False
99 not in t
True
1 not in t
False
t.index(89)
7
sorted(t)
[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 89]
t.sorted()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.sorted()
AttributeError: 'tuple' object has no attribute 'sorted'
sorted(t)
[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 7, 89]
min(t)
1
max(t)
89
min(t)+max(t)
90
t
(1, 2, 3, 4, 5, 6, 7, 89, 7, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)



d={
    1:2,
    2:3'
    
SyntaxError: unterminated string literal (detected at line 3)
d={
    1:2,
    2:3'
    
SyntaxError: unterminated string literal (detected at line 3)

d={
    1:2,
    2:3,
    3:4}
    
d
    
{1: 2, 2: 3, 3: 4}
type(d)
    
<class 'dict'>
d[1]=2
    
d[2]=6
    
d
    
{1: 2, 2: 6, 3: 4}
d[4]=8
    
d[9]=9
    
d
    
{1: 2, 2: 6, 3: 4, 4: 8, 9: 9}
d[9]
    
9
d[1]
    
2
d.get(22)
    
d.get(50,"NOT AVALIBLE IN DICT)
      
SyntaxError: unterminated string literal (detected at line 1)
d.get(50,"NOT AVALIBLE IN DICT")
      
'NOT AVALIBLE IN DICT'
d
      
{1: 2, 2: 6, 3: 4, 4: 8, 9: 9}
d[5]="sds"
      
d[6]="skdjhgfdvshjdfc"
      
d[7]=23456789
      
d[8]="asdfdsdfrerfdsd"
      
d
      
{1: 2, 2: 6, 3: 4, 4: 8, 9: 9, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd'}
d[10]
      
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    d[10]
KeyError: 10
d[9]=1
      
d[]10=10
      
SyntaxError: invalid syntax
d[10]=10
      
d
      
{1: 2, 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10}
d[10]
      
10
d[11]=[1,2,3,4,5]
      
d
      
{1: 2, 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10, 11: [1, 2, 3, 4, 5]}
d[-1]
      
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d[-1]
KeyError: -1
>>> d[11]
...       
[1, 2, 3, 4, 5]
>>> d[11,1]
...       
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d[11,1]
KeyError: (11, 1)
>>> d[11][1]
...       
2
>>> d[11][0]
...       
1
>>> d[11][1][::-1]
...       
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    d[11][1][::-1]
TypeError: 'int' object is not subscriptable
>>> d[11][::-1]
...       
[5, 4, 3, 2, 1]
>>> d.pop
...       
<built-in method pop of dict object at 0x106bd3140>
>>> d.pop()
...       
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.pop(11)
...       
[1, 2, 3, 4, 5]
>>> d
...       
{1: 2, 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10}
>>> id
...       
<built-in function id>
9
>>> d
...       
{1: 2, 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10}0
>>> 

>>> d(id)
...       
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    d(id)
TypeError: 'dict' object is not callable
>>> id(d)
...       
4408029504
>>> d[1]=["asd",1]
...       
>>> d
...       
{1: ['asd', 1], 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10}
>>> id(d)
...       
4408029504
>>> d
...       
{1: ['asd', 1], 2: 6, 3: 4, 4: 8, 9: 1, 5: 'sds', 6: 'skdjhgfdvshjdfc', 7: 23456789, 8: 'asdfdsdfrerfdsd', 10: 10}
