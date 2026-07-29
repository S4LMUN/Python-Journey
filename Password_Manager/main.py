# ---    main.py    --- #

# === import        === #

import ui
import control
import manager

# === default value === #

run = True

# === main loop     === #

manager.load_account()
while run:
    select = ui.main_menu()
    result = control.control_main_menu_func(select)
    if result == "exit":
        run = False
        print("Exit program")
        break

    else:
        continue
    