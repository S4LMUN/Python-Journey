# --- control.py --- #

# === import         === #

from calculator import Calculator
from calculator import board
from ui         import Ui

# === class          === #

class Control:
    def select_func(select):
        if select == 1:
            result = Control.cal_result(Calculator.plus,"+")
            if result is None:
                return

        elif select == 2:
            result = Control.cal_result(Calculator.subtract,"-")
            if result is None:
                return

        elif select == 3:
            result = Control.cal_result(Calculator.multiply,"*")
            if result is None:
                return

        elif select == 4:
            result = Control.divide_result(Calculator.divide,"/")
            if result is None:
                return

        elif select == 5:
            result = Control.cal_result(Calculator.power,"**")
            if result is None:
                return

        elif select == 6:
            result = Control.square_root_result(Calculator.square_root,"√")
            if result is None:
                return

        elif select == 7:
            for text in board.history:
                print(text)
            return

        elif select == 8:
            file = open("history.txt","w")
            for text in board.history:
                file.write(text + "\n")
            file.close
            return

        elif select == 9:
            confirm = Ui.ask_confirm()
            if confirm == "y":
                print("Clear history")
                board.history.clear()
                file = open("history.txt","w")
                file.close()
            else:
                return

        elif select == 10:
            confirm = Ui.ask_confirm()
            file = open("history.txt","w")
            for text in board.history:
                file.write(text + "\n")
            file.close()
            return "exit"

    def cal_result(func,text):
        ask_result = Ui.ask_2number()
        if ask_result is None:
            print("ValueError")
            return
        else:
            first,second = ask_result
            result = func(first,second)
            Ui.func_doing(first,second,text,result)
            return ask_result

    def divide_result(func,text):
        ask_result = Ui.ask_2number()
        if ask_result is None:
            print("ValueError")
            return
        else:
            first,second = ask_result
            if first == 0 or second == 0:
                print("ValueError")
                return
            else:
                result = func(first,second)
                Ui.func_doing(first,second,text,result)
                return ask_result

    def square_root_result(func,text):
        ask_result = Ui.ask_1number()
        if ask_result is None:
            print("ValueError")
            return
        else:
            first = ask_result
            result = func(first)
            Ui.func_doing_square(first,text,result)
            return ask_result

    def load_history():
        try:
            file = open("history.txt","r")
            load = file.readlines()
            for history in load:
                board.history.append(history.strip())
            file.close()

        except FileNotFoundError:
            file = open("history.txt","w")
            file.close()

