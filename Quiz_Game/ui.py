# --- ui.py         --- #

# === main func     === #

def main_menu():
    print("\n=== Quiz Game ===")
    print()
    print(" 1) Start")
    print(" 2) Exit")
    print()

def ask_select(low,high):
    try:
        select = int(input("Select : "))
        if low <= select <= high:
            return select
        else:
            print(f"Invalid value")
            return

    except ValueError:
        print("ValueError")
        return

def ask_confirm(text):
    print()
    print(f"Do you wanna {text}?")
    confirm = input(f"Confirm {text} Y/N : ")
    if confirm.lower() == "y":
        return confirm
    else:
        return 

def show_score(variable):
    print()
    print(f"=== Status Now ===")
    print()
    print(f"Score {variable}")
    print()
    print("=== Status Now ===")
    print()

# === mini func      === #

def head_print(text):
    print()
    print(text)