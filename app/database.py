# This project is licensed under the MIT License - see the LICENSE file for details.
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor


@contextmanager
def get_conn(db_name: str):
    """
    Context manager for creating and managing a SQLite database connection.

    This function ensures that the connection is properly established and closed,
    even if an exception occurs. The connection uses `row_factory` to return rows
    as dictionaries for easier access.
    Args:
        db_name (str): The name of the SQLite database file.
    Yields:
        sqlite3.Connection: A SQLite connection object with `row_factory` set
        to return rows as dictionaries.
    Ensures:
        The database connection is properly closed after use, even if an exception occurs.
    """
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # return dicts instead of tuples
    try:
        yield conn
    finally:
        conn.close()


def init_db(cursor: Cursor):
    """
    Initializes the database by creating a 'Tasks' table if it does not already exist.

    The 'Tasks' table contains the following columns:
    - id: An integer primary key that auto-increments.
    - title: A text field that cannot be null, representing the task title.
    - description: A text field for additional details about the task (optional).
    - completed: An integer field with a default value of 0, indicating whether
    the task is completed (0 for incomplete, 1 for complete).

    Args:
        cursor (Cursor): A database cursor object used to execute SQL queries.
    """
    query = """CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed INTEGER DEFAULT 0)"""
    cursor.execute(query)
