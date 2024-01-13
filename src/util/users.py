from src.entities.Player import *


class Usuario:
    def __init__(self, slime: Player, username, shop_coins=0, exp=0, ):
        self.file_path = os.path.join("../data", "users.dat")
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
        if user.username == self.username:
            return False
        return True
