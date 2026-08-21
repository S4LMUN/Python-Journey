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
        in_program = add_task(todo)
        return in_program
    elif selection == 2: # delete task
        in_program = run_func(todo,delete_menu)
        return in_program
    elif selection == 3: # mark task
        in_program = run_func(todo,mark)
        return in_program
    elif selection == 4: # edit task
        in_program = run_func(todo,edit)
        return in_program
    elif selection == 5: # show task
        in_program = run_func(todo,show)
        return in_program
    elif selection == 6: # save task
        return True
    elif selection == 7: # exit
        in_program = confirm(2,"Exit")
        return in_program
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
        if edited is None:
            return True
        else:
            todo.edit_task(task,edited)
            return True

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
            unconfirm_delete = confirm(3,f"delete clear all task")
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

def mark(todo):
    task = ui.ask_task(2,todo)
    if task is None:
        return True
    else:
       todo.mark_task(task)  

def add_task(todo):
    new_task = ui.add_task(2,"New task name ")
    todo.add_task(new_task)
    return True

def show(todo):
    todo.show_task()

def run_func(todo,func):
    if not todo.list:
        print()
        print("You don't have any task")
        return True
    else:
        func(todo)
        return True
