import tkinter as tk
from tkcalendar import DateEntry  # Install this library using: pip install tkcalendar

def toggle_date_entry_state():
    current_state = date_entry.cget("state")
    new_state = "normal" if current_state == "disabled" else "disabled"
    date_entry.configure(state=new_state)
    state_label.config(text=f"DateEntry State: {new_state.capitalize()}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Toggle DateEntry State")

# Create a DateEntry widget
date_entry = DateEntry(root, width=12, background='lightgray', foreground='black', borderwidth=2)
date_entry.grid(row=0, column=0, padx=10, pady=10)

# Create a button to toggle the state of the DateEntry
toggle_state_button = tk.Button(root, text="Toggle State", command=toggle_date_entry_state)
toggle_state_button.grid(row=1, column=0, pady=10)

# Create a label to display the current state of the DateEntry
state_label = tk.Label(root, text="DateEntry State: Normal")
state_label.grid(row=2, column=0, pady=10)

# Start the Tkinter event loop
root.mainloop()
