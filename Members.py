from Library import borrow_book
from Users import Users


class Members(Users):
    max_books = 3
    books = 0

    def borrow(self, book):
        if self.books == self.max_books:
            return print('can not borrow more than {} books'.format(self.max_books))
        self.max_books += 1
        borrow_book(book)

    def __init__(self, user_id, user_type):
        super().__init__(user_id, user_type)
