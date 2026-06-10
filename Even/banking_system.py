PIN = "1234"

entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin != PIN:
    print("Incorrect PIN!")
    exit()

print("Login Successful!")

account_holder = "Joel Smith"
print(f"\nWelcome {account_holder}")

balance = 1000
transactions = []

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transactions")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Current Balance: ₹{balance}")

    elif choice == "2":
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        transactions.append(f"Deposited ₹{amount}")
        with open("transactions.txt", "a") as file:
         file.write(f"Deposited ₹{amount}\n")
        print(f"₹{amount} deposited successfully!")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: ₹"))

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

        if len(transactions) == 0:
            print("No transactions found.")
        else:
            for t in transactions:
                print(t)

    elif choice == "6":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice!")