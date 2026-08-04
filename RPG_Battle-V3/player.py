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

    def heal(self):
        heal = random.randint(4,7)
        self.hp += heal
        self.hp = min(self.hp,self.max_hp)
        return heal

    def take_damage(self,damage):
        self.hp -= damage
        self.hp = max(self.hp,0)
        return self.hp > 0

    def restart(self):
        self.hp = self.max_hp