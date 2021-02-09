from Books import Book
LIBRARY = set()


def add_book(book):
    LIBRARY.add(book)


def borrow_book(book):
    if not book.reserved:
        LIBRARY.remove(book)
        book.reserved = True
        LIBRARY.add(book)


def print_books(self):
    for book in LIBRARY:
        print(book.title, book.name_authors, book.reference)


def give_back_book(book):
    if book.reserved:
        LIBRARY.remove(book)
        book.reserved = False
        LIBRARY.add(book)


def add_books():
    books = [
        Book("Chocolat", "Tret", "054"),
        Book("Comment coder", "Mississilia", "078"),
        Book("Algorithmie", "Fret", "076"),
        Book("Psychologie", "Freud", "054")
    ]

    for book in books:
        add_book(book)

