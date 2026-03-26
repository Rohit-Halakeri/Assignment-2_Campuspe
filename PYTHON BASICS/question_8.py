#Leap Year Checker 

Year=int(input("Enter a year :"))
if(Year%400==0):
    print("Leap Year")
elif Year%100==0:
    print("Not a leap year")
elif(Year%4==0):
    print("Leap Year")
else:
    print("Not a leap year ")
  
