# ---      main.py     --- #

# ===      import      === #

import ui
import quiz
import questions

# === default variable === #

run = True

# ===     main func    === #


questions.load_file_questions()
while run:
    ui.main_menu()
    main_menu_result = ui.ask_1(1,2,"func")
    if main_menu_result is None:
        continue
    else:
        if main_menu_result == 1:
            quiz.start_game()

        elif main_menu_result == 2:
            confirm_result = ui.ask_confirm("Exit")
            if confirm_result.lower() == "y":
                run = False
            else:
                continue