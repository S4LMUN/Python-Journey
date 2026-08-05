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
            ui.battle_info()
            ui.attack_info(player,monster,player_damage)
            monster_alive = monster.take_damage(player_damage)
            player_alive = monster_turn(player)
        elif result == 2:
            player_heal = player.heal()
            if player_heal == 0:
                ui.not_allow(player)
                continue
            else:
                ui.battle_info()
                ui.heal_info(player,player_heal)
                player_alive = monster_turn(player)

        elif result == 3:
            confirm = ui.ask_confirm("RUN")
            if confirm.lower() == "y":
                print(F" >>> PLAYER {player.name} | RUN OUT OF THE BATTLE")
                break
            else:
                continue

def monster_turn(player):
    monster_result = monster.decide()
    monster_action,monster_damage = monster_result
    if monster_action == 1:
        player_alive = player.take_damage(monster_damage)
        ui.monster_ui(monster,monster_action,monster_damage,player)
        return player_alive
    else:
        ui.monster_ui(monster,monster_action,monster_damage,player)
        return True
