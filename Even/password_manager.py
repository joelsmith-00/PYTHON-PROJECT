import os

FILE_NAME = "passwords.txt"

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Website Name: ")
        username = input("Username: ")
        password = input("Password: ")

        with open(FILE_NAME, "a") as file:
            file.write(f"{website} | {username} | {password}\n")

        print("Password saved successfully!")

    elif choice == "2":
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                data = file.read()

                if data:
                    print("\nSaved Passwords:")
                    print(data)
                else:
                    print("No passwords stored.")
        else:
            print("No passwords stored.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")