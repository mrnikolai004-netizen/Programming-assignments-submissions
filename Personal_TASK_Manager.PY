import sqlite3


# -----------------------------
# Database Connection Functions
# -----------------------------
def create_connection(db_file):
    """Create and return a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print("Database connection error:", e)
        return None


def setup_database(conn):
    """Create the tasks table if it does not already exist."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority TEXT,
                status TEXT
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print("Error creating table:", e)


# -----------------------------
# Database Operations
# -----------------------------
def add_task(conn, title, description, priority, status="Pending"):
    """Insert a new task into the database."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (title, description, priority, status)
            VALUES (?, ?, ?, ?)
            """,
            (title, description, priority, status)
        )
        conn.commit()
        print("Task added successfully.")
    except sqlite3.Error as e:
        print("Error adding task:", e)


def get_all_tasks(conn):
    """Return all tasks."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id")
    return cursor.fetchall()


def get_tasks_by_status(conn, status):
    """Return tasks matching a specific status."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM tasks WHERE status = ?",
        (status,)
    )
    return cursor.fetchall()


def update_task_status(conn, task_id, new_status):
    """Update the status of a task."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (new_status, task_id)
        )
        conn.commit()
        print("Task updated successfully.")
    except sqlite3.Error as e:
        print("Error updating task:", e)


def delete_task(conn, task_id):
    """Delete a task by ID."""
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()
        print("Task deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting task:", e)


# -----------------------------
# Display Function
# -----------------------------
def display_tasks(tasks):
    """Display tasks in a formatted table."""
    if not tasks:
        print("\nNo tasks found.\n")
        return

    print()
    print(f"{'ID':<5}{'Title':<20}{'Priority':<12}{'Status':<12}Description")
    print("-" * 70)

    for task in tasks:
        print(f"{task[0]:<5}{task[1]:<20}{task[3]:<12}{task[4]:<12}{task[2]}")

    print()


# -----------------------------
# Main Program
# -----------------------------
def main():
    conn = create_connection("tasks.db")

    if conn is None:
        return

    setup_database(conn)

    while True:
        print("\nPersonal Task Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Tasks by Status")
        print("4. Update Task Status")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Task title: ")
            description = input("Description: ")
            priority = input("Priority (High/Medium/Low): ")
            add_task(conn, title, description, priority)

        elif choice == "2":
            tasks = get_all_tasks(conn)
            display_tasks(tasks)

        elif choice == "3":
            status = input("Enter status (Pending/Completed): ")
            tasks = get_tasks_by_status(conn, status)
            display_tasks(tasks)

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            status = input("New status (Pending/Completed): ")
            update_task_status(conn, task_id, status)

        elif choice == "5":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(conn, task_id)

        elif choice == "6":
            print("Goodbye!")
            conn.close()
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()