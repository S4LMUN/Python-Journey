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
        return result, damage
        
    def take_damage(self,damage):
        self.hp -= damage
        self.hp = max(self.hp,0)
        return self.hp > 0

    def heal(self):
        heal = random.randint(5,9)
        self.hp += heal
        self.hp = min(self.hp,self.max_hp)
        return heal

    def decided(self,target):
        if self.hp >= self.max_hp - 10:
            result, damage = self.attack(target)
            return result, damage, 1
        else:
            action = random.randint(1,2)
            if action == 1:
                result, damage = self.attack(target)
                return result, damage, 1
            elif action == 2:
                result = self.heal()
                return target.hp > 0,result, 2
