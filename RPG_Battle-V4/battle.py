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

    player.reset()
    monster.reset()

    player_alive  = True
    monster_alive = True

    while player_alive and monster_alive:
        player_action = ui.battle(player,monster)
        if player_action == 1:
            pass
        elif player_action == 2:
            pass
        elif player_action == 3:
            confirm = ui.ask_confirm("run")
            if confirm.lower() == "y":
                print()
                print(" === RUNNING ===")
                print()
                print(f"PLAYER  | {player.name} RUN OUT OF THE BATTLE")
                break