#Write a program to double the given number and sum of two numbers using lambda function

#define lambda function
double=lambda x:x*2
add=lambda x,y:x+y

#take input from user
num=int(input("Enter a number: "))
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

#apply lambda function
result=double(num)
result1=add(num1,num2)

#display result
print("Double of ",num,"is",result)
print("Sum of ",num1,"and",num2,"is",result1)

