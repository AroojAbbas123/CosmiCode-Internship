import asyncio
from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

class Library:
    def __init__(self):
        self.books: List[Book] = []

    async def add_book(self, book: Book) -> None:
        # Simulate I/O delay (e.g., database operation)
        await asyncio.sleep(0.5)
        self.books.append(book)
        print(f"Added: {book}")

    async def list_books(self) -> None:
        # Simulate I/O delay
        await asyncio.sleep(0.3)
        if not self.books:
            print("The library is empty.")
            return
        
        print("\nBooks in the library:")
        for book in self.books:
            print(f" - {book}")

    async def find_book(self, title: str) -> Optional[Book]:
        # Simulate search delay
        await asyncio.sleep(0.4)
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    async def remove_book(self, title: str) -> None:
        # Simulate I/O delay
        await asyncio.sleep(0.6)
        book = await self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Removed: {book}")
        else:
            print(f"Book '{title}' not found in the library.")

async def main():
    library = Library()

    # Create some books
    books_to_add = [
        Book("1984", "George Orwell", 328),
        Book("To Kill a Mockingbird", "Harper Lee", 281),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 180),
        Book("Dune", "Frank Herbert", 412),
        Book("Pride and Prejudice", "Jane Austen", 279)
    ]

    # Add books asynchronously
    print("Adding books to the library...")
    add_tasks = [library.add_book(book) for book in books_to_add]
    await asyncio.gather(*add_tasks)

    # List all books
    await library.list_books()

    # Search for books asynchronously
    print("\nSearching for books...")
    search_tasks = [
        library.find_book("1984"),
        library.find_book("Dune"),
        library.find_book("Non-existent Book")
    ]
    found_books = await asyncio.gather(*search_tasks)

    for book in found_books:
        if book:
            print(f"Found: {book}")
        else:
            print("Book not found")

    # Remove books asynchronously
    print("\nRemoving books...")
    remove_tasks = [
        library.remove_book("The Great Gatsby"),
        library.remove_book("Non-existent Book")
    ]
    await asyncio.gather(*remove_tasks)

    # List remaining books
    await library.list_books()

    # Demonstrate concurrent operations
    print("\nPerforming concurrent operations:")
    await asyncio.gather(
        library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 310)),
        library.find_book("Dune"),
        library.remove_book("Pride and Prejudice")
    )

    # Final list of books
    print("\nFinal library contents:")
    await library.list_books()

if __name__ == "__main__":
    asyncio.run(main())