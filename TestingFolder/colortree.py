import tkinter as tk
from tkinter import ttk

def insert_data():
    data = [entry.get(),entry2.get()]
     
    selected_item = tree.focus()

    if selected_item:
        tree.insert(selected_item, "end", text=data, tags=("custom_tag",))
    else:
        tree.insert("", "end", text=data, tags=("custom_tag",))

def delete_data():
    selected_item = tree.focus()
    if selected_item:
        tree.delete(selected_item)

root = tk.Tk()
root.title("Colored Treeview Example")

# Create a Treeview widget
tree = ttk.Treeview(root)
tree["columns"] = ("Data")
tree.column("#0", width=100, minwidth=100)
tree.column("Data", anchor=tk.W, width=100)
tree.heading("#0", text="Tree")
tree.heading("Data", text="Data")

# Define a tag configuration for custom colors
tree.tag_configure("custom_tag", background="lightblue", foreground="black")

# Create an Entry widget for entering data
entry = tk.Entry(root, width=20)
entry2 = tk.Entry(root, width=20)

# Create buttons for inserting and deleting data
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
delete_button = tk.Button(root, text="Delete Selected", command=delete_data)

# Place widgets using grid layout
tree.grid(row=0, column=0, rowspan=4, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
insert_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
delete_button.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Start the Tkinter event loop
root.mainloop()
