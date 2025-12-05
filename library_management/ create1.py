# #CREATE
# def add_book(self, title, author, isbn):
#     # Validate input
#     if not title or not author or not isbn:
#         return "Error: Title, author, and ISBN are required."

#     # Check for duplicate ISBN
#     for book in self.books:
#         if book.isbn == isbn:
#             return f"Error: A book with ISBN {isbn} already exists."

#     # Add new book
#     new_book = Book(title, author, isbn)
#     self.books.append(new_book)
#     self._save_books()

#     return f"Book '{title}' added successfully."
from .libraryA import Book   # import fixed

def add_book(self, title, author, isbn):
    if not title or not author or not isbn:
        return "Error: Title, author, and ISBN are required."

    for book in self.books:
        if book.isbn == isbn:
            return f"Error: A book with ISBN {isbn} already exists."

    new_book = Book(title, author, isbn)
    self.books.append(new_book)
    self._save_books()
    return f"Book '{title}' added successfully."
