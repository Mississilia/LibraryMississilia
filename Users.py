from UserType import UserTypes

users = set()


class Users:
    def __init__(self, user_id, user_type):
        self.user_id = user_id
        self.value = user_type.value
        users.add(self)

    # va afficher tous les types d'utilisateurs
    def print_users(self):
        for user in users:
            print(user.user_id, user.user_type, user.value)


user = Users("abcd", UserTypes.Members)
