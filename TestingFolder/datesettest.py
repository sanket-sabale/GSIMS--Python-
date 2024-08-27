import tkinter as tk
from tkcalendar import DateEntry 
from datetime import datetime

def set_date():
    selected_date_str = "2023-05-15"
    try:
        selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
        date_entry.set_date(selected_date)
    except ValueError:
        print("Invalid date format")

root = tk.Tk()
root.title("Set Date to DateEntry Example")

date_entry = DateEntry(root, width=12, background='lightgray', foreground='black', borderwidth=2)
date_entry.pack(padx=10, pady=10)

set_date_button = tk.Button(root, text="Set Date", command=set_date)
set_date_button.pack(pady=10)

root.mainloop()
