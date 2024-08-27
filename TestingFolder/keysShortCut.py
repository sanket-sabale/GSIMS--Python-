import tkinter as tk

def run_function(event):
    print("Function executed!")

root = tk.Tk()

# Bind the callback function to the Ctrl + P + A combination
root.bind_all("<Control-p-a>", run_function)

root.mainloop()
