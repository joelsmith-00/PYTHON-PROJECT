employees = {}

while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        salary = input("Employee Salary: ")

        employees[emp_id] = {
            "name": name,
            "salary": salary
        }

        print("Employee Added!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees found.")
        else:
            for emp_id, emp_info in employees.items():
                print(f"{emp_id} : {emp_info['name']} - ₹{emp_info['salary']}")

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")

        if emp_id in employees:
            print(f"Employee Found: {emp_id}")
            print(f"Name: {employees[emp_id]['name']}")
            print(f"Salary: ₹{employees[emp_id]['salary']}")
        else:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted!")
        else:
            print("Employee not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")