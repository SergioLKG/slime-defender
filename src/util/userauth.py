import json


class UserAuth:
    def __init__(self, file_path='userdata.json'):
        self.file_path = file_path
        self.user_data = self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.file_path, 'r') as file:
                user_data = json.load(file)
        except FileNotFoundError:
            user_data = {}
        return user_data

    def save_user_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.user_data, file, indent=2)

    def register_user(self, username):
        if username not in self.user_data:
            self.user_data[username] = {'click_count': 0}
            self.save_user_data()

    def load_user_game_data(self, username):
        if username in self.user_data:
            return self.user_data[username]
        else:
            return None

    def update_user_game_data(self, username, click_count):
        if username in self.user_data:
            self.user_data[username]['click_count'] = click_count
            self.save_user_data()


""" 
#  Ejemplo de uso:
    user_auth = UserAuth()
    
#  Ingresa un nuevo usuario
    user_auth.register_user("usuario1")
    
#  Carga datos de usuario
    user_data = user_auth.load_user_game_data("usuario1")
    if user_data:
        print(f"Datos de {username}: {user_data}")
    else:
        print(f"El usuario {username} no existe.") 
"""
