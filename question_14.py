#Factorial Calculator

def factorial(n):
    result=1
    for i in range(2,n+1):#We start with 2 because we get the same result when we multipli with 1
        result=result*i
    return result

number=int(input("Enter number:"))
print(f"Factorial of {number} is {factorial(number)}")


