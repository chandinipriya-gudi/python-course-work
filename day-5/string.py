Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
>>> s.startswith('py')
True
>>> s.endswith('ing')
True
>>> 'abc'.isalpha()
True
>>> 'abc1'.isalpha()
False
>>> 'abc def'.isalpha()
False
>>> 'ADVdxsx'.isalpha()
True
>>> 'sswscfvrdv'.isalnum()
True
>>> 'asxdwe5re46555gt'.isalnum()
True
>>> 'qwdecsr@1321edws'.isalnum()
False
>>> 'fersvcd'.isupper()
False
>>> 'WCDEDCAED'.isupper()
True
>>> 'DCEWDCSX'.islower()
False
>>> 'fcrwsdc'.islower()
True
>>> '     '.isspace()
True
>>> 'Ac An '.istitle()
True
>>> 'my_var'.isidentifier()
True
>>> '2345'.isdecimal()
True
>>> 'iilcwsuij'.isdecimal()
False
>>> '2342346.343'.isdecimal
<built-in method isdecimal of str object at 0x000001EBB6EDD4F0>
>>> KeyboardInterrupt
>>> '2342346.343'.isdecimal()
False
>>> KeyboardInterrupt
>>> '2342346.343'.isdigit()
False
>>> '23456'.isdigit()
True
