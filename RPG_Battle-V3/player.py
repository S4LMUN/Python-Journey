# === player.py === #

# === import === #

import random

# === class === #

class Player:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def attack(self):
        damage = random.randint(1,5)
        return damage