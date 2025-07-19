

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
    
    def find_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def remove_book(self, title: str):
        book_to_remove = self.find_book(title)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Removed: {book_to_remove}")
        else:
            print(f"Book '{title}' not found in the library.")
            
            
def main():
    library = Library()
    
    book1 = Book("1984", "George Orwell", 328)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    print("Books in the library:")
    library.list_books()
    
    print("\nFinding '1984':")
    found_book = library.find_book("1984")
    if found_book:
        print(found_book)
    else:
        print("Book not found.")
    
    print("\nRemoving 'The Great Gatsby':")
    library.remove_book("The Great Gatsby")
    
    print("\nBooks in the library after removal:")
    library.list_books()
    
if __name__ == "__main__":
    main()
    