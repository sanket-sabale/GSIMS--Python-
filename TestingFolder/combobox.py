import tkinter as tk
from tkinter import ttk

def update_combobox(event):
    # Get the current input in the combobox
    current_input = combo_var.get().lower()

    # Find matching items and update the values in the combobox
    matching_items = [item for item in combo_values if current_input in item.lower()]
    combo['values'] = matching_items

    # print(combo['values'])

def clicked():
    print(combo.get())

# Create the Tkinter window
root = tk.Tk()
root.title("ComboBox with Dynamic Suggestions")

# Sample data for the combobox
combo_values = ["Apple", "Banana", "Cherry", "Grapes", "Orange", "Peach", "Pear", "Plum", "Sanket", "Santosh"]

# Create a StringVar to hold the current value in the combobox
combo_var = tk.StringVar()

# Create a Combobox with the sample data
combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = combo_values
combo.pack(pady=10)

button = tk.Button(root,text="click")
button.pack(padx=10)
button.configure(command=clicked)

# Bind the update_combobox function to the <<KeyRelease>> event
combo.bind("<KeyRelease>", update_combobox)

# Run the Tkinter event loop
root.mainloop()


