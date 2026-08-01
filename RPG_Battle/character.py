# ---   character.py   --- #

# === default variable === #

# === class            === #

class Character:
    def __init__(self,hp,damage,name):
        self.hp     = hp
        self.damage = damage
        self.name   = name

    def attack(self,object_name):
        self