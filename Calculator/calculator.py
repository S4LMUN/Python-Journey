# --- calculator.py --- #

# === import         === #

from history import History

# === value          === #

board = History()

# === class          === #

class Calculator:

    def plus(first, second):
        result = first + second
        board.history.append(f"{first} + {second} = {result}")
        return result

    def subtract(first, second):
        result = first - second
        board.history.append(f"{first} - {second} = {result}")
        return result

    def multiply(first,second):
        result = first * second
        board.history.append(f"{first} * {second} = {result}")
        return result

    def divide(first,second):
        result = first / second
        board.history.append(f"{first} / {second} = {result}")
        return result

    def power(first,second):
        result = first ** second
        board.history.append(f"{first} ** {second} = {result}")
        return result

    def square_root(first):
        result = first * 0.5
        board.history.append(f"√ {first} = {result}")
        return result
