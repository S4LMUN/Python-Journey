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
    selection = ask_menu(1,7,"Func",1)
    return selection

def ask_menu(low,high,text,state):
    try:
        result = int(input(f" {">" * state} Select {text} : "))
        if low <= result <= high:
            return result
        else:
            print()
            print("Invalid Value")
            return None

    except ValueError:
        print()
        print("Value Error")
        return None

def add_task(state,text):
    new_task = input(f" {'>' * state} {text}: ")
    if new_task.strip() == "":
        return None
    else:
        return new_task

def confirm(state,text):
    confirm = input(f" {">" * state} confirm {text} : ")
    return confirm

def ask_task(state,todo):
    try:
        select = int(input(f" {">" * state} Select task : "))
        select -= 1
        if 0 <= select < len(todo.list):
            return select
        else:
            print()
            print(f"No task number {select + 1}")
            return None

    except ValueError:
        print()
        print("Value Error")

def delete_menu():
    print()
    print(" === DELETE MENU ===")
    print()
    print("1) Select Task")
    print("2) Clear  Task")
    print("3) Exit   Menu")
    print()
    result = ask_menu(1,3,"Func",2)
    return result
