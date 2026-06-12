students = {}

while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        mark = int(input("Mark: "))
        students[name] = mark
        print("Student Added!")

    elif choice == "2":
        for name, mark in students.items():
            print(f"{name}: {mark}")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            print(f"Mark: {students[name]}")
        else:
            print("Student not found")

    elif choice == "4":
        break