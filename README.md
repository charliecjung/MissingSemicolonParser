# Duplicate Parser


This repository contains:

lint.py - checks for runs of repeated characters in a string. (Y/N confirmation for stripping away duplicates)
examples/test<#>.txt - test files which I tested my parser on.


## Program Usage:

```python3 lint.py
lint.py </path/to/unformatted/file> <path/to/linted/file>
```

```
Example:
python3 source/lint.py examples/test1.txt examples/test1_output.txt
Line [0]: aaaa

We have found 3 match(es) on this line.
Your line will be changed to this: a

Would you like to use the following changes (y/n)?
y
Your line has been changed to: |a
|

Line [1]: ;;;

We have found 2 match(es) on this line.
Your line will be changed to this: ;

Would you like to use the following changes (y/n)?
y
Your line has been changed to: |;
|

Linted file is located at <examples/test1_output.txt>. We hope to see you again! :)
```

Example:
test1.txt:
```
aaaa
;;;
bbbb
;;;
cccc
;;;;;
```

```
python3 lint.py
Please enter the file you would like to use: test1.txt
File name: test1.txt
Original Message: aaaa

file data: a

Line [0]: aaaa
We have found 4 match(es) on this line of the character: a
Your line will be changed to this: a

Would you like to use the following changes (y/n): n

Your line has remained: aaaa

Original Message: ;;;

file data: ;

Line [1]: ;;;
We have found 7 match(es) on this line of the character: ;
Your line will be changed to this: ;

Would you like to use the following changes (y/n): n

Your line has remained: ;;;

Original Message: bbbb

file data: b

Line [2]: bbbb
We have found 11 match(es) on this line of the character: b
Your line will be changed to this: b

Would you like to use the following changes (y/n): y

Your line has been changed to: b

Original Message: ;;;

file data: ;

Line [3]: ;;;
We have found 3 match(es) on this line of the character: ;
Your line will be changed to this: ;

Would you like to use the following changes (y/n): y

Your line has been changed to: ;

Original Message: cccc

file data: c

Line [4]: cccc
We have found 4 match(es) on this line of the character: c
Your line will be changed to this: c

Would you like to use the following changes (y/n): y

Your line has been changed to: c

Original Message: ;;;;;

file data: ;

Line [5]: ;;;;;
We have found 5 match(es) on this line of the character: ;
Your line will be changed to this: ;

Would you like to use the following changes (y/n): y

Your line has been changed to: ;

We have stripped duplicating characters from test1.txt. We hope to see you again! :)
Output:
```

```
aaaa
;;;
b
;
c
;
```
