# --- organizer.py  --- #

# === import        === #

import os
import ui
import shutil

# === default value === #

image   = []
music   = []
video   = []
project = []
text    = []

folders = [
    "Images",
    "Videos",
    "Musics",
    "Projects",
    "Texts"
]

# === func          === #

def show_files(path):
    try:
        folder = os.listdir(path)
        print()
        ui.print_files(folder)
        return folder
    except FileNotFoundError:
        print("File Not Found")

def manage_file(path,folder):
    files     = []
    not_files = []

    print("\n > Check files in the folder")
    print("=== All Files")

    for filename in folder:
        full_path = os.path.join(path,filename)
        if os.path.isfile(full_path):
            files.append(filename)
            print(filename)
        else:
            not_files.append(filename)

    print("\n=== Not Files")
    ui.print_files(not_files)

    return files

def file_list(files):
    image.clear()
    video.clear()
    music.clear()
    project.clear()
    text.clear()
    
    for filename in files:
        if filename.endswith((".png",".jpg",".jpeg",".gif")):
            image.append(filename)
        elif filename.endswith((".mp4",".mov")):
            video.append(filename)
        elif filename.endswith(".mp3"):
            music.append(filename)
        elif filename.endswith((".js",".py",".html",".css")):
            project.append(filename)
        elif filename.endswith(".txt"):
            text.append(filename)

    ui.if_print(image,"=== Image","Image")
    ui.if_print(video,"=== Video","Video")
    ui.if_print(music,"=== Music","Music")
    ui.if_print(project,"=== Project","Project")
    ui.if_print(text,"=== Text","Text")

def make_folders(path):
    print()
    print("=== Check and make folder for organize")

    for folder in folders:
        print(f"Check and make folder {folder}")
        os.makedirs(
            os.path.join(path,folder),
            exist_ok=True
        )

def move_files(path,folder_name,files_list):
    if not files_list:
        return
    else:
        print()
        print("=== Move files")
        for filename in files_list:
            source = os.path.join(path,filename)
            destination = os.path.join(path,folder_name,filename)

            shutil.move(source,destination)
            print(f"Move file name {filename} to Folder {folder_name}")