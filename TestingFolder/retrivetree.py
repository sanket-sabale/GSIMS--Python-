import tkinter as tk
from tkinter import ttk

def insert_data():
    data1 = entry1.get()
    data2 = entry2.get()

    # Insert data into the tree with two columns
    tree.insert("", "end", values=(data1, data2))

    # Clear the entry widgets
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

def on_tree_select(event):
    # Get the selected item
    selected_item = tree.focus()

    if selected_item:
        # Retrieve data from the selected item
        item_data = tree.item(selected_item, "values")
        print("Data from selected item:", item_data)
    else:
        print("No item selected")

root = tk.Tk()
root.title("Treeview with Two Columns Example")

# Create a Treeview widget with two columns
tree = ttk.Treeview(root, columns=("Column 1", "Column 2"), show="headings")
tree.column("Column 1", width=100, anchor=tk.W)
tree.column("Column 2", width=100, anchor=tk.W)
tree.heading("Column 1", text="Column 1", anchor=tk.W)
tree.heading("Column 2", text="Column 2", anchor=tk.W)

# Bind the selection event to the on_tree_select function
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Create Entry widgets for entering data
entry1 = tk.Entry(root, width=15)
entry2 = tk.Entry(root, width=15)

# Create a button to insert data into the tree
insert_button = tk.Button(root, text="Insert Data", command=insert_data)

# Place widgets using grid layout
tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
insert_button.grid(row=1, column=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
