def main():
    print("Operators in Python\n 1. Arithmetic Operators\n 2. Relational Operators\n 3. Logical Operators\n 4. Bitwise Operators\n 5. Assignment Operators\n 6. Membership Operators\n 7. Identity Operators")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"SUM: {a+b}")
        print(f"SUBTRACTION: {a-b}")
        print(f"PRODUCT: {a*b}")
        print(f"DIVISION: {a/b}")
        print(f"MODULUS: {a%b}")
        print(f"EXPONENTIATION: {a**b}")
        print(f"INTEGER DIVISION: {a//b}")

    elif choice == 2:
        print("Enter the number to check greater then.\n")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if a>b:
            print("a is greater than b")
        elif b>a:
            print("b is greater than a")
        else:
            print("a and b are equal")

    elif choice == 3:
        print("Enter the number to check if its equal to 0.\n")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if a and b == 0:
            print("Values are 0")
        else:
            print(f"Values are {a}, {b}")
        

    elif choice == 4:
        print("Bitwise Operators\n")
        a = int(input("Enter the first number: "))
    elif choice == 5:
        assignment()
    elif choice == 6:
        membership()
    elif choice == 7:
        identity()
    else:
        print("Invalid choice. Please try again.")

