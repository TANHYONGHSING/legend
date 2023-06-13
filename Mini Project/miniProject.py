# Nelstrooy Galat Anak Parti 20DDT21F1045
# Nico Anak Empin 20DDT21F1006
# Tan Hyong Hsing 20DDT21F1002


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymssql


class TaskManager:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = None
        self.cursor = None

    def connect_to_database(self):
        try:
            self.conn = pymssql.connect(
                server=self.server,
                database=self.database,
                user=self.username,
                password=self.password,
            )
            self.cursor = self.conn.cursor(as_dict=True)
            messagebox.showinfo("Success", "Connected to the database.")
        except pymssql.Error as e:
            messagebox.showerror(
                "Error", f"An error occurred while connecting to the database:\n{e}"
            )
            exit()

    def add_task(self):
        add_window = tk.Toplevel()
        add_window.title("Add Task")
        add_window.geometry("500x400")

        frame_entry = tk.Frame(add_window)
        frame_entry.pack(pady=10)

        label_title = tk.Label(frame_entry, text="Title:", width=15, font=20)
        label_title.grid(row=0, column=0, padx=5, pady=5)
        entry_title = tk.Entry(frame_entry, width=30)
        entry_title.grid(row=0, column=1, padx=5, pady=5)

        label_description = tk.Label(
            frame_entry, text="Description:", width=15, font=20
        )
        label_description.grid(row=1, column=0, padx=5, pady=5)
        entry_description = tk.Entry(frame_entry, width=30)
        entry_description.grid(row=1, column=1, padx=5, pady=5)

        label_start_date = tk.Label(frame_entry, text="Start Date:", width=15, font=20)
        label_start_date.grid(row=2, column=0, padx=5, pady=5)
        entry_start_date = tk.Entry(frame_entry, width=30)
        entry_start_date.grid(row=2, column=1, padx=5, pady=5)

        label_due_date = tk.Label(frame_entry, text="Due Date:", width=15, font=20)
        label_due_date.grid(row=3, column=0, padx=5, pady=5)
        entry_due_date = tk.Entry(frame_entry, width=30)
        entry_due_date.grid(row=3, column=1, padx=5, pady=5)

        def save_task():
            title = entry_title.get()
            description = entry_description.get()
            start_date = entry_start_date.get()
            due_date = entry_due_date.get()

            try:
                self.cursor.execute(
                    "INSERT INTO Task_Entry (Title, Description, Start_Date, Due_Date) "
                    "VALUES (%s, %s, %s, %s)",
                    (title, description, start_date, due_date),
                )
                self.conn.commit()
                messagebox.showinfo("Success", "Task added successfully.")
                add_window.destroy()
            except pymssql.Error as e:
                messagebox.showerror(
                    "Error", f"An error occurred while adding the task:\n{e}"
                )

        button_add_task = tk.Button(frame_entry, text="Add Task", command=save_task)
        button_add_task.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def delete_task(self):
        delete_window = tk.Toplevel()
        delete_window.title("Delete Task")
        delete_window.geometry("800x500")

        frame_entry = tk.Frame(delete_window)
        frame_entry.pack(pady=10)

        label_task_id = tk.Label(frame_entry, text="Task ID:", width=8, font=20)
        label_task_id.grid(row=0, column=0, padx=5, pady=5)
        entry_task_id = tk.Entry(frame_entry, width=30)
        entry_task_id.grid(row=0, column=1, padx=5, pady=5)

        def view_tasks():
            self.view_tasks(delete_window)

        button_view_tasks = tk.Button(
            frame_entry, text="View Tasks", command=view_tasks
        )
        button_view_tasks.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        def confirm_delete_task():
            task_id = entry_task_id.get()
            if task_id:
                confirmed = messagebox.askyesno(
                    "Confirm Delete", "Are you sure you want to delete this task?"
                )
                if confirmed:
                    try:
                        self.cursor.execute(
                            "DELETE FROM Task_Entry WHERE TaskID = %s", (task_id,)
                        )
                        self.conn.commit()
                        messagebox.showinfo("Success", "Task deleted successfully.")
                        delete_window.destroy()
                    except pymssql.Error as e:
                        messagebox.showerror(
                            "Error", f"An error occurred while deleting the task:\n{e}"
                        )
            else:
                messagebox.showwarning("Warning", "Please enter a valid Task ID.")

        button_delete_task = tk.Button(
            frame_entry, text="Delete Task", command=confirm_delete_task
        )
        button_delete_task.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def view_tasks(self, window=None):
        if window is None:
            window = tk.Toplevel()
        else:
            window.title("View Tasks")
            window.geometry("600x500")

        frame_tasks = tk.Frame(window)
        frame_tasks.pack(pady=10)

        # Create the Treeview widget
        treeview = ttk.Treeview(
            frame_tasks,
            columns=("TaskID", "Title", "Description", "Start_Date", "Due_Date"),
            show="headings",
        )
        treeview.pack()

        # Configure column headings
        treeview.heading("TaskID", text="Task ID")
        treeview.heading("Title", text="Title")
        treeview.heading("Description", text="Description")
        treeview.heading("Start_Date", text="Start Date")
        treeview.heading("Due_Date", text="Due Date")

        # Remove indentation
        style = ttk.Style()
        style.configure("Treeview", indent=0)

        scrollbar_tasks = ttk.Scrollbar(
            frame_tasks, orient="vertical", command=treeview.yview
        )
        scrollbar_tasks.pack(side="right", fill="y")
        treeview.configure(yscroll=scrollbar_tasks.set)

        try:
            self.cursor.execute("SELECT * FROM Task_Entry")
            tasks = self.cursor.fetchall()
            for task in tasks:
                # Insert task data into the treeview
                treeview.insert(
                    "",
                    tk.END,
                    values=(
                        task["TaskID"],
                        task["Title"],
                        task["Description"],
                        task["Start_Date"],
                        task["Due_Date"],
                    ),
                )
        except pymssql.Error as e:
            messagebox.showerror(
                "Error", f"An error occurred while loading tasks:\n{e}"
            )

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        messagebox.showinfo("Success", "Disconnected from the database.")
        exit()


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("500x400")

    # Create a label for welcome message
    label_welcome = tk.Label(
        root, text="Welcome to your personal Task Management!", font=("Arial", 16)
    )
    label_welcome.pack(pady=10)

    # Create a frame for buttons
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(pady=20)

    # Create an instance of the TaskManager class
    task_manager = TaskManager(
        server="Nelstrooy", database="TASKMANAGER", username="sa", password="112803"
    )

    # Connect to the database
    task_manager.connect_to_database()

    # Create buttons
    button_add = tk.Button(
        frame_buttons,
        text="Add Task",
        command=task_manager.add_task,
        font=("Arial", 14),
    )
    button_add.grid(row=1, column=3, padx=10, pady=10)

    button_delete = tk.Button(
        frame_buttons,
        text="Delete Task",
        command=task_manager.delete_task,
        font=("Arial", 14),
    )
    button_delete.grid(row=2, column=3, padx=10, pady=10)

    button_view = tk.Button(
        frame_buttons,
        text="View Tasks",
        command=task_manager.view_tasks,
        font=("Arial", 14),
    )
    button_view.grid(row=3, column=3, padx=10, pady=10)

    button_exit = tk.Button(
        frame_buttons,
        text="Exit",
        command=task_manager.close_connection,
        font=("Arial", 14),
    )
    button_exit.grid(row=4, column=3, padx=10, pady=10)

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
