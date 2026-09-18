class Book: 
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} published at {self.year}"

    def is_classic(self):
        if self.year < 1997:
            print("Yes its classic")
        else:
            print("No")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
    def list_books(self):
        for i , book in enumerate(self.books):
            print(f"{i+1}: {book.title}")

    def remove_book(self,title):
        for book in self.books:
            if book.title.lower == title.lower():
                self.books.remove(book)
                return book
        return None

book1 = Book("Ikigai","James",2021)
book2 = Book("The Last of US", "Haalnd",2021)

pokharalibrary = Library()
pokharalibrary.add_book(book1)
pokharalibrary.add_book(book2)
pokharalibrary.list_books()