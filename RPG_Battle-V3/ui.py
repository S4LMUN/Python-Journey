# === ui.py === #

# === default variable === #

def main_menu():
    print()
    print(" === RPG BATTLE Game ===")
    print()
    print("1) PLAY")
    print("2) EXIT")
    print()
    ask_menu(1,2,"Func")

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