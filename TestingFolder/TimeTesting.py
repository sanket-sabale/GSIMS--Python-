import tkinter as tk
from tkcalendar import DateEntry

def set_default_date():
    default_date = "2024-12-12"  # Set your desired default date in the format "YYYY-MM-DD"
    date_entry.set_date(default_date)

# Create the main application window
root = tk.Tk()
root.title("DateEntry Example")

# Create a DateEntry widget
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)

# Button to set a default date
set_default_button = tk.Button(root, text="Set Default Date", command=set_default_date)

# Pack widgets
date_entry.pack(pady=10)
set_default_button.pack(pady=10)

# Start the main event loop
root.mainloop()
