# === player.py === #

# === import === #

# === default variable === # 

# === main class === #

class Monster:
    def __init__(self,name,hp):
        self.name   = name
        self.max_hp = hp
        self.hp     = hp

    def reset(self):
        self.hp = self.max_hp