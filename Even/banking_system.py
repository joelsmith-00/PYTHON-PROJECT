PIN = input("Set your 4-digit PIN: ")

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != PIN:
    print("Incorrect PIN!")
    exit()

print("=" * 40)
print("LOGIN SUCCESSFUL")
print("=" * 40)

account_holder = "Joel Smith"
account_number = "ACC1001"

print(f"\nWelcome {account_holder}")
print(f"Account Number: {account_number}")

balance = 1000
transactions = []

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transactions")
    print("6. Calculate Interest")
    print("7. Mini Statement")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")
            continue

        balance += amount
        transactions.append(f"Deposited ₹{amount}")

        with open("transactions.txt", "a") as file:
            file.write(f"Deposited ₹{amount}\n")

        print(f"₹{amount} deposited successfully!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Invalid amount!")
            continue

        if amount <= balance:
            balance -= amount
            transactions.append(f"Withdrawn ₹{amount}")

            with open("transactions.txt", "a") as file:
                file.write(f"Withdrawn ₹{amount}\n")

            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        receiver = input("Enter receiver name: ")
        amount = float(input("Enter amount: ₹"))

        if amount <= balance:
            balance -= amount
            transactions.append(f"Transferred ₹{amount} to {receiver}")

            with open("transactions.txt", "a") as file:
                file.write(f"Transferred ₹{amount} to {receiver}\n")

            print("Transfer Successful!")
        else:
            print("Insufficient Balance!")

    elif choice == "5":
        print("\nTransaction History")
        print(f"Total Transactions: {len(transactions)}")

        if len(transactions) == 0:
            print("No transactions found.")
        else:
            for t in transactions:
                print(t)

    elif choice == "6":
        interest = balance * 0.05
        print(f"Estimated Interest: ₹{interest}")

    elif choice == "7":
        print("\n===== MINI STATEMENT =====")
        print(f"Account Holder: {account_holder}")
        print(f"Account Number: {account_number}")
        print(f"Current Balance: ₹{balance}")

        if len(transactions) == 0:
            print("No transactions available.")
        else:
            print("Recent Transactions:")
            for t in transactions[-5:]:
                print(t)

    elif choice == "8":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice!")