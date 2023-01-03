0x09. Python - Everything is object

In this project, I continued my OOP learning journey by working with mutable and imutable objects. Concepts I learned and applied include Mutation, Cloning and Aliasing.

Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc

.txt Answer Files

    Only one line
    No Shebang
    All your files should end with a new line

Tasks
0. Who am I?
What function would you use to print the type of an object?

Write the name of the function in the file, without ().

1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count 
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

3. Right count = 
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

 5. Right count =+ 
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

6. Is equal 
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

7. Is the same 
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

