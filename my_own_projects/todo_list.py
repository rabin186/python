tasks  = []

def main():
    print("To Do List App")
    print("1. Add a task\n2. Display Tasks\n3. Delete a completed task\n4. Exit")
    choice = 0
    while choice != 4:
        choice = int(input("What's on your mind? "))
        match choice:
            case 1:
                add_task()
                write()
            case 2:
                display_task()
            case 3:
                delete_task()
            case 4:
                print("Exiting.")
            case _:
                print("Not a valid choice!")

def add_task():
    task = input("What's up? ")
    tasks.append(task)

def write():
    with open('todo_list.txt', 'a') as file:
        file.write(f'{tasks[-1]}\n')

def read_task():
    added_tasks = []
    with open('todo_list.txt') as file:
        for line in file:
           added_tasks.append(line.rstrip())
    return added_tasks

def display_task():
    added_tasks = read_task()
    for i, task in enumerate(added_tasks, start = 1):
        print(f'{i}.{task}')

def delete_task():
    added_tasks = read_task()
    n = int(input("Wow, What have you completed? "))
    added_tasks.pop(n-1)
    with open('todo_list.txt' , 'w') as file:
        for task in added_tasks:
            file.write(f'{task}\n')

            
if __name__ == '__main__':
    main()

