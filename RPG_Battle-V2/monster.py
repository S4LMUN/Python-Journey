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
        self.hp += result
        self.hp = min(self.hp,self.max_hp)
        return result

    def chance(self):
        if self.hp >= self.max_hp - 10:
            result = self.attack()
            return result, "Attack"
        else:
            select = random.randint(1,2)
            if select == 1:
                result = self.attack()
                return result ,"Attack"

            elif select == 2:
                result = self.heal()
                return result ,"Attack"
            