#Simple ATM Simulator

balance = 10000   # Initial balance

while True:
    print("\n===== ATM SIMULATOR =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    # 1️ Check Balance
    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    # 2️ Deposit
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        
        if amount > 0:
            balance += amount
            print("Deposit successful!")
            print(f"New balance: ₹{balance}")
        else:
            print("Invalid deposit amount!")

    # 3️ Withdraw
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > balance:
            print("Insufficient balance!")

        elif balance - amount < 500:
            print("Minimum balance of ₹500 must remain!")

        else:
            balance -= amount
            print("Withdrawal successful!")
            print(f"New balance: ₹{balance}")

    # 4️ Exit
    elif choice == "4":
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")