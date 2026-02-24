#Number Pattern
print("=== PATTERN GENERATOR ===")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

choice=int(input("Enter a number to choose:"))
n=int(input("Enter height:"))

print() #to look good we print blank spaces

#first pattern
if choice==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

elif choice==2:
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()

elif choice == 3:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
elif choice == 4:

    for i in range(1,n+1):

        #For increasing step like structure
        for j in range(1,i+1):
            print(j,end="")
        
        #For decreasing step like structure
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
else:
    print("Please enter valid choice !!")
