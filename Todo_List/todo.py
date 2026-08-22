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
        for index,task in enumerate(self.list, start = 1):
            print(f"{index}) {task}")

    def delete_task(self,task):
        self.list.pop(task)

    def clear_task(self):
        self.list.clear()

    def edit_task(self,task,edited):
        self.list[task] = edited

    def mark_task(self,task):
        if "[✔] " not in self.list[task]:
            print()
            print(f"[✔] task {self.list[task]}")

            marked = self.list[task]
            self.list[task] = "[✔] " + marked
        else:
            print()
            print(f"{task + 1}) {self.list[task]} finished already")
            
    def is_list(self):
        if not self.list:
            print()
            print("You don't have any task")
            return False
        else:
            return True

    def load(self):
        try:
            file = open("todo.txt", "r")
            tasks = file.readlines()
            if tasks:
                for task in tasks:
                    if task.strip() == "":
                        continue
                    else:
                        print(f"Import task {task}")
                        self.list.append(task)
            else:
                print()
                print(" === No task in todo.txt ===")

        except FileNotFoundError:
            print()
            print(" === No task to import ===")
            file = open("todo.txt", "w")
        
        file.close()

    def save(self):
        print(" === Save Task ===")
        print()
        file = open("todo.txt","w")
        for task in self.list:
            print(f"Write task {task} to todo.txt")
            file.write(task + "\n")
        print()
        print("Save success full")
