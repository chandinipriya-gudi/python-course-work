Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
lis=[]
lis=[1,2.3,"asd",1+8j,[123,23],(123,"asd"),{123,"asd"},False,True,{A:1,B:2}]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lis=[1,2.3,"asd",1+8j,[123,23],(123,"asd"),{123,"asd"},False,True,{A:1,B:2}]
NameError: name 'A' is not defined
lis=[1,2.3,"asd",1+8j,[123,23],(123,"asd"),{123,"asd"},False,True,{"A":1,"B":2}]
lis
[1, 2.3, 'asd', (1+8j), [123, 23], (123, 'asd'), {'asd', 123}, False, True, {'A': 1, 'B': 2}]
l=[1, 2.3, 'asd', (1+8j), [123, 23], (123, 'asd'), {'asd', 123}, False, True, {'A': 1, 'B': 2}]
l
[1, 2.3, 'asd', (1+8j), [123, 23], (123, 'asd'), {'asd', 123}, False, True, {'A': 1, 'B': 2}]
a=list()
a
[]
l
[1, 2.3, 'asd', (1+8j), [123, 23], (123, 'asd'), {'asd', 123}, False, True, {'A': 1, 'B': 2}]
id(l)
4443713024
l.append(12)
l
[1, 2.3, 'asd', (1+8j), [123, 23], (123, 'asd'), {'asd', 123}, False, True, {'A': 1, 'B': 2}, 12]
id(l)
4443713024
names=["abhi","pujith","prannnu"]
names
['abhi', 'pujith', 'prannnu']
names*2
['abhi', 'pujith', 'prannnu', 'abhi', 'pujith', 'prannnu']
names[1:2]
['pujith']
names[1:]
['pujith', 'prannnu']
names+name[1:]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    names+name[1:]
NameError: name 'name' is not defined. Did you mean: 'names'?
names+names[1:]
['abhi', 'pujith', 'prannnu', 'pujith', 'prannnu']
names
['abhi', 'pujith', 'prannnu']




names[-1]
'prannnu'
names[1:3]
['pujith', 'prannnu']
names[:]
['abhi', 'pujith', 'prannnu']
names[-1:-4]
[]
names[-1:-3:]
[]
names[-1:-3:-1]
['prannnu', 'pujith']
names[-1:-4:-1]
['prannnu', 'pujith', 'abhi']
sorted(names)
['abhi', 'prannnu', 'pujith']
names(reverse=True)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names(reverse=True)
TypeError: 'list' object is not callable
sorted(names,reverse=True)
['pujith', 'prannnu', 'abhi']
max(names)
'pujith'
min(names)
'abhi'
names.sort()
\
names.sort()
names.append("fghjkloiuhgf")
names
['abhi', 'prannnu', 'pujith', 'fghjkloiuhgf']
names.insert(0,"arya")
names
['arya', 'abhi', 'prannnu', 'pujith', 'fghjkloiuhgf']
names.extend(["sadf","sdwfe"])
names
['arya', 'abhi', 'prannnu', 'pujith', 'fghjkloiuhgf', 'sadf', 'sdwfe']
names.pop()
'sdwfe'
names
['arya', 'abhi', 'prannnu', 'pujith', 'fghjkloiuhgf', 'sadf']
names.delete("abhi")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    names.delete("abhi")
AttributeError: 'list' object has no attribute 'delete'
names.remove("abhi")
names
['arya', 'prannnu', 'pujith', 'fghjkloiuhgf', 'sadf']
names.pop[0]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    names.pop[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
names.pop(0)
'arya'
names
['prannnu', 'pujith', 'fghjkloiuhgf', 'sadf']
names.pop(2,3)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    names.pop(2,3)
TypeError: pop expected at most 1 argument, got 2
>>> names.pop()
'sadf'
>>> nmmes.pop()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    nmmes.pop()
NameError: name 'nmmes' is not defined. Did you mean: 'names'?
>>> nmaes.pop()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    nmaes.pop()
NameError: name 'nmaes' is not defined. Did you mean: 'names'?
>>> names
['prannnu', 'pujith', 'fghjkloiuhgf']
>>> names.pop()
'fghjkloiuhgf'
>>> names
['prannnu', 'pujith']
>>> names.clear()
>>> names
[]
>>> names.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    names.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
>>> names
[]
>>> names.append(1)
>>> names
[1]
>>> names.append("abhinay")
>>> names.append("prannnu")
>>> names
[1, 'abhinay', 'prannnu']
>>> nmaes.pop()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nmaes.pop()
NameError: name 'nmaes' is not defined. Did you mean: 'names'?
>>> names.pop()
'prannnu'
>>> names
[1, 'abhinay']
>>> names.append("PRANNNU")
>>> names
[1, 'abhinay', 'PRANNNU']
>>> names.remove(1)
>>> names
['abhinay', 'PRANNNU']
>>> names.replace("PRANNU","pran")
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    names.replace("PRANNU","pran")
AttributeError: 'list' object has no attribute 'replace'
>>> l=[1,2,3]
>>> m=l.copy()
>>> m
[1, 2, 3]
>>> l
[1, 2, 3]
>>> m.append(5)
>>> m
[1, 2, 3, 5]
>>> l
[1, 2, 3]
