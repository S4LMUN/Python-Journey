# === main.py  === #

# === import === #

import ui
import battle

# === default variable === #

run = True

# === main loop === #

while run:
    result = ui.main_menu()
    if result is None:
        continue
    else:
        if result == 1:
            battle.start()
        elif result == 2:
            confirm = ui.ask_confirm("EXIT")
            if confirm.lower() == "y":
                print(" >>> Exit")
                run = False
            else:
                continue
