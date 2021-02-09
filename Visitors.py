from Users import Users

class Visitors(Users):
    # voit le contenu de la bibliotheque, pas d'emprunt
    def __init__(self):
        super(Visitors, self).__init__(Users.Visitors)