# control.py #

# import #

import ui
from todo import Todo

# mainfunc #

def start(run):
    todo = Todo()
    while run:
        selection = ui.main_menu()
        func_run = checkfunc(selection,todo)

def checkfunc(selection,todo):
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
        return True
    else:
        return False # This for function run variable#
