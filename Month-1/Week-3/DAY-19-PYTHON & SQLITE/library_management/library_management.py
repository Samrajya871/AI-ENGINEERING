import sqlite3

#connect to database
conn = sqlite3.connect("library.db")
cursor=conn.cursor()

#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY,
title TEXT,
author TEXT,
year INTEGER,
available INTEGER
)
""")

conn.commit()

def add_book():
    try:
        book_id = int(input("Enter BOOK ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter AUthor Name: ")
        year = int(input("Enter Published Year: "))
        available = int(input("Available? (1=Yes, 0=No): "))

        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)",
        (book_id, title, author, year, available))

        conn.commit()
        print("Book added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct values.")

    except sqlite3.IntegrityError:
        print("Book ID already exists.")

def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if books:
        print("\n------- Books -------")
        for book in books:
            status = "Available" if book[4] == 1 else "Borrowed"
            print(f"""
ID: {book[0]}
Title: {book[1]}
Author: {book[2]}
Year: {book[3]}
Status: {status}
""")

    else: 
        print("No books found")

def search_book():
    keyword = input("Enter title or author to search: ")

    cursor.execute(
      "SELECT * FROM books WHERE title LIKE ? or author LIKE ?",
      (f"%{keyword}%", f"%{keyword}%")
     )

    books = cursor.fetchall()

    if books:
        for book in books:
            status = "Available" if book[4] == 1 else "Borrowed"
            print(f"""
ID: {book[0]}
Title: {book[1]}
Author: {book[2]}
Year: {book[3]}
Status: {status}
""")

    else:
        print("Book not found.")


def update_book():
    try:
        book_id = int(input("Enter Book ID to update: "))

        cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))

        book = cursor.fetchone()

        if book:
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = int(input("Enter new year: "))
            available = int(input("Available? (1=Yes, 0=No)"))

            cursor.execute("""
                UPDATE books 
                SET title = ?, author = ?, year=?, available=?
                WHERE id=?
                """,(title, author, year, available, book_id))

            conn.commit()
            print("Book updated sucessfully.")

        else:
            print("Book not found")

    except ValueError:
        print("invalid input")


def delete_book():
    try:
        book_id = int(input("Enter Book ID to delete: "))

        cursor.execute("SELECT * FROM books WHERE id=?",(book_id,))
        book = cursor.fetchone()

        if book:
            cursor.execute("DELET FROM books WHERE id=?",(book_id,))
            conn.commit()
            print("BOOK deleted successfully.")
        else:
            print("Book not found")

    except ValueError:
        print("Invalid input")

def exit_program():
    conn.close()
    print("Database connection closed.")
    print("Thank you for using Library Management System. ")
    exit()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
         view_books()

    elif choice == "3":
         search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        exit_program()

    else:
        print("Invalid choice. Try again.")

