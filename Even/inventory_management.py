items = {}

while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Item Name: ")
        quantity = int(input("Quantity: "))
        items[item] = quantity
        print("Item Added!")

    elif choice == "2":
        for item, quantity in items.items():
            print(f"{item}: {quantity}")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")