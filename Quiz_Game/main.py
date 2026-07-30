# --- main.py       --- #

# === import        === #

import ui
import quiz

# === default value === #

run = True

# === main loop     === #

while run:
    ui.main_menu()
    select = ui.ask_select(1,2)
    if select is None:
        continue
    else:
        if select == 1:
            quiz.quiz_start()

        else:
            ui.head_print("=== Exit ===")
            confirm = ui.ask_confirm("Exit")
            if confirm == "y":
                print("Exit program")
                print()
                run = False
            else:
                continue