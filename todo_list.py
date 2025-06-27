def add_task():
    global task, tasks
    tasks = []
    task = str(input("Enter the task you want to perform:"))
    tasks.append(task)

def display():
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task}')

def remove():
    num = int(input("Enter the task to be removed: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)

def write():
    f = open('todo_list.txt' , 'a', encoding="utf-8")
    f.write(task)
    f.close()

def read():
    with open('todo_list.txt', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)



print("To do List")
global a
a = 0
while(a != 4):
    print("Choose what you want to do:")
    a = int(input("1. Add a task\n2. Display Tasks\n3. Delete a task\n4. Exit\n"))
    match a:
        case 1:
            add_task()
            write()
        case 2:
            display()
        case 3:
            remove()
        case 4:
            print("Exiting..")
        case _:
            print("Not a valid choice!")

read()
