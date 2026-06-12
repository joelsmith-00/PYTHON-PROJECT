employees = {}

while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")

        employees[emp_id] = name
        print("Employee Added!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            for emp_id, name in employees.items():
                print(f"{emp_id} : {name}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")