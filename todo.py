tasks = []

def add_task(task):
    tasks.append(task)

def complete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task completed!")
    else:
        print("Task not found.")

def display_tasks():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)

add_task("Buy groceries")
add_task("Finish homework")
display_tasks()
complete_task("Buy groceries")
display_tasks()
complete_task("Clean the house")
