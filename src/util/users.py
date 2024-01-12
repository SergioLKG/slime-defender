import json
from src.entities.Player import *


class Usuario:
    def __init__(self, slime: Player, username, shop_coins=0, exp=0, ):
        self.file_path = "../data/users.json"
        self.username = username
        self.shop_coins: int = shop_coins
        self.exp = exp
        self.slime: Player = slime

    def to_dict(self):
        return {"username": self.username, "shop_coins": self.shop_coins, "exp": self.exp}

    @classmethod
    def from_dict(cls, user_dict):
        return cls(user_dict["username"], user_dict["shop_coins"], user_dict["exp"])

    def comprobar_user(self, user):
        if user == self.user:
            return True
        return False

    def getCoins(self):
        return self.shop_coins


class UserManager:

    def guardarUser(user, filename):
        with open(filename, 'w') as file:
            json.dump(user.to_dict(), file)

    def cargarUser(filename):
        try:
            with open(filename, 'r') as file:
                user_dict = json.load(file)
                return Usuario.from_dict(user_dict)
        except FileNotFoundError:
            return None
