class Book:
    def __init__(self, book_id, title, author, year, available=1):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        status = "Available" if self.available == 1 else "Borrowed"

        return (
            f"ID: {self.id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Year: {self.year}\n"
            f"Status: {status}"
        )