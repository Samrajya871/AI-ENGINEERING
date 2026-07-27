class Book:
    def __init__(self,Title,Author):
        self.Title=Title
        self.Author=Author
        self.available=True
    

    def borrow(self):
        if self.available:
            self.available=False
            print(f"{self.Title} borrowed" )
        
        else:
            print(f"{self.Title} already Borrowed")
    
    def return_book(self):
        if not self.available:
            self.available=True
            print(f"{self.Title} returned. ")

        else:
            print(f"{self.title} is already available")

    
    def display(self):
        status= "Yes" if self.available else "No"
        print(f"Title: {self.Title}")
        print(f"Author: {self.Author}")
        print(f"Available: {self.available}")
        print("-" *30)


b1=Book("ASOIAF","GRRM")
b2=Book("LOTR","J.R.R Tolkein")
b3=Book("Red Rising","Pierce Brown")

books=[b1,b2,b3]

b1.borrow()
b1.return_book()
b2.borrow()

print("\nLibrary Books")
print("=" *30)

for book in books:
    book.display()