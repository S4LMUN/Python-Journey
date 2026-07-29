# ---     ui.py     --- #

# === import        === #

import manager

# === main func     === #

def main_menu():
    print("\n === Password Manager ===\n")
    print("1) Add    Account")
    print("2) Show   Account")
    print("3) Search Account")
    print("4) Edit   Account")
    print("5) Delete Account")
    print("6) Save   Account")
    print("7) Load   Account")
    print("8) Clear  All")
    print("9) Exit\n")

    select = ask_main_menu(1,9)
    return select

# === ask func       === #

def ask_delete():
    if not manager.board:
        print("Don'have any account")
        return
    else:
        try:
            select = int(input(" Select Delete : "))
            select -= 1
            if 0 <= select <= len(manager.board):
                print()
                print(f"Website  : {manager.board[select]["website"]}")
                print(f"Name     : {manager.board[select]["username"]}")
                print(f"Password : {manager.board[select]["password"]}")
                print("Do you wanna delete real?")
                print()
                return select

            else:
                print("Account not found")
                return
    
        except ValueError:
            print("ValueError")

def ask_main_menu(x,y):
    try:
        select = int(input(" Select func : "))
        if x <= select <= y:
            print()
            return select

        else:
            print("func not found")
            return

    except ValueError:
        print("func not found")

def ask_account():
    web      = input("website  : ")
    if web.strip() == "":
        print("website can't name empty")
        return
    
    name     = input("username : ")
    if name.strip() == "":
        print("name can't name empty")
        return
    
    password = input("password : ")
    if password.strip() == "":
        print("password can't name empty")
        return
    
    return web,name,password

def ask_search():
    if not manager.board:
        print("Don't have any account")
    else:
        search = input("Search website : ")
        if search.strip() == "" and search:
            print("You can't search empty")
            return
        
        print()
        return search

def ask_edit():
    if not manager.board:
        print("Don't have any account")
        return
    else:
        try:
            dic = int(input("Select number : "))
            if 0 <= dic <= len(manager.board):
                dic -= 1
                print()
                print(f"Website  : {manager.board[dic]["website"]}")
                print(f"Name     : {manager.board[dic]["username"]}")
                print(f"Password : {manager.board[dic]["password"]}")
                print()
            else:
                print("You don't have that account")
        except ValueError:
            print("ValueError")
            return

        name_edit = input("Edit website,username,password : ")
        if name_edit.strip() == "":
            print("Answer can't be empty")
            return
        if name_edit not in ["website","username","password"]:
            print("Please choose one of this website,username,password")

        edit_to = input(f"From {name_edit} {manager.board[dic][name_edit]} Edit to : ")
        if edit_to.strip() == "":
            return
        
        return dic,name_edit,edit_to

def confirm():
    confirm = input("Confirm Y/N : ")
    if confirm.lower() == "y":
        print("Confirm")
        return "y"
    else:
        print("Cancel")
        return


# === mini func      === #