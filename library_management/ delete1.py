 # DELETE

class DeleteBook:
    def __init__(self, books, save_callback):
        self.books = books
        self._save_books = save_callback

    def delete_book(self, isbn):
        initial_len = len(self.books)
        self.books = [book for book in self.books if book.isbn != isbn]

        if len(self.books) < initial_len:
            self._save_books()
            return f"Book with ISBN {isbn} deleted successfully."
        else:
            return f"Book with ISBN {isbn} not found."
