import calendar
import tkinter as tk
from tkcalendar import DateEntry

def set_date():
    selected_date = calendar.get_date()
    print("Selected Date:", selected_date)

    # You can perform additional actions with the selected date if needed

def main():
    root = tk.Tk()
    root.title("DateEntry Example")

    cal = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
    cal.pack(padx=10, pady=10)

    set_date_button = tk.Button(root, text="Set Date", command=set_date)
    set_date_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
