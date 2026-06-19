Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> t=()
>>> t=tuple()
>>> type(t)
<class 'tuple'>
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> t=(1,1,1)
>>> t
(1, 1, 1)
>>> t=(1,)
>>> t
(1,)
>>> t=
SyntaxError: invalid syntax
>>> t=(1,1,1)
>>> t
(1, 1, 1)
>>> (1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
>>> (1,2,3)*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t=(1,2,3,4,5,6,78,90)
>>> t[3]
4
>>> t[-1]
90
>>> t[-4]
5
>>> t[:4]
(1, 2, 3, 4)
>>> t[3:8]
(4, 5, 6, 78, 90)
>>> t[::-1]
(90, 78, 6, 5, 4, 3, 2, 1)
>>> t[-1:-5:-1]
(90, 78, 6, 5)
>>> 90 in t
True
>>> 30 in t
False
>>> 4 not in t
False
>>> t.index(4)
3
t.count(6)
1
sorted(t)
[1, 2, 3, 4, 5, 6, 78, 90]
max(t)
90
min(t)
1
max(t)
90
sum(t)
189
len(t)
8
any(1,x,b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    any(1,x,b)
NameError: name 'x' is not defined
any(1,a,b)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    any(1,a,b)
NameError: name 'a' is not defined
any(1,87,67)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    any(1,87,67)
TypeError: any() takes exactly one argument (3 given)

