import tkinter as tk
from tkinter import Label, StringVar, ttk
import mysql.connector

def on_combobox_selected(event):
    selected_value = ttk.Combobox.get()
    label1.config(text=f"Selected: {type(selected_value)}")
    # label2.config(text=f"Selected: {type(selected_value)}")

# Create the main window
root = tk.Tk()
root.title("Combobox Example")

mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
cursor = mydb.cursor()
label1 = Label(root)
label1.place(relx=0.01,rely=0.01)
label2 = Label(root)
label2.place(relx=0.01,rely=0.05)

productNameVar = StringVar()
productNameLabel = Label(root)
productNameLabel.place(relx=0.02,rely=0.21)
productNameLabel.configure(text="Item Name")
productNameLabel.configure(bg="#ad995e")
productNameLabel.configure(fg="#6e5a20")
cursor.execute("SELECT productname,dcno FROM purchase")
products = cursor.fetchall()
productName = ttk.Combobox(root,values=[[prod[0], prod[1]] for prod in products],textvariable=productNameVar)
productNameConboVal = [[prod[0], prod[1]] for prod in products]
productName.place(relx=0.02,rely=0.258)
productName.configure(width=20)
def update_combobox(event):
    current_input = productNameVar.get().lower()
    matching_items = [item for item in productNameConboVal if current_input in item.lower()]
    productName['values'] = matching_items
productName.bind("<KeyRelease>", update_combobox)
def onSelectProductName(event):
    selectedProduct = productName.get()
    cursor.execute("SELECT product_gst,product_id FROM product where product_description=%s",[selectedProduct,])
    data = cursor.fetchall()
    label1.config(text=f"Selected: {selectedProduct}")
productName.bind("<<ComboboxSelected>>", onSelectProductName)
mydb.commit()
root.mainloop()
