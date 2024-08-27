import tkinter as tk
from tkinter import ttk
import re

def validate_mobile_number():
    mobile_number = entry_mobile.get()

    # Regular expression to validate a mobile number
    pattern = re.compile(r'^[6-9]\d{9}$')

    if pattern.match(mobile_number):
        result_label_mobile.config(text="Mobile Number is valid.")
    else:
        result_label_mobile.config(text="Invalid Mobile Number. Please enter a valid number.")

def validate_aadhar_number():
    aadhar_number = entry_aadhar.get()

    # Regular expression to validate an Aadhar number
    pattern = re.compile(r'^\d{12}$')

    if pattern.match(aadhar_number) or aadhar_number == " " or aadhar_number == "":
        result_label_aadhar.config(text="Aadhar Number is valid.")
    else:
        result_label_aadhar.config(text="Invalid Aadhar Number. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Validation Example")

# Create an entry for mobile number
entry_mobile_label = tk.Label(root, text="Enter Mobile Number:")
entry_mobile_label.pack(pady=5)
entry_mobile = tk.Entry(root)
entry_mobile.pack(pady=5)

# Create a button to validate mobile number
validate_mobile_button = tk.Button(root, text="Validate Mobile Number", command=validate_mobile_number)
validate_mobile_button.pack(pady=10)

# Create a label for displaying the mobile number validation result
result_label_mobile = tk.Label(root, text="")
result_label_mobile.pack()

# Create an entry for Aadhar number
entry_aadhar_label = tk.Label(root, text="Enter Aadhar Number:")
entry_aadhar_label.pack(pady=5)
entry_aadhar = tk.Entry(root)
entry_aadhar.pack(pady=5)

# Create a button to validate Aadhar number
validate_aadhar_button = tk.Button(root, text="Validate Aadhar Number", command=validate_aadhar_number)
validate_aadhar_button.pack(pady=10)

# Create a label for displaying the Aadhar number validation result
result_label_aadhar = tk.Label(root, text="")
result_label_aadhar.pack()

# Run the Tkinter event loop
root.mainloop()
