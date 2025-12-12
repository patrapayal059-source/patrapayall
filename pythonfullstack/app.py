# from flask import Flask
# from router import register_routes
# from database.db import init_db

# app = Flask(__name__)

# # Initialize database
# init_db()

# # Register all API routes
# register_routes(app)

# if __name__ == "__main__":
#     app.run(debug=True , port=5000)
import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify
from services.book_service import BookService

def print_books():
    books = BookService.list_books()
    if not books:
        print("No books found.")
        return
    for book in books:
        print(f"{book['id']}: {book['title']} by {book['author']} (ISBN: {book['isbn']}, Year: {book.get('year')})")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. List all books")
        print("2. Add a book")
        print("3. Update a book")
        print("4. Get a book by ID")
        print("5. Delete a book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print_books()

        elif choice == "2":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year (optional): ")
            data = {"title": title, "author": author, "isbn": isbn, "year": int(year) if year else None}
            book = BookService.create_book(data)
            print("Book added:", book)

        elif choice == "3":
            book_id = int(input("Enter book ID to update: "))
            title = input("New Title: ")
            author = input("New Author: ")
            isbn = input("New ISBN: ")
            year = input("New Year (optional): ")
            data = {"title": title, "author": author, "isbn": isbn, "year": int(year) if year else None}
            updated = BookService.update_book(book_id, data)
            print("Book updated:", updated)

        elif choice == "4":
            book_id = int(input("Enter book ID: "))
            book = BookService.get_book(book_id)
            print("Book:", book if book else "Not found.")

        elif choice == "5":
            book_id = int(input("Enter book ID to delete: "))
            deleted = BookService.delete_book(book_id)
            print("Deleted:", deleted)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
