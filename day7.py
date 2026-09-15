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
            
b = Book("The Last of US","G martin",2021)
print(b.title)
print(b.author)
print(b.year)

b.is_classic()
