# ui.py #

def main_menu():
    print()
    print(" === TODO LIST ===")
    print()
    print("1) Add    Task")
    print("2) Delete Task")
    print("3) Mark   Task")
    print("4) Edit   Task")
    print("5) Show   Task")
    print("6) Save   Task")
    print("7) Exit")
    print()
    selection = ask_menu(1,7,"Func")
    return selection

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
