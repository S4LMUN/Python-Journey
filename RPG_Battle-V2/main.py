# --- main.py          --- #

# === import           === #

import ui

# === default variable === #

run = True

# === main func        === #

while run:
    result = ui.main_menu()
    if result is None:
        continue
    else:
        if result == 1:
            pass
        elif result == 2:
            confirm = ui.ask_confirm("Exit")
            if confirm.lower() == "y":
                print("Exit")
                run = False
            else:
                continue