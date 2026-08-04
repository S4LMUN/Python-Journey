# === battle.py === #

# === import === #

from player import Player
from monster import Monster
import ui

# === default variable === #

player = Player("David", 100)
monster = Monster("Skeleton", 80)

# === main func === #

def start():
    ui.battle(player,monster)