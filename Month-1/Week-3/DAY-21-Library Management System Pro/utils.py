# ===========================
# Helper Functions
# ===========================

def print_menu():
    print("\n" + "=" * 35)
    print(" Library Management System Pro")
    print("=" * 35)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Update Book")
    print("7. Delete Book")
    print("8. Statistics")
    print("9. Exit")
    print("=" * 35)


def validate_year():
    while True:
        try:
            year = int(input("Enter publication year: "))
            return year
        except ValueError:
            print("Invalid year. Please enter a number.")


def validate_available():
    while True:
        try:
            available = int(input("Available? (1 = Yes, 0 = No): "))

            if available in (0, 1):
                return available

            print("Please enter only 1 or 0.")

        except ValueError:
            print("Invalid input. Enter 1 or 0.")


def display_books(books):

    if not books:
        print("\nNo books found.")
        return

    print("\n" + "-" * 50)

    for book in books:

        status = "Available" if book[4] == 1 else "Borrowed"

        print(f"""
ID      : {book[0]}
Title   : {book[1]}
Author  : {book[2]}
Year    : {book[3]}
Status  : {status}
""")
        print("-" * 50)


def log_activity(message):
    with open("activity.log", "a") as file:
        file.write(message + "\n")