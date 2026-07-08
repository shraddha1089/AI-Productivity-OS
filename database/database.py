import sqlite3

# -------------------------------------------------
# Create Database Connection
# -------------------------------------------------
conn = sqlite3.connect("tasks.db")

# Create a cursor
cursor = conn.cursor()

# -------------------------------------------------
# Create Tasks Table
# -------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    priority TEXT NOT NULL,
    due_date TEXT NOT NULL
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()