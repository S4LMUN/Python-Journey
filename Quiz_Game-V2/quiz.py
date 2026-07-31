# ---      quiz.py     --- #

# ===      import      === #

import questions
import ui

# === default variable === #

score = 0
total_question = 0

# ===     main func    === #

def start_game():
    global score
    global total_question

    score = 0
    total_question = 0

    for question in questions.questions:
        total_question += 1

        print()
        print(f"Question {question["question"]}")
        print()

        for index,choice in enumerate(question["choices"], start=1):
            print(f" {index}) {choice}")

        print()
        answer = ui.ask_1(1,4,"Answer")
        if answer == question["answer"]:
            print("Correct")
            score += 1
        else:
            correct_answer = question["answer"]
            print("Incorrect")
            print(f"The Answer is {question["choices"][correct_answer - 1]}")
            continue

    print()
    print(f"Score {score} / {total_question}")