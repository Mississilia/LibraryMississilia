class Book:
    # Livres avec titres et noms d'auteurs
    def __init__(self, title, name_authors, reference):
        self.title = title
        self.name_authors = name_authors
        self.reference = reference
        self.reserved = False

