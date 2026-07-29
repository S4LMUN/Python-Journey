# --- ui.py         --- #

# === func          === #

def main_menu():
    print("\n === File Organizer ===\n")

    print("Terminal Ui")
    print("Organize File\n")

def ask_path():
    path = input("Enter folder path : ")
    if path.strip() == "":
        print("Path can't be empty")
    else:
        print(f" > Path {path}")
        return path

def print_files(folder):
    for file in folder:
        print(file)

def if_print(files_list,text,text2):
    if not files_list:
        return
    else:
        print()
        print(text)
        for file in files_list:
            print(f"File name {file} go to {text2}")