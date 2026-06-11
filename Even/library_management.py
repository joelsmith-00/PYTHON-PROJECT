print("=" * 40)
print("LIBRARY MANAGEMENT SYSTEM")
print("=" * 40)

books = []

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Return Book")
    print("6. Exit")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        author = input("Enter author name: ")
        category = input("Enter category: ")

        books.append(f"{book} - {author} - {category}")
        with open("books.txt", "a") as file:
            file.write(f"{book} - {author} - {category}\n")
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print(f"Total Books: {len(books)}")
            print("\nBooks in Library:")
            for book in books:
                print(book)

    elif choice == "3":
        search_term = input("Enter book name to search: ")
        found_books = [book for book in books if search_term.lower() in book.lower()]
        if found_books:
            print("\nFound Books:")
            for book in found_books:
                print(book)
        else:
            print("Book not found.")

    elif choice == "4":
        book_to_delete = input("Enter book name to delete: ")
        if book_to_delete in books:
            books.remove(book_to_delete)
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you!")
        break

    elif choice == "6":
        print("Thank you!")
        break
   
    elif choice == "7":
     return_book = input("Enter book name to return: ")
    print(f"{return_book} returned successfully!")

else:
    print("Invalid choice!")