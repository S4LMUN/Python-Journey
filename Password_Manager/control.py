# ---  control.py   --- #

# === import        === #

import manager
import ui

# === main func     === #

def control_main_menu_func(select):
    if select is None:
        return

    if select == 1:
        result = ui.ask_account()
        if result is None:
            return
        else:
            web,name,password = result
            manager.add_account(web,name,password)

    elif select == 2:
        manager.show_account()

    elif select == 3:
        search = ui.ask_search()
        manager.search_account(search)

    elif select == 4:
        result = ui.ask_edit()
        if result is None:
            return
        else:
            number,edit,edit_to = result
            confirm = ui.confirm()
            if confirm == "y":
                manager.edit_account(number,edit,edit_to)
            else:
                return

    elif select == 5:
        select = ui.ask_delete()
        if select is None:
            return
        confirm =ui.confirm()
        if confirm == "y":
            manager.delete_account(select)
        else:
            return

    elif select == 6:
        manager.save_account()

    elif select == 7:
        manager.load_account()

    elif select == 8:
        print("Do you wanna delete all of this?")
        confirm =ui.confirm()
        if confirm == "y":
            manager.clear_account()
        else:
            return

    elif select == 9:
        print("Do you wanna exit (Auto save file if exit)")
        confirm =ui.confirm()
        if confirm == "y":
            manager.save_account()
            return "exit"
        else:
            return
