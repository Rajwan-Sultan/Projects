import datetime
import uuid




class List:
    all_tasks = []
    completed = []
    incomplete = []


    def add(self, obj):  # ! Adds a task to the all_task list
        self.all_tasks.append(vars(obj))
        self.incomplete.append(vars(obj))


    def print_task(self):  # ! Prints all the tasks
        for i in self.all_tasks:
            print(f'\nTask No - {i["no"]}\nID: {i["id"]}\nTask - {i["name"]}\nCreated Time: {i["created_time"]}\nUpdated Time: {i["updated_time"]}\nCompleted: {i["task_done"]}\nCompleted Time: {i["completed_time"]}\n')


    def task_completed(self):  # ! Only Prints The Completed Task
        if len(self.completed) == 0:
            print("\nNo Task Is Yet Completed.\n")
        else:
            for i in self.completed:
                print(f'\nTask No - {i["no"]}\nID: {i["id"]}\nTask - {i["name"]}\nCreated Time: {i["created_time"]}\nUpdated Time: {i["updated_time"]}\nCompleted: {i["task_done"]}\nCompleted Time: {i["completed_time"]}\n')


    def task_incomplete(self):  # ! Only Prints The Inomplete Task
        if len(self.incomplete) == 0:
            print('\nNo Incomplete Task.\n')
        else:
            for i in self.incomplete:
                print(f'\nTask No - {i["no"]}\nID: {i["id"]}\nTask - {i["name"]}\nCreated Time: {i["created_time"]}\nUpdated Time: {i["updated_time"]}\nCompleted: {i["task_done"]}\nCompleted Time: {i["completed_time"]}\n')


    def task_update(self, no):  # ! Updates a Task
        for i in self.all_tasks:
            if i["no"] == no:
                x = input("Enter New Task: ")
                i["name"] = x
                i["updated_time"] = datetime.datetime.now().strftime(
                    "%d-%m-%Y  %H: %M: %S")
        print("\nTask Updated Successfully\n")


    def mark_done(self):  # ! Mark a Task as Completed
        print('\nSelect Which Task To Complete\n')
        x = int(input("Enter Task No: "))
        for i in range(len(self.incomplete)):
            if self.incomplete[i]["no"] == x:
                self.incomplete[i]["task_done"] = True
                self.incomplete[i]["completed_time"] = datetime.datetime.now().strftime(
                    "%d-%m-%Y  %H: %M: %S")
                self.completed.append(self.incomplete[i])
                self.incomplete.pop(i)
                break
        print("\nTask Completed\n")




class Task(List):
    def __init__(self, name):  # ! Initializes a new Task
        self.name = name
        self.task_done = False
        self.updated_time = "NA"
        self.created_time = datetime.datetime.now().strftime("%d/%m/%Y  %H: %M: %S")
        self.completed_time = "NA"
        self.id = uuid.uuid1()
        self.no = len(self.all_tasks)+1
        self.add(self)


    #! name  ,task_done, updated_time ,created_time , completed_time  ,id,no


    def update_task(self, no):  # ! Calls the task_update method
        self.task_update(no)


    def complete_task(self, no):  # ! Calls the mark_done method
        self.mark_done(no)




def main():
    x = """\n1. Add New Task
2. Show All Task
3. Show Incomplete Tasks
4. Show Completed Tasks
5. Update Task
6. Mark A Task as Completed
    """


    print(x)
    op = int(input("Enter Option: "))
    if op == 1:
        i = input("Enter New Task: ")
        obj = Task(i)
    elif op == 2:
        obj = List()
        obj.print_task()
    elif op == 3:
        obj = List()
        obj.task_incomplete()
    elif op == 4:
        obj = List()
        obj.task_completed()


    elif op == 5:
        obj = List()
        print("\nSelect Which Task To Update\n")
        obj.print_task()
        i = int(input("Enter Task No: "))
        obj.task_update(i)
    elif op == 6:
        obj = List()
        obj.mark_done()
    else:
        print("\n!!Invalid Input!!")




while True:
    main()


