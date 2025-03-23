# todo.py
tasks = []
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')


def list_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f'{idx}. {task}')

def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")


if __name__ == "__main__":
    add_task("Finish Assignment")
    list_tasks()
