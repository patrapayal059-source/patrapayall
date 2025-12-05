


from flask import Flask, request, jsonify
from library_management.libraryA import Library
from library_management.create1 import CreateBook
from library_management.read import ReadBook
from library_management.update1 import UpdateBook
from library_management.delete1 import DeleteBook

app = Flask(__name__)

# MAIN LIBRARY OBJECT
library = Library()

# CREATE CRUD CLASS OBJECTS
create_book = CreateBook(library.books, library._save_books)
read_book = ReadBook(library.books)
update_book = UpdateBook(library.books, library._save_books)
delete_book = DeleteBook(library.books, library._save_books)


# CREATE
@app.route("/create", methods=["POST"])
def create_route():
    data = request.json
    title = data.get("title")
    author = data.get("author")
    isbn = data.get("isbn")

    result = create_book.add_book(title, author, isbn)
    return jsonify({"message": result})


# READ (find book)
@app.route("/read/<isbn>", methods=["GET"])
def read_route(isbn):
    result = read_book.find_book(isbn)
    return jsonify(result)


# UPDATE - borrow
@app.route("/update/borrow/<isbn>", methods=["PUT"])
def borrow_route(isbn):
    result = update_book.borrow_book(isbn)
    return jsonify({"message": result})


# UPDATE - return
@app.route("/update/return/<isbn>", methods=["PUT"])
def return_route(isbn):
    result = update_book.return_book(isbn)
    return jsonify({"message": result})


# DELETE
@app.route("/delete/<isbn>", methods=["DELETE"])
def delete_route(isbn):
    result = delete_book.delete_book(isbn)
    return jsonify({"message": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
