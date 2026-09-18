#b = Book("Ikigai","James",2002)
# book_to_json(b)
# book--> json
from models import Book
import json 

def book_to_json(book):
    return{
        "title": book.title,
        "auhtor": book.auhtor,
        "year": book.year
    }

#json-->Book
def book_from_json(jsonBook):
    return Book(
        jsonBook["title"],
        jsonBook["auhtor"],
        jsonBook["year"]
    )

def save_library(library):
    data = []
    for book in library.books:
        data.append(book_to_json(book))
    with open("library.json", "w",encoding="utf-8") as file:
        json.dump(data)
        print("Library saved successfully")