import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

conn.execute("""
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully ✅")