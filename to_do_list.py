task=[]
def add_task(task1):
    task.append(task1)
    print(f"Your {task1} task was added")
def view_task():
    if not task:
        print("There are no tasks in the list")
    else:
        i=1
        for _ in task:
            print(f"{i}. {task[i-1]}")
            i+=1
def remove_task(task3):
    if task3>0 and task3<=len(task):
        to_remove=task.pop(task3-1)
        print(f"Your {task3} is removed")
    else:
        print("Invalid task number")
def update_task(task_4,task_input):
    if task_4>0 and task_4<=len(task):
        task[task_4-1]=task_input
        print(f"Your {task_input} task is updated")
    else:
        print("Invalid task number")
def mark_as_completed(task_5):
    if task_5>0 and task_5<=len(task):
        task[task_5-1]+="           ->completed"
        print(f"Your {task_5} task is marked as completed")
    else:
        print("Invalid task number")
def to_do_list():
    print("To do list:")
    print("1.Add task")
    print("2.View task")
    print("3.Remove task")
    print("4.Update task")
    print("5.Mark as completed")
    print("6.exit")
    while True:
        user_input=input("Choose your option: ")
        if user_input=='1':
            task_1=input("Enter the task to be added:  ")
            add_task(task_1)
        elif user_input=='2':
            view_task()
        elif user_input=='3':
            task_3=int(input("Enter the task number to remove:  "))
            remove_task(task_3)
        elif user_input=='4':
            task_4=int(input("Enter the task number to update:  "))
            task_input=input("Enter the task to be added: ")
            update_task(task_4,task_input)
        elif user_input=='5':
            task_5=int(input("Enter the task number to mark as completed:  "))
            mark_as_completed(task_5)
        elif user_input=='6':
            exit()
        else:
            print("Choose from the above options only")
if __name__=="__main__":
    to_do_list()