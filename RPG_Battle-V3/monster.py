# === monster.py === #

# === import === #

import random

# === class === #

class Monster:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def attack(self):
        damage = random.randint(3,8)
        return damage

    def heal(self):
        heal = random.randint(1,4)
        self.hp += heal
        self.hp = min(self.hp,self.max_hp)
        return heal