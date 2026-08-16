# === ui.py === #

# === default variable === #

# === main func === #

def main_menu():
    print()
    print(" === RPG BATTLE Game ===")
    print()
    print("1) PLAY")
    print("2) EXIT")
    print()
    result = ask_menu(1,2,"Func")
    return result

def ask_menu(low,high,text):
    try:
        result = int(input(f" > Select {text} : "))
        if low <= result <= high:
            return result
        else:
            print("Invalid Value")
            return None
    except ValueError:
        print("Value Error")
        return None

def battle(player,monster):
    print()
    print(" === BATTLE ZONE ===")
    print()
    print(f"Player  : {player.name} | HP {player.hp}")
    print(f"Monster : {monster.name} | HP {monster.hp}")
    print()
    print(" === ACTION ZONE ===")
    print()
    print("1) ATTACK")
    print("2) HEAL")
    print("3) RUN")
    print()
    result = ask_menu(1,3,"Action")
    return result

def ask_confirm(text):
    result = input(f" >> Confirm {text} y/n : ")
    return result

def heal_info(target,value):
    print(f"{target.name} | HEAL {value} HP")

def attack_info(attacker,target,value):
    print(f"{attacker.name} ATTACK | {target.name} {value} HP")

def battle_info():
    print()
    print(" === BATTLE INFO ===")
    print()

def not_allow(target):
    print()
    print(" === NOT ALLOW ===")
    print()
    print(f"CAN'T HEAL IF FULL HP {target.max_hp}")

def monster_ui(monster,actions,number,player):
    action = actions        
    value = number
    if action == 1:
        attack_info(monster,player,value)
    elif action == 2:
        heal_info(monster,value)

def win_lose(entity,text,lost,text2):
    print()
    print(" === WINNER ===")
    print()
    print(f"{text} | {entity.name}")
    print()
    print(" === LOSE ===")
    print()
    print(f"{text2} | {lost.name}")