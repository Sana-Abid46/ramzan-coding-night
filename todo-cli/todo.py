import click #to create a cli
import json # To save and load tasks from a file 
import os # to check if a file exists

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open (TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """A simple todo list"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a task to the todo list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(click.style(f"Task added successfully: {task}", fg="green"))


@click.command()
def list():
    """List all tasks in the todo list"""
    tasks = load_tasks()
    if not tasks:
        click.echo(click.style("No tasks available", fg="yellow"))
        return
    for index, task in enumerate(tasks, 1):
        status = click.style("Done", fg="green") if task["done"] else click.style("NotDone", fg="red")
        click.echo(f"{index}. {task['task']} [{status}]")


@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(click.style(f"Task {task_number} marked as completed.", fg="green"))
    else:
        click.echo(click.style("Invalid task number", fg="red"))


@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the todo list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(click.style(f"Task {task_number} deleted: {removed_task['task']}", fg="green"))
    else:
        click.echo(click.style("Invalid task number", fg="red"))



cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()
