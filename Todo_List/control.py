# control.py #

# import #

import ui
from todo import Todo

# mainfunc #

def start(run):
    todo = Todo()
    while run:
        selection = ui.main_menu()
        run = check_func(selection,todo)
        

def check_func(selection,todo):
    if selection == 1: # add task
        new_task = ui.add_task(2,"New task name ")
        todo.add_task(new_task)
        return True
    elif selection == 2: # delete task
        result = todo.is_list()
        if result is False:
            return True
        else:
            delete_menu(todo)
            return True
    elif selection == 3:
        return True
    elif selection == 4:
        result = todo.is_list()
        if result is False:
            return True
        else:
            edit(todo)
            return True
    elif selection == 5: # show task
        todo.show_task()
        return True
    elif selection == 6:
        return True
    elif selection == 7:
        result = confirm(2,"Exit")
        return result
    else:
        return True

def check_confirm(result):
    if result.lower() == "y":
        return True
    else:
        return False

def confirm(state,text):
    result = ui.confirm(state,text)
    confirm = check_confirm(result)
    if confirm:
        print()
        print(f"User {text}")
        return False
    else:
        return True

def edit(todo):
    task = ui.ask_task(2,todo)
    if task is None:
        return True
    else:
        edited = ui.add_task(3,f"Edit {todo.list[task]} task to ")
        if edit is None:
            return True
        else:
            todo.edit_task(task,edited)

def delete_menu(todo):
    select = ui.delete_menu()
    if select is None:
        return True
    else:
        if select == 1:
            task = ui.ask_task(3,todo)
            if task is None:
                return True
            else:
                unconfirm_delete = confirm(4,f"delete {todo.list[task]} task")
                if not unconfirm_delete:
                    todo.delete_task(task)
                    return True
                else:
                    print()
                    print("Nothing happen")
                    return True
        elif select == 2:
            unconfirm_delete = confirm(4,f"delete clear all task")
            if not unconfirm_delete:
                todo.clear_task()
                return True
            else:
                print()
                print("Nothing happen")
                return True
        else:
            print()
            print("Exit delete menu")
            return True
