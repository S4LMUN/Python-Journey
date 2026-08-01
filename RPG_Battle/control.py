# ---    control.py    --- #

# === import           === #

from character import Character
import ui

# === default variable === #

player = Character(100,100,10,"John")
monster = Character(50,50,20,"Slime")

# === main func        === #

def battle():
    player.hp  = player.max_hp
    monster.hp = monster.max_hp
    while player.hp > 0 and monster.hp > 0:
        result = ui.battle_ui(player,monster)
        if result == 1:
            player.attack(monster)
            if monster.hp <= 0:
                print()
                print(f"Monster : {monster.name} Die")
                print(f"Player  : {player.name} Win")
                break
            else:
                monster.attack(player)
                if player.hp <= 0:
                    print()
                    print(f"Player  : {player.name} Die")
                    print(f"Monster : {monster.name} Win")
                    break
        else:
            print("Player run out of the battle")
            break

