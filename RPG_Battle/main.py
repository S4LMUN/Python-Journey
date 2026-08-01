# ---      main.py     --- #

# === import           === #

import control
import ui

# === default variable === #

run = True

# === main loop        === #

while run:
    select_result = ui.main_menu()
    if select_result is None:
        continue
    else:
        if select_result == 1:
            control.battle()
        elif select_result == 2:
            confirm_result = ui.confirm("Exit")
            if confirm_result.lower() == "y":
                print()
                print("Exit Program")
                run = False
            else:
                print()
