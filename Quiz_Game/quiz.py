# --- quiz.py       --- #

# === default value === #

score = 0

# === import        === #

import ui
import questions

# === main func     === #

def quiz_start():
    global score
    score = 0

    ui.head_print("=== Start Quiz ===")
    print()
    if not questions.question_load:
        for question in questions.questions:
            print(question["question"])
            print()
            for index,choice in enumerate(question["choices"],start=1):
                print(f"{index}) {choice}")

            print()
            answer = ui.ask_select(1,4)
            if answer == question["answer"]:
                print(f"Correct Answer is {question["answer"]}")
                score += 1
                ui.show_score(score)
                continue

            else:
                print(f"Incorrect Answer is {question["answer"]}")
                ui.show_score(score)
                continue
    else:
        pass
