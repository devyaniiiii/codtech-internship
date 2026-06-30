from tkinter import *

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(END, task)
        task_entry.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = Tk()
root.title("To-Do List")

task_entry = Entry(root, width=30)
task_entry.pack(pady=10)

Button(root, text="Add Task", command=add_task).pack()
Button(root, text="Delete Task", command=delete_task).pack()

listbox = Listbox(root, width=40, height=10)
listbox.pack(pady=10)

root.mainloop()
