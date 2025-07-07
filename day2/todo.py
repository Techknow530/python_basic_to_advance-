from tabulate import tabulate


class Todo:
    def __init__(self):

        self._tdo = {}
        

    def new_task(self,title,discription):
        title = title.lower()
        self._todo[title] = discription
        self.show_task()
    
    def edit_task(self):
        self.show_task()
        task_name=input("which task you want to edit type it's name:").strip().lower()
        low_dic = {k.lower():v for k , v in self._todo.items()}
        
    
        if task_name in low_dic.keys():
            new_disc=input(f"Enter discription for {task_name} :")
            self._todo[task_name]=new_disc
        else:
            print("invalid task name")
            user = input("you want to edit task continue (y/n) :").lower()
            if user == 'y' or user == 'yes':

                self.edit_task()

            else:
                self.main_loop()
    
    def delete_task(self):
        self.show_task()
        task_name=input("which task you want to edit type it's name:").strip().lower()
        low_dic = {k.lower():v for k , v in self._todo.items()}
        
    
        if task_name in low_dic.keys():
            new_disc=input(f"Enter discription for {task_name} :")
            del(self._todo[task_name])
        else:
            print("invalid task name")
            user = input("you want to edit task continue (y/n) :").lower()
            if user == 'y' or user == 'yes':

                self.delete_task()

            else:
                self.main_loop()
        

    def show_task(self):
        print("It's all your task list \n"
        "========================================")
        # for key , val in self._todo.items():
        #     print(f"{key} : '{val}'")

        table = [(tasks,discription) for tasks , discription in self._todo.items()]
        print(tabulate(table ,headers=["Task-Name ","Task-Discription"],tablefmt="grid"))

        print("\n =============================")
        

    def main_loop(self):
        while True:
            print("\n \n============================\n" \
            "1. Enter for New Task  \n" \
            "2. Enter For Edit Anytask \n" \
            "3. Enter for delete any Task \n" \
            "4. Enter for show all task \n" \
            "==============================\n \n" )
            ch = int(input("Enter Your choice :").strip())
            
            choice = [1,2,3,4]
            if ch in choice:
                if ch == 1 :
                    print("creating a New todo list \n" \
                    "-----------------------------------------")
                    title = input("Enter your title for new Todo List :")
                    discription=input(f"enter Discription for '{title}' :")
                    self.new_task(title , discription)
                    

                elif ch ==2 :
                    print("\n Editing exsiting record \n" \
                    "-------------------------------- ")
                    self.show_task()
                    self.edit_task()
                elif ch == 3 :
                    print("\n Deleting exsiting record \n" \
                    "-------------------------------- ")
                    self.delete_task()

                elif ch == 4:
                    self.show_task()
            else:
                print("\n-------------------------" \
                "\n ! Enter value between given choice \n" \
                "-----------------------------! ")
                

task = Todo ()
task.main_loop()



