# control.py #

# import #

import ui
from todo import Todo

# mainfunc #

def start(run):
    todo = Todo()
    while run:
        selection = ui.main_menu()
        run = check_func(selection,todo)
        

def check_func(selection,todo):
    if selection == 1: # add task
        new_task = ui.add_task()
        todo.add_task(new_task)
        return True
    elif selection == 2:
        return True
    elif selection == 3:
        return True
    elif selection == 4:
        return True
    elif selection == 5: # show task
        todo.show_task(todo)
        return True
    elif selection == 6:
        return True
    elif selection == 7:
        result = confirm(2,"Exit")
        return result
    else:
        return True

def check_confirm(result):
    if result.lower() == "y":
        return True
    else:
        return False

def confirm(state,text):
    result = ui.confirm(state,text)
    confirm = check_confirm(result)
    if confirm:
        print()
        print(f"User {text}")
        print() # ADD auto save task #
        return False
    else:
        return True
