#Calculator Functions

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Cannot divide by zero")
    else:
        return a/b
def modulus(a,b):
    return a%b

def power(a,b):
    return a**b

def calculator():
    while True:
        print("~~~~~~~~~MENU~~~~~~~~~~")
        print("1.Addition of two numbers")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Modulus operation")
        print("6.Power of another number")
        print("7.Exit")
        choice=int(input("Enter a choice to proceed:"))
        if choice==1:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Addition of {number_1}+{number_2} = {add(number_1,number_2)}")
        elif choice==2:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Subtraction of {number_1}-{number_2} = {subtract(number_1,number_2)}")
        elif choice==3:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Product of {number_1}*{number_2} = {multiply(number_1,number_2)}")
        elif choice==4:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Quotient of {number_1}/{number_2} = {divide(number_1,number_2)}")
        elif choice==5:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Remainder of {number_1}%{number_2} = {modulus(number_1,number_2)}")
        elif choice==6:
            number_1=float(input("Enter the first number :"))
            number_2=float(input("Enter the second number:"))
            print(f"Result of {number_1}^{number_2} = {power(number_1,number_2)}")
        elif choice==7:
            return -1
        else:
            print("Invalid Input Try again")


calculator()