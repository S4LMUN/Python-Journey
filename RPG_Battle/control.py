# ---    control.py    --- #

# === import           === #

from character import Character
import ui

# === default variable === #

player = Character(100,10,"John")
monster = Character(50,20,"Slime")

# === main func        === #

def battle_info():
    ui.info(player)
    ui.info(monster)
