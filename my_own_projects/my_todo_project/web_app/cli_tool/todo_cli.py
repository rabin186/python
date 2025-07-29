import argparse
from todo_utils import read_task, write_tasks

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
        add_task(args)
    elif args.command == 'delete':
        delete_task(args)
    elif args.command == 'list':
        list_task(args)
    elif args.command == 'complete':
        complete_task(args)

def add_task(args):
    tasks = read_task()
    task = {'todo': args.task, 'due_date': args.due, 'status': False}
    tasks.append(task)
    write_tasks(tasks)

def list_task(args):
    tasks = read_task()
    if args.all:
        show_tasks(tasks)
    elif args.completed:
        show_tasks([t for t in tasks if t['status']])
    else:
        show_tasks([t for t in tasks if not t['status']])

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f'{i}. {task["todo"]}\t(Due: {task["due_date"]})\t(Status: {"Completed" if task["status"] else "Pending"})')

def delete_task(args):
    tasks = read_task()
    if 1 <= args.task_no <= len(tasks):
        tasks.pop(args.task_no - 1)
        write_tasks(tasks)
    else:
        print("Invalid task number.")

def complete_task(args):
    tasks = read_task()
    if 1 <= args.task_no <= len(tasks):
        tasks[args.task_no - 1]['status'] = True
        write_tasks(tasks)
    else:
        print("Invalid task number.")

if __name__ == '__main__':
    main()

