#Prime Number Checker
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

number=int(input("Enter a number:"))
if isPrime(number):
    print("Prime number ")
else:
    print("Composite number")
# def n_prime_numbers(number):
#     if number==1 or number == 0:
#         return 0
#     for i in range(2,int(number ** 0.5)+1,2):
#         if number % i== 0:
#             print(i,end=" ")
# print(n_prime_numbers)
