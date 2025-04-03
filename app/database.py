# This project is licensed under the MIT License - see the LICENSE file for details.
import sqlite3
from contextlib import contextmanager
from sqlite3 import Cursor


@contextmanager
def get_conn(db_name: str):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # return dicts instead of tuples
    try:
        yield conn
    finally:
        conn.close()


def init_db(cursor: Cursor):
    query = """CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed INTEGER DEFAULT 0)"""
    cursor.execute(query)
