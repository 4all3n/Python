# String example
name = "Alice"
print("String value:", name)


# Input integer
a = int(input("Enter an integer: "))
print("Integer value:", a)

# Integer example
age = 25
print("Integer value:", age)

# Float example
height = 5.9
print("Float value:", height)

# Complex number example
complex_number = 3 + 4j
print("Complex value:", complex_number)

# List example
fruits = ["apple", "banana", "cherry"]
print("List value:", fruits)

# Tuple example
dimensions = (400, 600)
print("Tuple value:", dimensions)

# Range example

list=(1,2,3,4,5,6,7,8,9,10)


numbers = range(10)
print("Range value:", numbers)

n = range(5, 10)
for x in n:
    print(x)

r = range(0, 10, 2)
for x in r:
    print(x)
    


# dictionary example
# Python dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# dictionary is optimmized for retrieving values when you know the key.
# we create a dictionary by placing key:value pairs inside curly brackets, separated by commas.    

# syntax
# mydict = {"key": "value", "key": "value"}

#example
mydict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary value:", mydict)
print(mydict["name"])

#  Set is a collection which is unorder,unchangeable and uunindexed,no duplicate values
# Set Example 
set={1,4,2,5,3,6,5} #It auto arange the set and remove the dublicate value
print(set)

s=frozenset({"yo","hi","go","no"}) #its a frozen set
print("its a frozen set",s)
try:
    s[1] = "bruh"
except Exception as e:
    print(e)

a=4//2
b=9//2
print(a,b)


# is operator identity operator
a = 5
b = 10
print(a is b)

#in operator membership operator
a = 5
b = [10,5,4,4,4,3,32,34,242]
print(a in b)


# Date 8/8/24 
# Functions of python
# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a result.

#syntax
# def function_name(parameters):
#     """Docstring: Docstring explains what the function does"""  
#     Body of the function
#     return [expression]

#example
print("Function example")
def add(a, b):
    """This function adds two numbers"""
    return a + b
# Call the function
#to call a function use the function name followed by the parenthesis
print(add(5, 10))

#Argument
#Information passed to a function is called an argument.
#The number of arguments that a function must or can receive is called the function's parameter.

#perameters 
#Parameters are variables that are passed to a function.
#Parameters are specified after the function name, inside the parentheses.
#Perameters vs Arguments
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.
#no of arguments should be equal to no of parameters

#Key Components
#1. Function name :-The unique identifier of the function
#2. Parameters :-The data type of the parameters. It allows you to pass data to the function
#3. Docstring :-The description of the function it is optional
#4. Function body :-The code that is executed when the function is called
#5. Return value :-The value that the function returns. If no return value is specified, the function will return None

#Benefit of function
#1. Reusability :- Allows you to use the same code multiple times
#2. Modularity :-Breaking down the code into smaller parts which is easier to maintain
#3. Readability :- The code is easier to understand
#4. Debugging   :- The code is easier to debug

#Types of functions
#1. Function with Arguments and return value
#2. Function without Arguments and return value
#3. Function with Arguments and without return value
#4. Function without Arguments and without return value

#Syntax for with arguments and return value
# def function_name(parameters1,parameters2):
#     """Docstring: Docstring explains what the function does (optional)"""  
#     Body of the function
#     return return_value

#example
print("Function with arguments and return value")
def add(a, b):
    """This function adds two numbers"""
    return a + b
print(add(5, 10))

#Syntax for without arguments and return value
# def function_name():
#     """Docstring: Docstring explains what the function does (optional)"""  
#     Body of the function
#     return return_value

#example
print("Function without arguments and return value")
def add():
    """This function adds two numbers"""
    return 5 + 10
print(add())

#Syntax for with arguments and without return value
# def function_name(parameters1,parameters2):
#     """Docstring: Docstring explains what the function does (optional)"""  
#     Body of the function

#example
print("Function with arguments and without return value")
def add(a, b):
    """This function adds two numbers"""
    print(a + b)
add(1,2)    

#Syntax for without arguments and without return value
# def function_name():
#     """Docstring: Docstring explains what the function does (optional)"""  
#     Body of the function

#example
print("Function without arguments and without return value")
def add():
    """This function adds two numbers"""
    print(5 + 10)
add()    



#lambda
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Syntax
# lambda parameters: expression
#example
print("Lambda example")
x = lambda a : a + 10
print(x(5))



#Date 19/8/24
print("\nDate 19/8/24\n")
#unpacking Tuple
#Python allows you to unpack a tuple
#It is a way to assign the values of tuple to multiple variables in single line
#Syntax
# var1, var2, var3 = tuple
#example
print("Unpacking Tuple example")
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)


#unpacking List
#Python allows you to unpack a list
#It is a way to assign the values of list to multiple variables in single line
#Syntax
# var1, var2, var3 = list
#example
print("Unpacking List example")
a, b, c = [10, 20, 30]
print(a)
print(b)
print(c)

#unpacking Dictionary
#Python allows you to unpack a dictionary
#It is a way to assign the values of dictionary to multiple variables in single line
#Syntax
# var1, var2, var3 = dictionary
#example
print("Unpacking Dictionary example")
mydict= {'x': 10, 'y': 20, 'z': 30}
print("Dictionary:- ",mydict)

print("unpacking Dictionary using keys or just mydict")
a, b, c = mydict # or u can use a, b, c = mydict.keys() #gives key
print(a)
print(b)
print(c)

print("Unpacking Dictionary using items")
a, b, c = mydict.items()#gives key and value
print(a)
print(b)
print(c)

print("Unpacking Dictionary using values")
a, b, c = mydict.values()#gives value
print(a)
print(b)
print(c)



#date 20/8/24
print("\nDate 20/8/24\n")
#Mathematical Functions
#Python's standard library provides many mathematical functions.
#Syntax
#First import math by using 'import math'
#example
#Absolute value
print("Absolute value example")
import math
a = -10
print(math.fabs(a))

#max
#Returns the largest number
#Syntax
#max(a, b, c)
#max(iterable, *args)
#example
print("max example")
a = 10
b = 20
c = 30
print(max(a, b, c))

#min
#Returns the smallest number
#Syntax
#min(a, b, c)
#min(iterable, *args)
#example
print("min example")
a = 10
b = 20
c = 30
print(min(a, b, c))

#other mathematical functions
#ceil gives the smallest integer that is greater than or equal to the number
#floor gives the largest integer that is less than or equal to the number
#round gives the nearest integer
#sqrt gives the square root


#Coding style in python 
#1. Indentation (4 spaces)
#2. Line length (no more than 80 characters per line) use parentheses to group statements
#3. Blank lines (2 blank lines) use blank lines to separate functions and classes from each other
#4. import (at the top) Always import the module at the top of the file or before using its package in your code
#5. Comments (use # for single line comments)
#6. Naming conventions (For variables, functions, Attributes and classes use lower_case_with_underscores)
#7. Docstrings (For functions and classes use """docstring""" to add a description of the function or class)     
#8. Whitespace in Expression and Statement (Avoid spaces before and after =, :, ;)
#9. Exception Handling (try, except, finally) 