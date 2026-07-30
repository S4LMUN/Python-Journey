# --- questions     --- #

# === default value === #

questions = [{
    "question":"Minecraft is sandbox game?",
    "choices":["Yes","No","Ok","Thank"],
    "answer":1
},
{   
    "question":"Text question",
    "choices":["This is correct","This is incorrect","Hello world","Banana"],
    "answer":1
}
]

question_load = []

# === main func     === #

def load_question():
    try:
        file = open("Questions.txt","r")
        question_load = file.readlines
        for question in question_load:
            print(question)
        file.close()
        
    except FileNotFoundError:
        file = open("Questions.txt","w")
        file.close()