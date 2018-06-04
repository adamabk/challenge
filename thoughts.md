```
>>> sr = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
>>> pattern = r'(\([0-9]\,\s[0-9]\))'
>>> re.findall(pattern, sr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 're' is not defined
>>> import re
>>> re.findall(pattern, sr)
['(0, 0)', '(1, 3)', '(4, 4)', '(4, 2)', '(4, 2)', '(0, 1)', '(3, 2)', '(2, 3)', '(4, 1)']
>>> for i in re.findall(pattern, sr):
...     print(i)
...
(0, 0)
(1, 3)
(4, 4)
(4, 2)
(4, 2)
(0, 1)
(3, 2)
(2, 3)
(4, 1)
>>> import ast
>>> for i in re.findall(pattern, sr):
...     i = ast.literal_eval(i)
...     print(type(i))
...
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
<class 'tuple'>
>>>
```
