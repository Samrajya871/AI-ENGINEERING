from database import (
    create_table,
    add_book,
    view_books,
    search_book,
    borrow_book,
    return_book,
    update_book,
    delete_book,
    statistics,
    close_connection
)

from models import Book
from utils import (
    print_menu,
    validate_year,
    validate_available,
    display_books,
    log_activity
)


def main():

    create_table()

    while True:

        print_menu()

        choice = input("Choose an option: ")

        # ---------------- Add Book ----------------

        if choice == "1":

            try:
                book_id = int(input("Enter Book ID: "))
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                year = validate_year()
                available = validate_available()

                book = Book(book_id, title, author, year, available)

                if add_book(book):
                    print("Book added successfully.")
                    log_activity(f"Added book: {title}")

            except ValueError:
                print("Invalid input.")

        # ---------------- View Books ----------------

        elif choice == "2":

            books = view_books()
            display_books(books)

        # ---------------- Search Book ----------------

        elif choice == "3":

            keyword = input("Enter title or author: ")

            books = search_book(keyword)

            if books:
                display_books(books)
            else:
                print("Book not found.")

        # ---------------- Borrow Book ----------------

        elif choice == "4":

            try:
                book_id = int(input("Enter Book ID: "))

                result = borrow_book(book_id)

                if result == "success":
                    print("Book borrowed successfully.")
                    log_activity(f"Borrowed book ID: {book_id}")

                elif result == "already_borrowed":
                    print("Book is already borrowed.")

                else:
                    print("Book not found.")

            except ValueError:
                print("Invalid ID.")

        # ---------------- Return Book ----------------

        elif choice == "5":

            try:
                book_id = int(input("Enter Book ID: "))

                result = return_book(book_id)

                if result == "success":
                    print("Book returned successfully.")
                    log_activity(f"Returned book ID: {book_id}")

                elif result == "already_returned":
                    print("Book is already available.")

                else:
                    print("Book not found.")

            except ValueError:
                print("Invalid ID.")

        # ---------------- Update Book ----------------

        elif choice == "6":

            try:
                book_id = int(input("Enter Book ID: "))

                title = input("Enter New Title: ")
                author = input("Enter New Author: ")
                year = validate_year()
                available = validate_available()

                book = Book(book_id, title, author, year, available)

                if update_book(book):
                    print("Book updated successfully.")
                    log_activity(f"Updated book: {title}")
                else:
                    print("Book not found.")

            except ValueError:
                print("Invalid input.")

        # ---------------- Delete Book ----------------

        elif choice == "7":

            try:
                book_id = int(input("Enter Book ID: "))

                if delete_book(book_id):
                    print("Book deleted successfully.")
                    log_activity(f"Deleted book ID: {book_id}")
                else:
                    print("Book not found.")

            except ValueError:
                print("Invalid ID.")

        # ---------------- Statistics ----------------

        elif choice == "8":

            total, available, borrowed = statistics()

            print("\n===== Library Statistics =====")
            print(f"Total Books      : {total}")
            print(f"Available Books  : {available}")
            print(f"Borrowed Books   : {borrowed}")

        # ---------------- Exit ----------------

        elif choice == "9":

            close_connection()

            print("Database connection closed.")
            print("Thank you for using Library Management System.")
            break

        # ---------------- Invalid Choice ----------------

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()