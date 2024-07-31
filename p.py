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