# === battle.py === #

# === import === #

from player import Player
from monster import Monster
import ui

# === default variable === # 

player = Player("Steve",120)
monster = Monster("Zombie",100)

# === main func === #

def start():
    while True:
        player_action = ui.battle(player,monster)