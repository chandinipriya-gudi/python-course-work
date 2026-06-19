Python 3.14.5 (v3.14.5:5607950ef23, May 10 2026, 07:38:09) [Clang 21.0.0 (clang-2100.0.123.102)] on darwin
Enter "help" below or click "Help" above for more information.
 print("STRING TESTING")
 
SyntaxError: unexpected indent
print("STRING TESTING")
STRING TESTING
s='python programming'
s
'python programming'
s.startswith(py)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.startswith(py)
NameError: name 'py' is not defined
s.startswith("py")
True
s.endswith("ing")
True


s.endswith("iou")
False
s.isaplpha()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s.isaplpha()
AttributeError: 'str' object has no attribute 'isaplpha'. Did you mean: 'isalpha'?
s.isaplha
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.isaplha
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
s.isalpha()
False
"abc123".isalpha()
False
"123".isnum()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    "123".isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
123.isnum()
SyntaxError: invalid syntax
123.isalnum()
SyntaxError: invalid syntax
"123".isalnum()
True
s="123456"
s
'123456'
s.isalnum()
True
s.isalpha()
False
s="23edsw2345re34"
s
'23edsw2345re34'
s.isalnum()
True
s
'23edsw2345re34'
s.isalpha()
False
a="sdfe"
a
'sdfe'
a.upper()
'SDFE'
a.isupper()
False
s="jdhgsh shdgsh sjdhytgf"
s
'jdhgsh shdgsh sjdhytgf'
s.isspace()
False
s="    "
s
'    '
s.isspace()
True
s.istitle()
False
>>> s="Sdfdvbh Dduhs"
>>> s
'Sdfdvbh Dduhs'
>>> s.istitle()
True
>>> s="wedfdswed1234!@#"
>>> s
'wedfdswed1234!@#'
>>> s.isidentifier()
False
>>> s="if"
>>> s
'if'
>>> s.isidentifer()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.isidentifer()
AttributeError: 'str' object has no attribute 'isidentifer'. Did you mean: 'isidentifier'?
>>> s.isidentifier()
True
>>> a="45678.8765"
>>> a.isdecimal()
False
>>> a="23456"
>>> a
'23456'
>>> a.isdecimal()
True
>>> "123".isdigit()
True
>>> s
'if'
>>> s.startswith("if")
True
>>> s="a,sjhdgfcsvj sdhytfgwhsjduh s"
>>> s
'a,sjhdgfcsvj sdhytfgwhsjduh s'
>>> a=123.12
>>> a.isdecimal
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a.isdecimal
AttributeError: 'float' object has no attribute 'isdecimal'
>>> a.isdecimal()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.isdecimal()
AttributeError: 'float' object has no attribute 'isdecimal'
>>> s=list(int,input().split())
1
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s=list(int,input().split())
TypeError: list expected at most 1 argument, got 2
2
>>> s
'a,sjhdgfcsvj sdhytfgwhsjduh s'
>>> list=[123,'asds','asdjhfbd',234]
>>> list
[123, 'asds', 'asdjhfbd', 234]
>>> list[0]
123
>>> s=[]
>>> s
[]
>>> s=list()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s=list()
TypeError: 'list' object is not callable
