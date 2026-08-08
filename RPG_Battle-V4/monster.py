# === player.py === #

# === import === #

import random

# === default variable === # 

# === main class === #

class Monster:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def reset(self):
        self.hp = self.max_hp

    def attack(self,target):
        damage = random.randint(3,10)
        result = target.take_damage(damage)
        return result
        
    def take_damage(self,damage):
        self.hp -= damage
        self.hp = max(self.hp,0)
        return self.hp > 0