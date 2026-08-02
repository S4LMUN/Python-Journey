# --- monster.py       --- #

# === import           === #

import random

# === default variable === #

# === main Class       === #

class Monster:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def attack(self):
        result = random.randint(5,10)
        return result

    def heal(self):
        result = random.randint(1,3)
        return result