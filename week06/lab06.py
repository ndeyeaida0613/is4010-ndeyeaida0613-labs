class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 
    
    def get_age(self):
        current_year = 2025
        return current_year - self.year

    def __str__(self):
        return f"\"{self.title}\" by {self.author} ({self.year})"
    
class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"
    
if __name__ == "__main__":
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    ebook1 = EBook("Dune", "Frank Herbert", 1965, 5)

    print(book1)  # Output: "The Hobbit" by J.R.R. Tolkien (1937)
    print(ebook1) # Output: "Dune" by Frank Herbert (1965) (5 MB)
    print(book1.get_age())  # Output: 88
    print(ebook1.get_age()) # Output: 60