# ---       ui.py      --- #

# === default variable === #

# === main func        === #

def main_menu():
    print()
    print(" === RPG BATTLE ===")
    print()
    print("1) Start")
    print("2) Exit")
    print()
    result = ask_one(1,2)
    return result

def ask_one(low,high):
    try:
        select = int(input(" Select > "))
        if low <= select <= high:
            return select
        else:
            print(" >> Invalid Value")

    except ValueError:
        print(" >> Value Error")

def confirm(text):
    print()
    print(f" === {text} ===")
    print()
    result = input(f"Confirm {text} Y/N > ")
    return result
    

def battle_ui(object_player,object_monster):
    print()
    print(" === BATTLE ===")
    info(object_player)
    info(object_monster)

    print()
    print("1) Attack")
    print("2) Run")
    print()
    result = ask_one(1,2)
    print()
    return result

def info(object_name):
    print()
    print(f"Name : {object_name.name}")
    print(f"Hp   : {object_name.hp} | Attack Damage : {object_name.damage}")