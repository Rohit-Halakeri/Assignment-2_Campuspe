#Bill Splitter

total_bill=float(input("Enter total bill coccured:"))
no_of_people=int(input("Enter no of people:"))
tax_percent=float(input("Enter tax percent:"))
tip_percent=float(input("Enter tip_percent:"))

sub_total=total_bill

Tax_Amount=sub_total*tax_percent/100
Bill_After_Tax=sub_total+Tax_Amount

Tip_Amount=sub_total*tip_percent/100
Total_Amount=Bill_After_Tax+Tip_Amount


Amount_per_person=Total_Amount/no_of_people

print("~~~~~~~~~BILL BREAKDOWN ~~~~~~~~~~~")
print("Subtotal: ₹",sub_total)
print(f"Tax of ({tax_percent}):₹{Tax_Amount}")
print(f"After tax :₹{Bill_After_Tax}")
print(f"Tip({tip_percent}):₹{Tip_Amount}")
print(f"Total :₹{Total_Amount}")
print(f"Per Person :₹{Amount_per_person}")