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