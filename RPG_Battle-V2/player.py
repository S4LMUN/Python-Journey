# --- player.py        --- #

# === import           === #

import random

# === default variable === #

# === main Class       === #

class Player:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def attack(self):
        result = random.randint(1,5)
        return result

    def heal(self):
        result = random.randint(2,7)
        return result