# todo.py #

class Todo:
    def __init__(self):
        self.list = []

    def add_task(self,new_task):
        if new_task is None:
            print()
            print("Try again")
        else:
            self.list.append(new_task)

    def show_task(self,todo):
        print()
        if not todo.list:
            print("You don't have any task")
        else:
            for index,task in enumerate(self.list, start = 1):
                print(f"{index}) {task}")
