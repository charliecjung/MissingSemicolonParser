<h1> Duplicate Parser </h1>

Hello everyone,


This repository contains:

lint.py - which checks for duplicate characters in a string. (Y/N confirmation for stripping away duplicates)
test<#>.txt - test files which I tested my parser on.


<h2> Program Usage: </h2>

<h3> From command line: </h3>
<pre><code>python3 lint.py
-OR-
python3 lint.py <name of file you want to parse>
</code></pre>

Example:
test1.txt:
<pre><code>

aaaa
;;;
bbbb
;;;
cccc
;;;;;
</code></pre>
    


<pre><code>
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

<pre><code>

aaaa
;;;
b
;
c
;




</code></pre>
