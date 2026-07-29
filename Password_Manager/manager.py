# ---  manager.py   --- #

# === default value === #

board = []

# === main func     === #

def add_account(website,name,password):
    board.append(
        {"website":(website),
        "username":(name),
        "password":(password)
        }
    )

def show_account():
    if not board:
        print("Don't have any account")
    else:
        for index,dic in enumerate(board, start=1):
            print (f"{index}) ===")
            print_account(dic)

def search_account(name_website):
    for dic in board:
        if dic["website"] == name_website:
            print_account(dic)
        else:
            print("Account not found")

def edit_account(number,edit,edit_to):
    board[number][edit] = edit_to

def delete_account(number):
    if not board:
        print("Don'have any account")
    else:
        board.pop(number)
        print("You delete")

def save_account():
    if not board:
        print("Don'have any account")
        return
    else:
        file = open("Password_manager.txt","w")
        for dic in board:
            file.write(dic["website"] + "\n")
            file.write(dic["username"] + "\n")
            file.write(dic["password"] + "\n")
        file.close()
        print("You save account to Password_manager.txt")            

def load_account():
    board.clear()
    try:
        file = open("Password_manager.txt","r")
        note = file.readlines()
        note_board = []
        for account in note:
            note_board.append(account.strip())
        for i in range(0, len(note_board), 3):
            board.append(
                {
                "website":(note_board[i]),
                "username":(note_board[i + 1]),
                "password":(note_board[i + 2])
                }
            )
        file.close()
        print("Load success full")
        
    except FileNotFoundError:
        file = open("Password_manager.txt","w")
        file.close()
        print("You make Password_manager.txt")
        return[]

    if not board:
        print("You don't have any account")

def clear_account():
    if not board:
        print("Don't have any account")
    else:
        print("You delete all account (Not auto save)")
        board.clear()

# === mini func      === #

def print_account(name):
    print(f"Website  : {name["website"]}")
    print(f"Name     : {name["username"]}")
    print(f"Password : {name["password"]}")
    print()
