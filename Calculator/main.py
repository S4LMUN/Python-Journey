# --- main.py --- #

# === import          === #

from control    import Control
from ui         import Ui

# === default value   === #

run = True

# === main loop       === #

Control.load_history()

while run:
    select_mainmenu = Ui.mainmenu()
    result = Control.select_func(select_mainmenu)
    if result == "exit":
        run = False