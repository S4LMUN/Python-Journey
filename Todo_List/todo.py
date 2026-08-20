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

    def show_task(self):
        print()
        if not self.list:
            print("You don't have any task")
        else:
            for index,task in enumerate(self.list, start = 1):
                print(f"{index}) {task}")

    def delete_task(self,task):
        self.list.pop(task)

    def clear_task(self):
        self.list.clear()

    def is_list(self):
        if not self.list:
            print()
            print("You don't have any task")
            return False
        else:
            return True

