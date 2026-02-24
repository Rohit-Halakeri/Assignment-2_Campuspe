#Number System Functions

def factorial(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

def isPrime(number):
    if number<=1:
        return False
    if number == 2:
        return True
    if number%2==0:
        return False
    
    for i in range(3, int(number**0.5)+1, 2):
        if (number % i) == 0:
            return False
    return True

def fibbonacci(n):
    if n<=1:
        return n
    return fibbonacci(n-1)+fibbonacci(n-2)

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return (n%10)+sum_of_digits(n//10)
    
def reverse_number(n):
    if n<0:
        reversed_num=int(str(abs(n))[::-1])*-1
    else:
        reverse_number=int(str(n)[::-1])
    return reversed_num

def isArmStrong(n):
    temp = n
    sum=0
    while temp > 0:
         digit = temp % 10
         sum += digit ** 3
         temp //= 10
    if n == sum:
        return True
    return False

def gcd(a,b):
    while b != 0:
      a= b
      b=a % b
    return a

def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i
        
def is_perfect_number(n):
    
    Sum = 0
    for i in range(1, n):
       if(n % i == 0):
          Sum = Sum + i
       if (Sum == n):
           return True
    return False

def math_menu():

    while True:
        print("~~~~~~~~~MENU~~~~~~~~~~")
        print("1.Factorial of a number")
        print("2.Check if a number is prime or not")
        print("3.nth element of a fibonacci series")
        print("4.Sum of digits")
        print("5.Reverse a number")
        print("6.Check if a number is an armstrong number")
        print("7.Calculate gcd of two numbers")
        print("8.Calculate LCM of two numbers")
        print("9.Check if a number is perfect or not")
        print("10.Exit")

        choice=int(input("Enter a choice to proceed:"))
        if choice==1:
            number=int(input("Enter a  number to check :"))
            print("Factorial of 5",factorial(number))
        
        #Check if the number is prime or not
        elif choice==2:
            number=int(input("Enter a  number to check:"))
            if isPrime(number):
                print("Prime Number")
            else:
                print("Composite number")
        
        #To check nth number of fibonacci series
        elif choice==3:
            number=int(input("Enter a  number to check:"))
            print("nth no of the series is ",fibbonacci(number))

        #To find the sum of digits
        elif choice==4:
            number=int(input("Enter a  number to find:"))
            print("Sum of the digits is ",sum_of_digits(number))

        #To reverse a number
        elif choice==5:

            number=int(input("Enter a  number to find:"))
            print("The reversed number is ",reverse_number(number))

        #To check if a number is armstrong number or not
        elif choice==6:
            number=int(input("Enter a  number to check:"))
            if isArmStrong(number):
                print("Its an Armstrong Number")
            else:
                print("Its not armstrong number")

        #To find out gcd
        elif choice==7:
            a=int(input("Enter a  first number to find:"))
            b=int(input("Enter a second  number to find:"))
            print(f"GCD of {(a,b)} is {gcd(a,b)}")

        #To find out LCM 
        elif choice==8:
            a=int(input("Enter a  first number to find:"))
            b=int(input("Enter a second  number to find:"))
            print(f"LCM of {(a,b)} is {LCM(a,b)}")

        #To check if its a perfect number or not
        elif choice==9:
            number=int(input("Enter a  number to check:"))
            if is_perfect_number(number):
                print("Yes its a perfect number")
            else:
                print("Not a perfect number ")
        elif choice==10:
            return -1
        else:
            print("Invalid Input Try again")




math_menu()
     


   


    

   
  
# display the result

    
    