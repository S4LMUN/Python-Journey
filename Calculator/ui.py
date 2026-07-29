# --- ui.py --- #

# === class          === #

class Ui:
    def ask_2number():
        try:
            first_number  = int(input("\nPress first number: "))
            second_number = int(input("Press second number: "))
            return first_number, second_number
        
        except ValueError:
            print("ValueError")
            return

    def ask_main_number(low,high):
        try:
            select = int(input("Press func number: "))
            if low <= select <= high:
                return select
            else:
                print("ValueError")
                return

        except ValueError:
            print("ValueError")
            return

    def ask_confirm():
        select = input("Press confirm y/n: ")
        if select.lower() == "y":
            print("Confirm")
            return "y"
        else:
            print("No")
            return "n"

    def ask_1number():
        try:
            select = int(input("Press number: "))
            return select

        except ValueError:
            print("ValueError")
            return

    def mainmenu():
        print("\n=== Calculator === \n")

        print(" 1) Add")
        print(" 2) Subtract")
        print(" 3) Multiply")
        print(" 4) Divide")
        print(" 5) Power")
        print(" 6) Square Root")
        print(" 7) Show History")
        print(" 8) Save History")
        print(" 9) Clear History")
        print("10) Exit\n")
        select = Ui.ask_main_number(1,10)
        return select

    def func_doing(first,second,text,result):
        print(f"\n{first} {text} {second} \nResult = {result}")

    def func_doing_square(first,text,result):
        print(f"\n{text} {first} \nResult = {result}")
