# ---       ui.py      --- #

# ===      import      === #

# === default variable === #

# ===     main func    === #

def main_menu():
    print()
    print("=== Quiz Game V2 ===")
    print()
    print(" 1) Start Game")
    print(" 2) Exit  Game")
    print()

def ask_1(low,high,text):
    try:
        select = int(input(f"Select {text} > "))
        if low <= select <= high:
            return select
        else:
            print("Invalid Value")
            return
        
    except ValueError:
        print("Value Error")
        return

def ask_confirm(text):
    print()
    print(f"=== {text}")
    print()
    result = input(f"Do you wanna {text}? Y/N > ")
    if result.lower() == "y":
        print()
        print(f"Confirm {text}")
        return result
    else:
        print()
        print(f"Decline {text}")
        return "n"