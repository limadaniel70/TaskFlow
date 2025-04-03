# This project is licensed under the MIT License - see the LICENSE file for details.
from sqlite3 import Cursor

# class Task:
#    id: int | None
#    title: str
#    description: str | None
#    completed: int = 0


def get_tasks(cursor: Cursor) -> list[dict[str, str | int]]:
    """
    Retrieve all tasks from the database.
    Args:
        cursor (Cursor): The SQLite database cursor.
    Returns:
        tasks (list[dict[str, str | int]]): A list of tasks, where each task is represented as a dictionary
        containing its attributes (e.g., id, title, description, completed).
    """
    query = """SELECT * FROM Tasks"""
    cursor.execute(query)
    tasks = cursor.fetchall()
    return tasks


def add_task(cursor: Cursor, title: str, description: str | None):
    """
    Add a new task to the database.
    Args:
        cursor (Cursor): The SQLite database cursor.
        title (str): The title of the task.
        description (str | None): The description of the task. Can be None.
    """
    query = "INSERT INTO Tasks(title, description, completed) VALUES (?, ?, ?)"
    cursor.execute(query, (title, description, 0))


def update_task(cursor: Cursor, task_id: int, new_title: str, new_desc: str):
    """
    Update the title and description of an existing task.
    Args:
        cursor (Cursor): The SQLite database cursor.
        task_id (int): The ID of the task to update.
        new_title (str): The new title for the task.
        new_desc (str): The new description for the task.
    """
    query = "UPDATE Tasks SET title = ?, description = ? WHERE id = ?"
    cursor.execute(query, (new_title, new_desc, task_id))


def set_completed(cursor: Cursor, task_id: int):
    """
    Mark a task as completed in the database.
    Args:
        cursor (Cursor): The SQLite database cursor.
        task_id (int): The ID of the task to mark as completed.
    """
    query = "UPDATE Tasks SET completed = 1 WHERE id = ?"
    cursor.execute(query, (task_id,))


def delete_task(cursor: Cursor, task_id: int):
    """
    Delete a task from the database.
    Args:
        cursor (Cursor): The SQLite database cursor.
        task_id (int): The ID of the task to delete.
    """
    query = "DELETE FROM Tasks WHERE id = ?"
    cursor.execute(query, (task_id,))
