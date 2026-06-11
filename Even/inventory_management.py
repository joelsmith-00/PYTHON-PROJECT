items = {}

while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Search Item")
    print("4. Delete Item")
    print("5. Update Stock")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Item Name: ")
        quantity = int(input("Quantity: "))

        items[item] = quantity
        print("Item Added!")

    elif choice == "2":
        print(f"Total Products: {len(items)}")

        if len(items) == 0:
            print("Inventory is empty.")
        else:
            for item, quantity in items.items():
                print(f"{item}: {quantity}")

                if quantity < 5:
                    print("⚠ Low Stock")

    elif choice == "3":
        search_item = input("Enter item name to search: ")

        if search_item in items:
            print(f"{search_item}: {items[search_item]}")
        else:
            print("Item not found.")

    elif choice == "4":
        delete_item = input("Enter item name: ")

        if delete_item in items:
            del items[delete_item]
            print("Item deleted")
        else:
            print("Item not found")

    elif choice == "5":
        update_item = input("Enter item name: ")

        if update_item in items:
            new_quantity = int(input("Enter new quantity: "))
            items[update_item] = new_quantity
            print("Stock updated!")
        else:
            print("Item not found")

    elif choice == "6":
        print("Exiting Inventory Management System...")
        break

    else:
        print("Invalid Choice")