# control.py #

# import #

import ui

# mainfunc #

def start(run):
    while run:
        selection = ui.main_menu()
        func_run = checkfunc(selection)
        print(func_run)

def checkfunc(selection):
    if selection == 1:
        return True
    elif selection == 2:
        return True
    elif selection == 3:
        return True
    elif selection == 4:
        return True
    elif selection == 5:
        return True
    elif selection == 6:
        return True
    elif selection == 7:
        return True
    else:
        return False # This for function run variable#
