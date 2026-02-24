#Multiplication Table Generator

number=int(input("Enter the number which we want to print the table:"))
end_num=int(input("Enter the end range of the table "))
result=0

for i in range(1,end_num+1):
    result = number*i
    print(f"{number} * {i} = {result}")
    