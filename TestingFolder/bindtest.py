import tkinter as tk

def key_press_callback(event):
    print(f"Key Pressed: {event.char}")

def focus_in_callback(event):
    print("Focus In")

def focus_out_callback(event):
    print("Focus Out")

def mouse_click_callback(event):
    print("Mouse Click")

def enter_key_press_callback(event):
    print("Enter Key Pressed")

def mouse_enter_callback(event):
    print("Mouse Enter")

def mouse_leave_callback(event):
    print("Mouse Leave")

root = tk.Tk()
root.title("Entry Widget Events Example")

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)

entry.bind("<Key>", key_press_callback)
entry.bind("<FocusIn>", focus_in_callback)
entry.bind("<FocusOut>", focus_out_callback)
entry.bind("<Button-1>", mouse_click_callback)
entry.bind("<Return>", enter_key_press_callback)
entry.bind("<Enter>", mouse_enter_callback)
entry.bind("<Leave>", mouse_leave_callback)

root.mainloop()
