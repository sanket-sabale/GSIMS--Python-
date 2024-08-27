import tkinter as tk
from tkinter import messagebox

def validate_float(value, action_type):
    if action_type == '1':  # Insert
        try:
            float(value)
            return True
        except ValueError:
            return False
    return True

def check_float():
    user_input = entry.get()
    try:
        float_value = float(user_input)
        messagebox.showinfo("Success", f"Entered value: {float_value}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a float.")

# Create the Tkinter window
root = tk.Tk()
root.title("Float Input with Validation Example")

# Validation for float input
float_validator = root.register(validate_float)

# Create an Entry widget for float input with validation
entry = tk.Entry(root, validate="key", validatecommand=(float_validator, '%P', '%d'))
entry.pack(pady=10)

# Create a Button to trigger the float check
check_button = tk.Button(root, text="Check Float", command=check_float)
check_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
