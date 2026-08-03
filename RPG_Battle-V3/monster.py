# === monster.py === #

# === import === #

import random

# === class === #

class Monster:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp