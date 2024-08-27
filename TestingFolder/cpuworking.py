import tkinter as tk
from tkinter import messagebox

def menu_command():
    messagebox.showinfo("Shortcut Example", "Menu item clicked")

# Create the main Tkinter window
root = tk.Tk()
root.title("Menubar with Shortcut Keys")

# Create a menubar
menubar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=menu_command, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=menu_command, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Alt+F4")

# Add the File menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

# Configure the root window to use the menubar
root.config(menu=menubar)

# Bind shortcut keys to menu items
root.bind_all("<Control-o>", lambda event: menu_command())  # Ctrl+O
root.bind_all("<Control-s>", lambda event: menu_command())  # Ctrl+S
root.bind_all("<Alt-F4>", lambda event: root.quit())         # Alt+F4

# Run the Tkinter event loop
root.mainloop()
