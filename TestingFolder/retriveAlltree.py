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

def retrieve_all_data():
    # Get all item IDs in the tree
    all_items = tree.get_children()

    for item in all_items:
        # Retrieve data from each item
        item_data = tree.item(item, "values")
        print("Data from item", item, ":", item_data)

root = tk.Tk()
root.title("Retrieve All Data from Treeview Example")

# Create a Treeview widget with two columns
tree = ttk.Treeview(root, columns=("Column 1", "Column 2"), show="headings")
tree.column("Column 1", width=100, anchor=tk.W)
tree.column("Column 2", width=100, anchor=tk.W)
tree.heading("Column 1", text="Column 1")
tree.heading("Column 2", text="Column 2")

# Create Entry widgets for entering data
entry1 = tk.Entry(root, width=15)
entry2 = tk.Entry(root, width=15)

# Create buttons to insert and retrieve data
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
retrieve_all_button = tk.Button(root, text="Retrieve All Data", command=retrieve_all_data)

# Place widgets using grid layout
tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=5)
entry2.grid(row=1, column=1, padx=10, pady=5)
insert_button.grid(row=1, column=2, padx=10, pady=5)
retrieve_all_button.grid(row=2, column=0, columnspan=3, pady=5)

# Start the Tkinter event loop
root.mainloop()
