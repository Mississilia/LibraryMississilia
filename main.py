from Library import add_books, LIBRARY
from Members import Members
from UserType import UserTypes


def print_all_books():
    for book in LIBRARY:
        print(book.title, book.name_authors, book.reference)


def get_book_by_title(title):
    for book in LIBRARY:
        if book.title == title:
            return book


def main():
    add_books()
    print_all_books()
    member = Members('1', UserTypes.Members)
    book = get_book_by_title("Algorithmie")
    print("before borrowing: ", book.reserved)
    member.borrow(book)
    book = get_book_by_title("Algorithmie")
    print("after borrowing: ", book.reserved)


if __name__ == '__main__':
    main()
