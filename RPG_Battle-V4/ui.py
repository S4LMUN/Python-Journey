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
    result = ask_menu(1,2,"Choice")
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