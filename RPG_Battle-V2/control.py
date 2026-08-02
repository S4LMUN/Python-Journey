# --- control.py       --- #

# === import           === #

from monster import Monster
from player  import Player
import ui

# === default variable === #

monster = Monster("Slime",50)
player  = Player("Josh",100)

# === main func        === #

def battle():
    player.hp = player.max_hp
    monster.hp = monster.max_hp

    while player.hp > 0 and monster.hp > 0:
        result = ui.battle(player,monster)
        if result is None:
            continue
        else:
            if result == 1:
                player_attack = player.attack()
                monster.hp -= player_attack
                print()
                print(f"Player  : {player.name} Attack Monster {monster.name} {player_attack} Damage")
                if monster.hp <= 0:
                    print()
                    print("Monster Die")
                else:
                    result = monster.chance()
            elif result == 2:
                player_heal = player.heal()
                print()
                print(f"Player  : {player.name} heal {player_heal} Hp")
                pass
            elif result == 3:
                confirm = ui.ask_confirm("Run")
                if confirm == "y":
                    print(f"Player  : {player.name} Run out of the battle")
                    break