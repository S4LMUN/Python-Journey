# ui.py #

def main_menu():
    print()
    print(" === Pokemon Info ===")
    print()
    result = ask_pokemon()
    return result

def ask_pokemon():
    result = input(" > Pokemon Name : ")
    if result.strip() != "":
        return result
    else:
        print()
        print("Try Again")
