# --- questions     --- #

# === import        === #

import json

# === default value === #

questions = [
    {
        "question":"Minecraft is sandbox game?",
        "choices":["Yes","No","Ok","Thank"],
        "answer":1
    }
]

# === main func     === #

def load_question():
    global questions

    try:
        file = open("Questions.txt","r")

        questions = json.load(file)

        file.close()

        print("Import Question Success")

    except FileNotFoundError:
        print("No Questions To Import")
        print("Default Question Enable")

    except json.JSONDecodeError as error:
        print("JSON ERROR:")
        print(error)
