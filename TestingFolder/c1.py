import tkinter as tk
from tkinter import ttk

def set_completion_list(event):
    # Get the current input in the combobox
    current_input = combo_var.get().lower()

    # Find matching items and update the values in the combobox
    matching_items = [item for item in combo_values if current_input in item.lower()]
    # combo['values'] = matching_items

    # Open the dropdown list
    combo.event_generate("<Down>")

# Create the Tkinter window
root = tk.Tk()
root.title("ComboBox with Auto-Open")

# Sample data for the combobox
combo_values = ["Apple", "Banana", "Cherry", "Grapes", "Orange", "Peach", "Pear", "Plum"]

# Create a StringVar to hold the current value in the combobox
combo_var = tk.StringVar()

# Create a Combobox with the sample data
combo = ttk.Combobox(root, textvariable=combo_var)
combo['values'] = combo_values
combo.pack(pady=10)

# Bind the set_completion_list function to the <KeyRelease> event
combo.bind("<KeyRelease>", set_completion_list)

# Run the Tkinter event loop
root.mainloop()
