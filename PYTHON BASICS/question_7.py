#Temperature Converter
'''
Menu
Choose the numbers for the following conversions
1 .Celsius to Fahrenheit
2.Fahrenheit to Celsius
3.Celsius to Kelvin
4.Kelvin to Celsius
5.Fahrenheit to Kelvin
6.Kelvin to Fahrenheit
7.Exit
'''

print("~~Menu~~~~")
print("Choose the numbers for the following conversions")
print("1 .Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("4.Kelvin to Celsius")
print("5.Fahrenheit to Kelvin")
print("6.Kelvin to Fahrenheit")
print("7.Exit")

choice=int(input("Choose the number from the menu:"))

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
def celsius_to_kelvin(celsius):
    return celsius+273.15
def kelvin_to_celsius(kelvin):
    return kelvin-273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit-32)*5/9+273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin-273.15)*9/5+32

if choice==1:
    temp=float(input("Enter temperature in celsius :"))
    print("Converted temnperature in Fahrenheit : ",celsius_to_fahrenheit(temp))
elif choice==2:
    temp=float(input("Enter temperature in Fahrenheit:"))
    print("Converted temperature in celsius :",fahrenheit_to_celsius(temp))
elif choice==3:
    temp=float(input("Enter temperature in celsius:"))
    print("Converted temperature in kelvin :",celsius_to_kelvin(temp))
elif choice==4:
    temp=float(input("Enter temperature in Kelvin:"))
    print("Converted temperature in Celsius :",kelvin_to_celsius(temp))
elif choice==5:
    temp=float(input("Enter temperature in Fahrenheit:"))
    print("Converted temperature in Kelvin :",fahrenheit_to_kelvin(temp))
elif choice ==6:
    temp=float(input("Enter temperature in Kelvin:"))
    print("Converted temperature in Fahrenheit :",kelvin_to_fahrenheit(temp))
elif choice==7:
    print("Bye Bye 😄🙋‍♂️")

    

