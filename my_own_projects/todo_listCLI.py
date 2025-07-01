import json
import os
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='todo',
        description='A simple CLI-based To-Do List Manager to add, list, complete, and delete tasks.',
        epilog='Use "todo <command> -h" to get help on a specific command.'
    )
    subparsers = parser.add_subparsers(dest='command')

    addTask_parser = subparsers.add_parser('add', help='Add a new task to your list')
    addTask_parser.add_argument('--task', required=True, help='The task description')
    addTask_parser.add_argument('--due', required=True, help='Due date in mm/dd format')
    
    deleteTask_parser = subparsers.add_parser('delete', help='Delete a task by its number')
    deleteTask_parser.add_argument('--task_no', type=int, required=True, help='The task number to delete')

    listTask_parser = subparsers.add_parser('list', help='List your tasks')
    listTask_parser.add_argument('--all', action='store_true', help='Show all tasks')
    listTask_parser.add_argument('--completed', action='store_true', help='Show only completed tasks')
 
    completedTask_parser = subparsers.add_parser('complete', help='Mark a task as completed')
    completedTask_parser.add_argument('--task_no', type=int, required=True, help='The task number to mark as complete')

    args = parser.parse_args()
    if args.command == 'add':
        task = add_task(args)
        write(task)
    elif args.command == 'delete':
        delete_task(args)
    elif args.command == 'list':
        list_task(args)
    elif args.command == 'complete':
        complete_task(args)


def add_task(args):
    completed_status = False
    return {'todo': args.task,'due_date': args.due, 'status': completed_status}

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
        

def list_task(args):
    added_tasks = read_task()
    if args.all:
        for i, task in enumerate(added_tasks, start = 1):
            print(f'{i}.{task["todo"]}\t(Due_Date: {task["due_date"]})\t(Completed_Status: {task["status"]})')
    elif args.completed:
        for i, task in enumerate(added_tasks, start = 1):
            if task['status'] == True:
                print(f'{i}.{task["todo"]}\t(Due_Date: {task["due_date"]})\t(Completed_Status: {task["status"]})')
    else:
        for i, task in enumerate(added_tasks, start = 1):
            if task['status'] == False:
                print(f'{i}.{task["todo"]}\t(Due_Date: {task["due_date"]})\t(Completed_Status: {task["status"]})')

def delete_task(args):
    added_tasks = read_task()
    n = args.task_no
    if 1 <= n <= len(added_tasks):
        added_tasks.pop(n-1)
        with open('todo_list.txt' , 'w') as file:
            json.dump(added_tasks, file, indent=2)
    else:
        print("Invalid task number.")  

def complete_task(args):
    added_tasks = read_task()
    n = args.task_no
    if 1 <= n <= len(added_tasks):
        added_tasks[n-1]['status'] = True
        with open('todo_list.txt' , 'w') as file:
            json.dump(added_tasks, file, indent=2)
    else:
        print("Invalid task number.")  


if __name__ == '__main__':
    main()

