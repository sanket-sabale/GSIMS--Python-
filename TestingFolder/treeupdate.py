import tkinter as tk
from tkinter import ttk

def update_data():
    selected_item = tree.selection()
    if selected_item:
        updated_data = entry.get()
        tree.item(selected_item, values=(updated_data,updated_data))

root = tk.Tk()
root.title("Tree Update Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Data","value"), show="headings")
tree.heading("Data", text="Data")

# Insert some initial data into the tree
tree.insert("", "end", values=("Item 1","v1",))
tree.insert("", "end", values=("Item 2","v1",))
tree.insert("", "end", values=("Item 3","v1",))

# Create an Entry widget for entering updated data
entry = tk.Entry(root)
entry_label = tk.Label(root, text="Updated Data:")

# Create a button to trigger data update
update_button = tk.Button(root, text="Update Data", command=update_data)

# Place the widgets on the window using grid layout
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
update_button.grid(row=0, column=2, padx=10, pady=10)
tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
