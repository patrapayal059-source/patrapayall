 # UPDATE
class UpdateBook:
    def __init__(self, books, save_callback):
        self.books = books
        self._save_books = save_callback

    def borrow_book(self, isbn):
        ...

    def return_book(self, isbn):
        ...

