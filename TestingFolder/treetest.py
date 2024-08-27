import tkinter as tk
from tkinter import ttk

def on_tree_double_click(event):
    item = tree.selection()
    if item:
        print(f"Double-clicked on item: {item}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Treeview with Double-Click Event")

# Create a Treeview
tree = ttk.Treeview(root, columns=("Name", "Age"))
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# Insert some sample data into the Treeview
tree.insert("", tk.END, values=("1", "John Doe", "25"))
tree.insert("", tk.END, values=("2", "Jane Doe", "30"))
tree.insert("", tk.END, values=("3", "Bob Smith", "40"))

# Bind the double-click event to the on_tree_double_click function
tree.bind("<Double-1>", on_tree_double_click)

# Pack the Treeview
tree.pack(expand=True, fill=tk.BOTH)

# Run the Tkinter event loop
root.mainloop()
