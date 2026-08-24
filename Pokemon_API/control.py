# control.py #

import ui

def start():
    run = True
    while run:
        pokemon = ui.main_menu()
        if pokemon is None:
            continue
        else:
            pass

