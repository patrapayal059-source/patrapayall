# READ
class ReadBook:
    def __init__(self, library):
        self.library = library

    def list_all_books(self):
        if not self.library.books:
            return "No books found."

        return [str(book) for book in self.library.books]

    def find_book(self, search_term):
        results = [
            book for book in self.library.books
            if search_term.lower() in book.title.lower()
            or search_term.lower() in book.author.lower()
            or search_term == book.isbn
        ]

        if not results:
            return "No books match your search."

        return [str(book) for book in results]
