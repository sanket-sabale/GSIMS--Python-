import tkinter as tk
from datetime import datetime, timedelta

def display_dates():
    entered_date_str = entry_date.get()

    try:
        entered_date = datetime.strptime(entered_date_str, '%Y-%m-%d')
        today = datetime.today()

        if entered_date >= today:
            date_list = [today + timedelta(days=x) for x in range((entered_date - today).days + 1)]

            result_text.delete(1.0, tk.END)  # Clear previous results

            for date in date_list:
                result_text.insert(tk.END, date.strftime('%Y-%m-%d') + '\n')

        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Please enter a date on or after today.")

    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Invalid date format. Please use YYYY-MM-DD.")

# Tkinter GUI
root = tk.Tk()
root.title("Date Range Display")

# Label and Entry for entering the date
label_date = tk.Label(root, text="Enter Date (YYYY-MM-DD):")
label_date.pack()

entry_date = tk.Entry(root)
entry_date.pack()

# Button
display_button = tk.Button(root, text="Display Dates", command=display_dates)
display_button.pack()

# Result Textbox
result_text = tk.Text(root, height=10, width=30)
result_text.pack()

root.mainloop()
