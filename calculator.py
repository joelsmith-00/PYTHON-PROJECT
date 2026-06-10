while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")

    choice = input("Choice: ")

    if choice == "5":
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        print("Result:", a / b)