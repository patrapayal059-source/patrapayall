import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "library.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not DB_PATH.exists():
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            year INTEGER
        )
        """)
        conn.commit()
        conn.close()

init_db()
