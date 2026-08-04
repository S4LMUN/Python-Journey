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

    def decide(self):
        if self.hp < self.max_hp - 10:
            result = random.randint(1,2)
            if result == 1:
                damage = self.attack()
                return damage
            elif result == 2:
                heal = self.heal()
                return heal
        else:
            damage = self.attack()
            return damage

    def take_damage(self,damage):
        self.hp -= damage
        self.hp = max(self.hp,0)
        return self.hp > 0

    def restart(self):
        self.hp = self.max_hp