import tkinter as tk
from tkinter import messagebox

# Save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as f:
        for i in task_listbox.get(0, tk.END):
            f.write(i + "\n")

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

# Add a new task
def add_task():
    task = task_entry.get()
    if task:  # If not empty
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()
        if selected:
            task_listbox.delete(selected[0])
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")
    except:
        messagebox.showwarning("Warning", "No task selected!")

# Mark selected task as done
def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected[0])
        if not task.startswith("✅"):  # avoid double marking
            task_listbox.delete(selected[0])
            task_listbox.insert(selected[0], "✅ " + task)
            save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task to mark done!")

# --- GUI ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("420x480")

# Entry field for new task
task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_button.pack(pady=5)

# Frame for listbox + scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

# Task list display
task_listbox = tk.Listbox(frame, width=50, height=15, selectmode=tk.SINGLE, font=("Arial", 12))
task_listbox.pack(side=tk.LEFT)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Double click to mark as done
task_listbox.bind("<Double-1>", lambda e: mark_done())

# Load tasks at startup
load_tasks()

# Save tasks when closing
root.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), root.destroy()])

root.mainloop()
