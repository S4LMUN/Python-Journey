# === ui.py === #

# === import === #

# === default variable === # 

# === main func === #

def main_menu():
    print()
    print(" === RPG BATTLE V4 ===")
    print()
    print("1) Battle")
    print("2) Exit")
    print()
    result = ask_menu(1,2,"choice")
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

def ask_confirm(text):
    result = input(f" >> Confirm {text} y/n : ")
    return result

def battle(player,monster):
    print()
    print(" === BATTLE INFO ===")
    print()
    print(f"Player  | {player.name}  | Hp {player.hp}")
    print(f"Monster | {monster.name} | Hp {monster.hp}")
    print()
    print(" === ACTION MENU ===")
    print()
    print("1) Attack")
    print("2) Heal")
    print("3) Run")
    print()
    result = ask_menu(1,3,"action")
    return result

def attack(entity,damage,target):
    print(f"{entity.name} Attack {target.name} {damage} Hp")

def heal(entity,heal):
    print(f"{entity.name} Heal {heal} Hp")

def action():
    print()
    print(" === ACTION INFO ===")
    print()

def winner(player_alive,player,monster):
    print()
    print(" === BATTLE RESULT ===")
    if player_alive == True:
        print()
        print(f"Player  | {player.name}  Win")
        print(f"Monster | {monster.name} Lose")

    else :
        print()
        print(f"Monster | {monster.name} Win")
        print(f"Player  | {player.name}  Lose")        

def cannot(entity,do):
    print()
    print(" === CAN'T DO IT ===")
    print()
    print(f"{entity.name} can't {do}")