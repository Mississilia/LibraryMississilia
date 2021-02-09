from Users import Users


class Librarians(Users):
    # add ->
    # ajoute et reference un nouveau livre dans la bibliotheque
    def __init__(self):
        super(Librarians, self).__init__(Users.Librarian)