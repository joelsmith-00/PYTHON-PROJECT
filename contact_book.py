contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact Added!")

    elif choice == "2":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

    elif choice == "3":
        break

    else:
        print("Invalid Choice")