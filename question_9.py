#Ticket Pricing System


age = int(input("Enter age: "))
day = input("Enter day of week: ").lower() #here we used lower because some of them use Uppercase letters .
tickets = int(input("Enter number of tickets: "))

if age < 3:
    price = 0
    category = "Free"
elif age <= 12:
    price = 150
    category = "Child"
elif age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

base_price = price * tickets

if day in ["friday", "saturday", "sunday"]:
    discount = base_price * 0.20   # 20% discount
else:
    discount = 0

price_after_discount = base_price - discount

print("\n=== MOVIE BILL ===")
print("Category:", category)
print(f"Base price: ₹{base_price:}")
print(f"Discount: ₹{discount:}")
print(f"After discount: ₹{price_after_discount:}")
print(f"Total amount: ₹{price_after_discount:}")


