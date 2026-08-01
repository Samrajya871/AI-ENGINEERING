import sqlite3
from models import Book


def connect_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    return conn, cursor


conn, cursor = connect_db()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        available INTEGER
    )
    """)
    conn.commit()


def add_book(book):
    try:
        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?, ?)",
            (book.id, book.title, book.author, book.year, book.available)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Book ID already exists.")
        return False
    except sqlite3.Error as e:
        print("Database Error:", e)
        return False


def view_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()


def search_book(keyword):
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )
    return cursor.fetchall()


def borrow_book(book_id):
    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if not book:
        return "not_found"

    if book[0] == 0:
        return "already_borrowed"

    cursor.execute(
        "UPDATE books SET available=0 WHERE id=?",
        (book_id,)
    )
    conn.commit()
    return "success"


def return_book(book_id):
    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if not book:
        return "not_found"

    if book[0] == 1:
        return "already_returned"

    cursor.execute(
        "UPDATE books SET available=1 WHERE id=?",
        (book_id,)
    )
    conn.commit()
    return "success"


def update_book(book):
    cursor.execute("SELECT * FROM books WHERE id=?", (book.id,))
    existing = cursor.fetchone()

    if not existing:
        return False

    cursor.execute("""
        UPDATE books
        SET title=?,
            author=?,
            year=?,
            available=?
        WHERE id=?
    """, (
        book.title,
        book.author,
        book.year,
        book.available,
        book.id
    ))

    conn.commit()
    return True


def delete_book(book_id):
    cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if not book:
        return False

    cursor.execute(
        "DELETE FROM books WHERE id=?",
        (book_id,)
    )

    conn.commit()
    return True


def statistics():
    cursor.execute("SELECT COUNT(*) FROM books")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE available=1")
    available = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE available=0")
    borrowed = cursor.fetchone()[0]

    return total, available, borrowed


def close_connection():
    conn.close()