import sqlite3


# -------------------------------------------------
# Create Database
# -------------------------------------------------
def create_database():

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        priority TEXT NOT NULL,
        due_date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_task(task_name, priority, due_date):

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (task_name, priority, due_date)
        VALUES (?, ?, ?)
    """, (task_name, priority, due_date))

    conn.commit()

    conn.close()

def get_tasks():

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tasks
    """)

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def delete_task(task_id):

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    conn.commit()

    conn.close()

def update_task(task_id,task_name, priority, due_date):
    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
            UPDATE tasks
            SET
                task_name = ?,
                priority = ?,
                due_date = ?
            WHERE id = ?
    """, (task_name, priority,due_date,task_id))

    conn.commit()

    conn.close()
    
def get_task(task_id):
    
    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
            SELECT * from tasks
            WHERE id = ?
            """, (task_id,)) 
    
    task = cursor.fetchone()
    
    conn.close()
    
    return task
