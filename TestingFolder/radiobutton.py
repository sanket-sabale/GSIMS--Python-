import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value = combo.get()
    status_label.config(text=f"Selected: {selected_value}")

def on_enter(event):
    status_label.config(text="Mouse entered ComboBox")

def on_leave(event):
    status_label.config(text="Mouse left ComboBox")

def on_key(event):
    status_label.config(text=f"Key pressed: {event.char}")
    print(f"-{event.char}-\t({type(event.char)})")

# Create the main window
root = tk.Tk()
root.title("ComboBox Bind Example")

# Create a Combobox
combo_values = ["Option 1", "Option 2", "Option 3"]
combo = ttk.Combobox(root, values=combo_values)
combo.pack(pady=10)
combo.set("Select an option")

# Create a Label for status
status_label = tk.Label(root, text="Status: ")
status_label.pack()

# Bind events to the Combobox
combo.bind("<<ComboboxSelected>>", on_select)
combo.bind("<Enter>", on_enter)
combo.bind("<Leave>", on_leave)
combo.bind("<Key>", on_key)

# Run the Tkinter event loop
root.mainloop()
