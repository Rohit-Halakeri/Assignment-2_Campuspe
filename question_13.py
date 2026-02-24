#Sum and Average Calculator

n=int(input("Enter how many numbers you want to add:"))


num=float(input("Enter number 1:"))
total=num
min=num
max=num

for i in range(2,n+1):
    num=float(input(f"Enter number {i} :"))
    total =total+num;
    
    if num>max:
        max=num
    if num<min:
        min=num
        

average=total/n
print("Total Sum :",total)
print("Average:",average)
print("Maximum number:",max)
print("Minimum number:",min)


