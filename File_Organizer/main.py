# --- main.py       --- #

# === import        === #

import ui
import organizer

# === default value === #

run = True

# === main loop     === #

while run:
    ui.main_menu()
    path   = ui.ask_path()
    folder = organizer.show_files(path)
    if folder == None:
        continue
    else:
        files  = organizer.manage_file(path,folder)
        organizer.file_list(files)
        organizer.make_folders(path)
        organizer.move_files(path,"Images",organizer.image)
        organizer.move_files(path,"Videos",organizer.video)
        organizer.move_files(path,"Musics",organizer.music)
        organizer.move_files(path,"Projects",organizer.project)
        organizer.move_files(path,"Texts",organizer.text)