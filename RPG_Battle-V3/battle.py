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
    player_alive = True
    monster_alive = True
    player.restart()
    monster.restart()

    while player_alive and monster_alive:
        result = ui.battle(player,monster)
        if result == 1:
            player_damage = player.attack()
            monster_alive = monster.take_damage(player_damage)
        elif result == 2:
            player_heal = player.heal()
        elif result == 3:
            confirm = ui.ask_confirm("RUN")
            if confirm.lower() == "y":
                print(F" >>> PLAYER {player.name} | RUN OUT OF THE BATTLE")
                break
            else:
                continue
