# This project is licensed under the MIT License - see the LICENSE file for details.
from sqlite3 import Cursor

# class Task:
#    id: int | None
#    title: str
#    description: str | None
#    completed: int = 0


def get_tasks(cursor: Cursor) -> list[dict[str, str | int]]:
    query = """SELECT * FROM Tasks"""
    cursor.execute(query)
    tasks = cursor.fetchall()
    return tasks


def add_task(cursor: Cursor, title: str, description: str | None):
    query = "INSERT INTO Tasks(title, description, completed) VALUES (?, ?, ?)"
    cursor.execute(query, (title, description, 0))


def update_task(cursor: Cursor):
    cursor.execute("")
