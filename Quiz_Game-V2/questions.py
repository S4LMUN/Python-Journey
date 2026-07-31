# ---   questions.py   --- #

# ===      import      === #

import json

# === default variable === #

questions = []

# ===     main func    === #

def load_file_questions ():
    global questions

    try:
        file = open("Questions.json","r")
        questions = json.load(file)
        file.close()

        print()
        print("*** Import Questions Success ***")

    except FileNotFoundError:
        file = open("Questions.json","w")
        file.close()

        load_default_questions()

        print()
        print("*** Use Default Questions ***")

    except json.JSONDecodeError:
        load_default_questions()

        print()
        print("*** No Questions to import ***")
        print("*** Use Default Questions ***")

def load_default_questions():
    global questions

    file = open("Questions_Default.json","r")
    questions = json.load(file)