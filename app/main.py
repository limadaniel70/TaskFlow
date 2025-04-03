# This project is licensed under the MIT License - see the LICENSE file for details.
from database import get_conn, init_db
from tasks import add_task, get_tasks

DB_NAME = "taskflow.db"

tasks = [
    {"title": "read", "desc": "read 1984"},
    {"title": "study", "desc": "study math"},
    {"title": "exercise", "desc": "go for a run"},
    {"title": "code", "desc": "work on Python project"},
]

with get_conn(DB_NAME) as conn:
    cursor = conn.cursor()
    tasks = get_tasks(cursor)
    for task in tasks:
        print(f"Title: {task["title"]}\nDescription: {task["description"]}")
