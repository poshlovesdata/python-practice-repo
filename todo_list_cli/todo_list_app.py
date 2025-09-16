from typing import List


todo_list: List[str] = []

def line_seperator():
    """Seperate line for CLI"""
    print("#===========================#")

def add_task(task: str) -> None:
    """Add a task to the global todo_list.
    
Args:
    task (str): The description of the task.
"""
    todo_list.append(task)

def view_tasks() -> None:
    """View all tasks in global todo_list."""
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. | {item} |")

def delete_task(task_id: int) -> None:
    """Delete a task from the global todo_list.

Args:
    task_id (int): The number of the task on the list.
"""
    task_id -= 1
    if task_id >= len(todo_list) or task_id < 0:
        print("Invalid task number. Please select a valid task.")
    else:
        todo_list.pop(task_id)
    
def save_tasks_to_txt() -> None:
    """Save the contents of the global todo_list as text file (todo.txt)."""
    with open("todo.txt", "w") as f:
        for index, item in enumerate(todo_list, start=1):
            f.write(f"{index}. | {item} |\n")
    print("Changes saved to todo.txt")
      

if __name__ == "__main__":  
    while True:
        try:
            action_input = int(input(
                """Welcome to todo-cli
            Type a number to select an action:
            1. Add Task
            2. View All Tasks
            3. Delete Task
            4. Save Changes
            5. Exit
            """
            ))

        

            if action_input == 1:
                line_seperator()
                input_task = input("Add a new task: ")
                add_task(input_task)
                line_seperator()
            elif action_input == 2:
                line_seperator()
                view_tasks()
            elif action_input == 3:
                line_seperator()
                view_tasks()
                input_task_id = int(input("Type a task number to delete: "))
                delete_task(input_task_id)
            elif action_input == 4:
                line_seperator()
                save_tasks_to_txt() 
            elif action_input == 5:
                break
            else:
                print("Select a valid option")
        except ValueError:
            print("Input a number option")
            

    