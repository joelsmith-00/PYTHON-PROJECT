items = {}

while True:
    print("\n===== INVENTORY MANAGEMENT =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Search Item")
    print("4. Exit")

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
        search_item = input("Enter item name to search: ")
        if search_item in items:
            print(f"{search_item}: {items[search_item]}")
        else:
            print("Item not found.")

    elif choice == "4":
        break
    elif choice == "4":
     delete_item = input("Enter item name: ")

    if delete_item in items:
        del items[delete_item]
        print("Item deleted")
    else:
        print("Item not found")

    e