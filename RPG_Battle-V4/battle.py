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
            monster_alive,player_damage = player.attack(monster)
            player_turn(player,player_damage,monster,1)
            if monster_alive is False:
                break
            else:
                player_alive, monster_value, monster_action = monster.decided(player)
                monster_turn(monster,monster_action,monster_value,player)    
        elif player_action == 2:
            player_heal = player.heal()
            player_turn(player,player_heal,monster,2)
            player_alive, monster_value, monster_action = monster.decided(player)
            monster_turn(monster,monster_action,monster_value,player)
        elif player_action == 3:
            confirm = ui.ask_confirm("run")
            if confirm.lower() == "y":
                print()
                print(" === RUNNING ===")
                print()
                print(f"PLAYER  | {player.name} RUN OUT OF THE BATTLE")
                break

def monster_turn(monster,monster_action,monster_value,target):
    if monster_action == 1:
        ui.attack(monster,monster_value,target)
    elif monster_action == 2:
        ui.heal(monster,monster_value)

def player_turn(player,player_value,target,action):
    ui.action()
    if action == 1:
        ui.attack(player,player_value,target)
    elif action == 2:
        ui.heal(player,player_value)