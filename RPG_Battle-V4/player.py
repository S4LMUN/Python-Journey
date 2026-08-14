# === player.py === #

# === import === #

import random

# === default variable === # 

# === main class === #

class Player:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     =  hp

    def reset(self):
        self.hp = self.max_hp

    def attack(self,target):
        damage = random.randint(1,7)
        result = target.take_damage(damage)
        return result, damage

    def take_damage(self,damage):
        self.hp -= damage
        self.hp = max(self.hp,0)
        return self.hp > 0

    def heal(self):
        if self.hp < self.max_hp:
            heal = random.randint(1,12)
            self.hp += heal
            self.hp = min(self.hp,self.max_hp)
            return heal,True
        else:
            return 0,False