# === main.py === #

# === import === #

import battle
import ui

# === default variable === # 

run = True

# === main func === #

while run:
    result = ui.main_menu()
    if result is None:
        continue
    else:
        if result == 1:
            battle.start()
        elif result == 2:
            confirm = ui.ask_confirm("exit")
            if confirm.lower() == "y":
                print()
                print(" === EXIT ===")
                print()
                run = False
            else:
                continue