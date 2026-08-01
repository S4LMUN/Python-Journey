# ---   character.py   --- #

# === default variable === #

# === class            === #

class Character:
    def __init__(self,hp,max_hp,damage,name):
        self.hp     = hp
        self.max_hp = max_hp
        self.damage = damage
        self.name   = name


    def attack(self,object_name):
        object_name.hp -= self.damage
        print(f"{self.name} Attack {object_name.name} {self.damage} Damage")