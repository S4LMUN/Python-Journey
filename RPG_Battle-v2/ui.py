# --- ui.py            --- #

# === import           === #

# === default variable === #

# === main func        === #

def main_menu():
    print()
    print(" === RPG BATTLE ===")
    print()
    print("1) Play")
    print("2) Exit")
    print()
    result = ask_select(1,2,"func")
    return result

def ask_select(low,high,text):
    try:
        result = int(input(f"Select {text} > "))
        if low <= result <= high:
            return result
        else:
            print(" Invalid Value")
            return None

    except ValueError:
        print()
        print(" Value Error")
        return None

def ask_confirm(text):
    print()
    print(f" === {text} ===")
    print()
    result = input(f"Confirm {text} Y/n > ")
    return result

def battle(player,monster):
    print()
    print(" === BATTLE ZONE ===")
    print()
    print(f"Player  : {player.name} {player.hp} Hp")
    print(f"Monster : {monster.name} {monster.hp} Hp")
    result = battle_menu()
    return result

def battle_menu():
    print()
    print(" === ACTION ZONE ===")
    print()
    print("1) Attack")
    print("2) Heal")
    print("3) Run")
    print()
    result = ask_select(1,3,"action")
    return result