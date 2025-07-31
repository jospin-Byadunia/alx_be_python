class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out_book(self):
        self._is_checked_out = True
        return self
    def return_book(self):
        self._is_checked_out = False
        return self

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out_book()
                return book
        return None

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return book
        return None

    def list_available_books(self):
        return [self._books]