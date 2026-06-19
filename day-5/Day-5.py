Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
s="
SyntaxError: unterminated string literal (detected at line 1)
s=""
s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s*10
'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
\
s*100
'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
"-"*10
'----------'
"------------------------"*20
'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'


print("INDEXING")
INDEXING
s
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s[0]
'A'
s[-1]
'Z'
s[0:1]
'A'
s[::2]
'ACEGIKMOQSUWY'
s[;;-1]
SyntaxError: invalid syntax
s[::-1]
'ZYXWVUTSRQPONMLKJIHGFEDCBA'
s[1]
'B'
s[2]
'C'
s[3]
'D'
s[4]
'E'
s[5
  s[8]
  
SyntaxError: '[' was never closed
s[99]
  
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s[99]
IndexError: string index out of range
s[20]
  
'U'
a=["ABHI", "Arya"]
  
a
  
['ABHI', 'Arya']
"ABHI" in a
  
True
"ABHI"
  
'ABHI'
a
  
['ABHI', 'Arya']
a[:4:]
  
['ABHI', 'Arya']
a[:4]
  
['ABHI', 'Arya']
b="ABHI PRANNNU"
  
b
  
'ABHI PRANNNU'
b[0:4:]
  
'ABHI'
b[-1:-8:-1]
  
'UNNNARP'


len(b)
  
12
ord(b)
  
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    ord(b)
TypeError: ord() expected a character, but string of length 12 found
ord(b)
  
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ord(b)
TypeError: ord() expected a character, but string of length 12 found
ord("A")
  
65
ord("Z")
  
90
chr("A")
  
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    chr("A")
TypeError: 'str' object cannot be interpreted as an integer
chr(40)
  
'('
char(23)
  
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    char(23)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(34)
  
'"'
sorted (b)
  
[' ', 'A', 'A', 'B', 'H', 'I', 'N', 'N', 'N', 'P', 'R', 'U']
min(b)
  
' '
max(b)
  
'U'
b.upper()
  
'ABHI PRANNNU'
b.lower()
  
'abhi prannnu'
b.swapcase()
  
'abhi prannnu'
b.captialize()
  
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    b.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
b.captilize()
  
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
b.capitalize()
  
'Abhi prannnu'
b.title()
  
'Abhi Prannnu'
s.center(60,"-")
  
'-----------------ABCDEFGHIJKLMNOPQRSTUVWXYZ-----------------'
s.center(100,"&")
  
'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&ABCDEFGHIJKLMNOPQRSTUVWXYZ&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
s.ljust(60,"*")
  
'ABCDEFGHIJKLMNOPQRSTUVWXYZ**********************************'
s.rjust(100,"_")
  
'__________________________________________________________________________ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"12345".zfill(10)
  
'0000012345'
"44".zfill(4)
  
'0044'



s.find("f")
  
-1
s
  
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s.find("K")
  
10
s.find("A")
  
0
s.rfind("Z")
  
25
len(s)
  
26
s.rfind("A")
  
0
s.index("A")
  
0
s.index("Z")
  
25
z="AAAAAAAABCDEGDSSAXWW"
  
z
  
'AAAAAAAABCDEGDSSAXWW'
z.count("A")
  
9
z.count("S")
  
2
z is alpha
  
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    z is alpha
NameError: name 'alpha' is not defined
z.isalpha
  
<built-in method isalpha of str object at 0x10aba3bb0>


 s.splitlines()
  
SyntaxError: unexpected indent
s=["abhi","pran"]
  
s
  
['abhi', 'pran']
"<3".join(s)
  
'abhi<3pran'

"_@_".join(s)
  
'abhi_@_pran'







s=["asdkjh","asdfds","sdfres","oiusdytgfsvb"]
  
s
  
['asdkjh', 'asdfds', 'sdfres', 'oiusdytgfsvb']
s.partition("a")
  
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.partition("a")
AttributeError: 'list' object has no attribute 'partition'
s.partition("a")
  
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s.partition("a")
AttributeError: 'list' object has no attribute 'partition'
>>> s="hello      worls      "
...   
>>> s
...   
'hello      worls      '
>>> s.strip()
...   
'hello      worls'
>>> s.lstrip()
...   
'hello      worls      '
>>> s.rstrip()
...   
'hello      worls'
>>> s.trim()
...   
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    s.trim()
AttributeError: 'str' object has no attribute 'trim'. Did you mean: 'strip'?
>>> 
>>> 
>>> s.replace("hello","abhi")
...   
'abhi      worls      '
>>> s.maketrans("aeiou","****")
...   
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s.maketrans("aeiou","****")
ValueError: the first two maketrans arguments must have equal length
>>> s.maketrans("aeiou","*****")
...   
{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
>>> s.translate(s.maketrans("aeiou","*****"))
...   
'h*ll*      w*rls      '
>>> 

>>> 
>>> s="shhshsjsjs ❤️"
...   
>>> s
...   
'shhshsjsjs ❤️'
>>> s.encode()
...   
b'shhshsjsjs \xe2\x9d\xa4\xef\xb8\x8f'
>>> s.decode()
...   
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> s=b'shhshsjsjs \xe2\x9d\xa4\xef\xb8\x8f'
... 
>>> s
...   
b'shhshsjsjs \xe2\x9d\xa4\xef\xb8\x8f'
>>> s.decode()
...   
'shhshsjsjs ❤️'
