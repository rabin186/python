import json
import os

def main():
    print("To Do List App")
    print("1. Add a task\n2. Display Tasks\n3. Mark a task as complete\n4. Delete a completed task\n5. Exit")
    choice = 0
    while choice != 5:
        choice = int(input("What's on your mind? "))
        match choice:  
            case 1:
                task = add_task()
                write(task)
            case 2:
                display_task()
            case 3:
                complete_task()
            case 4:
                delete_task()
            case 5:
                print("Exiting.")
            case _:
                print("Not a valid choice!")

def add_task():
    todo = input("What's up? ")
    due_date = input("What's it's due date (mm/dd)? ")
    completed_status = False
    return {'todo': todo,'due_date': due_date, 'status': completed_status}

def write(task):
    added_tasks = read_task()
    added_tasks.append(task)
    with open('todo_list.txt', 'w') as file:
        json.dump(added_tasks,file,indent=2)

def read_task():
    if not os.path.exists('todo_list.txt'):
        return []
    with open('todo_list.txt') as file:
        return json.load(file)
        

def display_task():
    added_tasks = read_task()
    for i, task in enumerate(added_tasks, start = 1):
        print(f'{i}.{task["todo"]}\t(Due_Date: {task["due_date"]})\t(Completed_Status: {task["status"]})')


def complete_task():
    added_tasks = read_task()
    display_task()
    task_no = int(input("Wow, Which no. task have you completed? "))
    if 1 <= task_no <= len(added_tasks):
        added_tasks[task_no-1]['status'] = True
        with open('todo_list.txt' , 'w') as file:
            json.dump(added_tasks, file, indent=2)

    else:
        print("Invalid task number.")  

def delete_task():
    added_tasks = read_task()
    display_task()
    n = int(input("Which no. task do you want to delete? "))
    if 1 <= n <= len(added_tasks):
        added_tasks.pop(n-1)
        with open('todo_list.txt' , 'w') as file:
            json.dump(added_tasks, file, indent=2)

    else:
        print("Invalid task number.")  


if __name__ == '__main__':
    main()

