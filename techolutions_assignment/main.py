import user  # Handles user management from user.py
import book  # Handles book management from book.py
import check  # Handles checkout operations from check.py

def main_menu() -> str:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. Update User")
    print("5. Delete User")
    print("6. Checkout Book")
    print("7. Exit")
    choice = input("Enter choice (1-7): ").strip()
    return choice

def main() -> None:
    while True:
        choice = main_menu()

        if choice == '1':  # Add Book
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN (numeric): ").strip()

            # Validate ISBN input
            if not isbn.isdigit():
                print("Invalid ISBN. Please enter a numeric ISBN.")
                continue

            book.add_book(title, author, isbn)
            print(f"Book '{title}' added successfully.")

        elif choice == '2':  # List books
            book.list_books()

        elif choice == '3':  # Add User
            name = input("Enter user name: ").strip()
            user_id = input("Enter user ID (numeric): ").strip()

            # Validate user ID input
            if not user_id.isdigit():
                print("Invalid User ID. Please enter a numeric ID.")
                continue

            user.add_user(name, int(user_id))
            print(f"User '{name}' added successfully.")

        elif choice == '4':  # Update User
            user_id = input("Enter user ID (numeric) to update: ").strip()
            if not user_id.isdigit():
                print("Invalid User ID. Please enter a numeric ID.")
                continue

            new_name = input("Enter new user name: ").strip()
            user.update_user(int(user_id), new_name)
            print(f"User with ID {user_id} updated successfully.")

        elif choice == '5':  # Delete User
            user_id = input("Enter user ID (numeric) to delete: ").strip()
            if not user_id.isdigit():
                print("Invalid User ID. Please enter a numeric ID.")
                continue

            user.delete_user(int(user_id))
            print(f"User with ID {user_id} deleted successfully.")

        elif choice == '6':  # Checkout Book
            user_id = input("Enter user ID (numeric): ").strip()
            isbn = input("Enter ISBN of the book to checkout (numeric): ").strip()

            # Validate inputs
            if not user_id.isdigit():
                print("Invalid User ID. Please enter a numeric ID.")
                continue
            if not isbn.isdigit():
                print("Invalid ISBN. Please enter a numeric ISBN.")
                continue

            check.checkout_book(int(user_id), isbn)

        elif choice == '7':  # Exit
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
