# ==================( IMPORT )==================
from tkinter import *
# import re
import string
import mysql.connector
import random
# import psutil
from datetime import date
from tkinter import ttk
# from GSIMSPac import fun
# from GSIMSPac import Product
# from GSIMSPac import Partys
# from GSIMSPac import PurchaseDC
# from GSIMSPac import PurchaseInvoice
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
# ===============================================

def dcNumber():
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for _ in range(2))
    result0 = random.randint(1000,9999)
    bill_number = f"{result}{result0}"
    return bill_number

class PurchaseDc:
    
    def __init__(self,canvas_widget):
        
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        self.cursor = self.mydb.cursor()
        self.num = ""
        self.numdis = '0'
        self.numcharg = ""
        self.numround = ""
        f1 = ("Times", 11)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 12)
        f4 = ("Arial Black", 11)
        f5 = ("Arial Black", 10)
        
        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.1,rely=0.16)
        self.root.configure(width=1200,height=610)
        self.root.configure(bg="#ad995e")

        self.floatValidator = self.root.register(self.validateFloat)
        
        self.line1 = Canvas(self.root)
        self.line1.place(rely=0.19)
        self.line1.configure(width=1350,height=5)
        self.line1.configure(bg="#e5e6d5")
        
        self.line2 = Canvas(self.root)
        self.line2.place(relx=0.7)
        self.line2.configure(width=5,height=113)
        self.line2.configure(bg="#e5e6d5")
        
        self.line3 = Canvas(self.root)
        self.line3.place(rely=0.386)
        self.line3.configure(width=1350,height=5)
        self.line3.configure(bg="#e5e6d5")

        self.radiooption = StringVar()

        self.entryNoLabel = Label(self.root)
        self.entryNoLabel.place(relx=0.01,rely=0.01)
        self.entryNoLabel.configure(text="Entry No:")
        self.entryNoLabel.configure(bg="#ad995e")
        self.entryNoLabel.configure(fg="#6e5a20")
        self.entryNoLabel.configure(font=f3)
        self.entryNo = Entry(self.root)
        self.entryNo.place(relx=0.09,rely=0.02)
        self.entryNo.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="#05591c")
        self.entryNo.configure(width=11)
        self.entryNo.configure(bg="#e5e6d5")
        self.entryNo.configure(font=f2)
        
        self.entryDateLabel = Label(self.root)
        self.entryDateLabel.place(relx=0.23,rely=0.01)
        self.entryDateLabel.configure(text="Entry Date:")
        self.entryDateLabel.configure(bg="#ad995e")
        self.entryDateLabel.configure(fg="#6e5a20")
        self.entryDateLabel.configure(font=f3)
        self.entryDate = DateEntry(self.root)
        self.entryDate.place(relx=0.32,rely=0.01)
        self.entryDate.configure(background='#6e5a20', foreground='#ad995e')
        self.entryDate.configure(width=10)
        
        self.typeLabel = Label(self.root)
        self.typeLabel.place(relx=0.44,rely=0.01)
        self.typeLabel.configure(text="Pur-Bill or D/C:")
        self.typeLabel.configure(bg="#ad995e")
        self.typeLabel.configure(fg="#6e5a20")
        self.typeLabel.configure(font=f3)
        self.type = ttk.Combobox(self.root)  
        self.type.place(relx=0.55,rely=0.02)
        self.type['values'] = ("Select","Pur D/C","Pur Bill")
        self.type.current(0)
        self.type.configure(width=10)
        self.type.configure(font=f2)
        def onSelectType(event):
            selected_item = self.type.get()
            if selected_item == "Pur D/C":
                self.billNo.configure(state="disabled")
                self.dcNo.configure(state="normal")
                self.supplierName.configure(state="normal")
                self.productName.configure(state="normal")
                self.type.configure(state="disabled")
            elif selected_item == "Pur Bill":
                self.billNo.configure(state="normal")
                self.dcNo.configure(state="normal")
                self.supplierName.configure(state="normal")
                self.productName.configure(state="normal")
                self.type.configure(state="disabled")
            else:
                self.billNo.configure(state="disabled")
                self.dcNo.configure(state="disabled")
                self.supplierName.configure(state="disabled")
                self.productName.configure(state="disabled")
                messagebox.showerror("Warning","Select an type of entry")
        self.type.bind("<<ComboboxSelected>>", onSelectType)

        self.supplierNameLabel = Label(self.root)
        self.supplierNameLabel.place(relx=0.01,rely=0.07)
        self.supplierNameLabel.configure(text="Supplier Name:")
        self.supplierNameLabel.configure(bg="#ad995e")
        self.supplierNameLabel.configure(fg="#6e5a20")
        self.supplierNameLabel.configure(font=f3)
        self.supplierNo = Entry(self.root)
        self.supplierNo.place(relx=0.13,rely=0.075)
        self.supplierNo.configure(width=8)
        self.supplierNo.configure(bg="#e5e6d5")
        self.supplierNo.configure(font=f2)
        self.supplierNo.configure(state="disabled")
        self.cursor.execute("SELECT partyname FROM partys where status= %s",["active",])
        self.partys = self.cursor.fetchall()
        self.supplierName = ttk.Combobox(self.root,values=[party[0] for party in self.partys])
        self.supplierName.place(relx=0.21,rely=0.075)
        self.supplierName.configure(width=28)
        self.supplierName.configure(font=f2)
        self.supplierName.configure(state="disabled")
        def onSelectSupplierName(event):
            selected_item = self.supplierName.get()
            select_query3 = "select partyid,location from partys where partyname = %s"
            self.cursor.execute(select_query3,[selected_item,])
            data = self.cursor.fetchall()
            self.supplierNo.configure(state="normal")
            self.supplierLocation.configure(state="normal")
            self.supplierNo.delete(0,END)
            self.supplierLocation.delete(0,END)
            self.supplierNo.insert(END, data[0][0])
            self.supplierLocation.insert(END, data[0][1])
            self.supplierNo.configure(state="disabled")
            self.supplierLocation.configure(state="disabled")
        self.supplierName.bind("<<ComboboxSelected>>", onSelectSupplierName)
        self.supplierLocation = Entry(self.root)
        self.supplierLocation.place(relx=0.47,rely=0.075)
        self.supplierLocation.configure(width=13)
        self.supplierLocation.configure(bg="#e5e6d5")
        self.supplierLocation.configure(font=f2)
        self.supplierLocation.configure(state="disabled")
        
        self.dcNoDateLabel = Label(self.root)
        self.dcNoDateLabel.place(relx=0.01,rely=0.13)
        self.dcNoDateLabel.configure(text="D/C No/Date:")
        self.dcNoDateLabel.configure(bg="#ad995e")
        self.dcNoDateLabel.configure(fg="#6e5a20")
        self.dcNoDateLabel.configure(font=f3)
        self.dcNo = Entry(self.root)
        self.dcNo.place(relx=0.13,rely=0.138)
        self.dcNo.configure(width=8)
        self.dcNo.configure(bg="#e5e6d5")
        self.dcNo.configure(font=f2)
        self.dcNo.configure(state="disabled",disabledbackground="#fce89d")
        self.dcDate = DateEntry(self.root)
        self.dcDate.place(relx=0.21,rely=0.13)
        self.dcDate.configure(background='#6e5a20', foreground='#ad995e')
        self.dcDate.configure(width=10)

        self.billNoDateLabel = Label(self.root)
        self.billNoDateLabel.place(relx=0.35,rely=0.13)
        self.billNoDateLabel.configure(text="Bill No/Date:")
        self.billNoDateLabel.configure(bg="#ad995e")
        self.billNoDateLabel.configure(fg="#6e5a20")
        self.billNoDateLabel.configure(font=f3)
        self.billNo = Entry(self.root)
        self.billNo.place(relx=0.45,rely=0.138)
        self.billNo.configure(width=8)
        self.billNo.configure(bg="#e5e6d5")
        self.billNo.configure(font=f2)
        self.billNo.configure(state="disabled",disabledbackground="#fce89d")
        self.billDate = DateEntry(self.root)
        self.billDate.place(relx=0.53,rely=0.13)
        self.billDate.configure(background='#6e5a20', foreground='#ad995e')
        self.billDate.configure(width=10)
        
        self.cashButton = Radiobutton(self.root,text="Cash", variable=self.radiooption, value="cash")
        self.cashButton.place(relx=0.72,rely=0.02)
        self.cashButton.configure(fg="#6e5a20")
        self.cashButton.configure(bg="#ad995e")
        self.cashButton.configure(activebackground="#ad995e")
        self.cashButton.configure(font=f3)
        self.creditButton = Radiobutton(self.root,text="Credit", variable=self.radiooption, value="credit")
        self.creditButton.place(relx=0.72,rely=0.07)
        self.creditButton.configure(fg="#6e5a20")
        self.creditButton.configure(bg="#ad995e")
        self.creditButton.configure(activebackground="#ad995e")
        self.creditButton.configure(font=f3)

        self.noteLabel = Label(self.root)
        self.noteLabel.place(relx=0.715,rely=0.137)
        self.noteLabel.configure(text="Note:")
        self.noteLabel.configure(bg="#ad995e")
        self.noteLabel.configure(fg="#6e5a20")
        self.noteLabel.configure(font=f3)
        self.note = Entry(self.root)
        self.note.place(relx=0.76,rely=0.14)
        self.note.configure(width=25)
        self.note.configure(bg="#e5e6d5")
        self.note.configure(font=f2)
        self.productNameVar = StringVar()
        self.productNameLabel = Label(self.root)
        self.productNameLabel.place(relx=0.02,rely=0.21)
        self.productNameLabel.configure(text="Item Name")
        self.productNameLabel.configure(bg="#ad995e")
        self.productNameLabel.configure(fg="#6e5a20")
        self.productNameLabel.configure(font=f4)
        self.cursor.execute("SELECT product_description FROM product where status = %s",["active",])
        self.products = self.cursor.fetchall()
        self.productName = ttk.Combobox(self.root,values=[prod[0] for prod in self.products],textvariable=self.productNameVar)
        self.productNameConboVal = [prod[0] for prod in self.products]
        self.productName.place(relx=0.02,rely=0.258)
        self.productName.configure(width=20)
        self.productName.configure(font=f2)
        self.productName.configure(state="disabled")
        def update_combobox(event):
            current_input = self.productNameVar.get().lower()
            matching_items = [item for item in self.productNameConboVal if current_input in item.lower()]
            self.productName['values'] = matching_items
        self.productName.bind("<KeyRelease>", update_combobox)
        def onSelectProductName(event):
            selectedProduct = self.productName.get()
            self.cursor.execute("SELECT product_gst,product_id FROM product where product_description=%s",[selectedProduct,])
            data = self.cursor.fetchall()
            self.gst.configure(state="normal")
            self.code.configure(state="normal")
            self.gst.delete(0,END)
            self.code.delete(0,END)
            self.gst.insert(0, data[0][0])
            self.code.insert(0, data[0][1])
            self.gst.configure(state="disabled")
            self.code.configure(state="disabled")
            self.lotNo.configure(state="normal")
            self.quantity.configure(state="normal")
            if self.type.get() == "Pur Bill":
                self.rate.configure(state='normal')
        self.productName.bind("<<ComboboxSelected>>", onSelectProductName)

        self.code = Entry(self.root)
        self.code.place(relx=0.02,rely=0.32)
        self.code.configure(width=10)
        self.code.configure(bg="#e5e6d5")
        self.code.configure(font=f2)
        self.code.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")        
        
        self.lotNoLabel = Label(self.root)
        self.lotNoLabel.place(relx=0.22,rely=0.21)
        self.lotNoLabel.configure(text="Batch/Lot")
        self.lotNoLabel.configure(bg="#ad995e")
        self.lotNoLabel.configure(fg="#6e5a20")
        self.lotNoLabel.configure(font=f3)
        self.lotNo = Entry(self.root)
        self.lotNo.place(relx=0.22,rely=0.258)
        self.lotNo.configure(width=10)
        self.lotNo.configure(bg="#e5e6d5")
        self.lotNo.configure(font=f2)
        self.lotNo.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        
        self.expDateLabel = Label(self.root)
        self.expDateLabel.place(relx=0.32,rely=0.21)
        self.expDateLabel.configure(text="Expiry")
        self.expDateLabel.configure(bg="#ad995e")
        self.expDateLabel.configure(fg="#6e5a20")
        self.expDateLabel.configure(font=f3)
        self.expDate = DateEntry(self.root)
        self.expDate.place(relx=0.32,rely=0.252)
        self.expDate.configure(background='#6e5a20', foreground='#ad995e')
        self.expDate.configure(width=10)
        
        self.quantityLabel = Label(self.root)
        self.quantityLabel.place(relx=0.437,rely=0.21)
        self.quantityLabel.configure(text="Quantity")
        self.quantityLabel.configure(bg="#ad995e")
        self.quantityLabel.configure(fg="#6e5a20")
        self.quantityLabel.configure(font=f3)
        self.quantity = Entry(self.root)
        self.quantity.place(relx=0.437,rely=0.258)
        self.quantity.configure(width=10)
        self.quantity.configure(bg="#e5e6d5")
        self.quantity.configure(font=f2)
        self.quantity.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.quantity.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.rateLabel = Label(self.root)
        self.rateLabel.place(relx=0.544,rely=0.21)
        self.rateLabel.configure(text="Rate")
        self.rateLabel.configure(bg="#ad995e")
        self.rateLabel.configure(fg="#6e5a20")
        self.rateLabel.configure(font=f3)
        self.rate = Entry(self.root)
        self.rate.place(relx=0.544,rely=0.258)
        self.rate.configure(width=10)
        self.rate.configure(bg="#e5e6d5")
        self.rate.configure(font=f2)
        self.rate.bind("<Key>", self.keyWorkRate)
        self.rate.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.rate.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.amountLabel = Label(self.root)
        self.amountLabel.place(relx=0.651,rely=0.21)
        self.amountLabel.configure(text="Taxable Amt")
        self.amountLabel.configure(bg="#ad995e")
        self.amountLabel.configure(fg="#6e5a20")
        self.amountLabel.configure(font=f3)
        self.amount = Entry(self.root)
        self.amount.place(relx=0.651,rely=0.258)
        self.amount.configure(width=10)
        self.amount.configure(bg="#e5e6d5")
        self.amount.configure(font=f2)
        self.amount.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.amount.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.gstLabel = Label(self.root)
        self.gstLabel.place(relx=0.758,rely=0.21)
        self.gstLabel.configure(text="GST %")
        self.gstLabel.configure(bg="#ad995e")
        self.gstLabel.configure(fg="#6e5a20")
        self.gstLabel.configure(font=f3)
        self.gst = Entry(self.root)
        self.gst.place(relx=0.758,rely=0.258)
        self.gst.configure(width=10)
        self.gst.configure(bg="#e5e6d5")
        self.gst.configure(font=f2)
        self.gst.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.gst.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.taxAmountLabel = Label(self.root)
        self.taxAmountLabel.place(relx=0.875,rely=0.21)
        self.taxAmountLabel.configure(text="Amount")
        self.taxAmountLabel.configure(bg="#ad995e")
        self.taxAmountLabel.configure(fg="#6e5a20")
        self.taxAmountLabel.configure(font=f3)
        self.taxAmount = Entry(self.root)
        self.taxAmount.place(relx=0.875,rely=0.258)
        self.taxAmount.configure(width=10)
        self.taxAmount.configure(bg="#e5e6d5")
        self.taxAmount.configure(font=f2)
        self.taxAmount.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.taxAmount.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))

        self.addButton = Button(self.root, height=1)
        self.addButton.place(relx=0.875,rely=0.32)
        self.addButton.configure(text="Add")
        self.addButton.configure(font=f1)
        self.addButton.configure(width=12)
        self.addButton.configure(activebackground="#ad995e")
        self.addButton.configure(bg="#e0cb8d")
        self.addButton.configure(command=self.addToCart)

        self.changeButton = Button(self.root, height=1)
        self.changeButton.place(relx=0.758,rely=0.32)
        self.changeButton.configure(text="Update")
        self.changeButton.configure(font=f1)
        self.changeButton.configure(width=12)
        self.changeButton.configure(activebackground="#ad995e")
        self.changeButton.configure(bg="#e0cb8d")
        self.changeButton.configure(command=self.changeProduct)
        
        self.modifyButton = Button(self.root, height=1)
        self.modifyButton.place(relx=0.651,rely=0.32)
        self.modifyButton.configure(text="Modify")
        self.modifyButton.configure(font=f1)
        self.modifyButton.configure(width=12)
        self.modifyButton.configure(activebackground="#ad995e")
        self.modifyButton.configure(bg="#e0cb8d")
        self.modifyButton.configure(command=self.modifyProduct)

        self.removeButton = Button(self.root, height=1)
        self.removeButton.place(relx=0.544,rely=0.32)
        self.removeButton.configure(text="Remove")
        self.removeButton.configure(font=f1)
        self.removeButton.configure(width=12)
        self.removeButton.configure(activebackground="#ad995e")
        self.removeButton.configure(bg="#e0cb8d")
        self.removeButton.configure(command=self.toRemoveProductfromCart)

        self.clearButton = Button(self.root, height=1)
        self.clearButton.place(relx=0.437,rely=0.32)
        self.clearButton.configure(text="Clear")
        self.clearButton.configure(font=f1)
        self.clearButton.configure(width=12)
        self.clearButton.configure(activebackground="#ad995e")
        self.clearButton.configure(bg="#e0cb8d")
        self.clearButton.configure(command=self.clear)

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.01, rely=0.41, width=1000, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.845, rely=0.41, width=18, height=305)

        self.tree = ttk.Treeview(self.root)
        self.tree.place(relx=0.01, rely=0.44, width=1000, height=290)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.configure(command=self.tree.yview)
        
        self.tree.configure(
            columns=(
                "Item Name",
                "Code",
                "Batch/Lot",
                "Expiry",
                "Quantity",
                "Rate",
                "Taxable amt",
                "GST %",
                "Amount"
            )
        )

        self.tree.heading("Item Name", text="Item Name", anchor=W)
        self.tree.heading("Code", text="Code", anchor=W)
        self.tree.heading("Batch/Lot", text="Batch/Lot", anchor=W)
        self.tree.heading("Expiry", text="Expiry", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Rate", text="Rate", anchor=W)
        self.tree.heading("Taxable amt", text="Taxable amt", anchor=W)
        self.tree.heading("GST %", text="GST %", anchor=W)
        self.tree.heading("Amount", text="Amount", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=170)
        self.tree.column("#2", stretch=NO, minwidth=0, width=91)
        self.tree.column("#3", stretch=NO, minwidth=0, width=95)
        self.tree.column("#4", stretch=NO, minwidth=0, width=110)
        self.tree.column("#5", stretch=NO, minwidth=0, width=100)
        self.tree.column("#6", stretch=NO, minwidth=0, width=110)
        self.tree.column("#7", stretch=NO, minwidth=0, width=110)
        self.tree.column("#8", stretch=NO, minwidth=0, width=100)
        self.tree.column("#9", stretch=NO, minwidth=0, width=110)
        self.tree.configure(selectmode="extended")
        self.tree.tag_configure("item", background="#fce89d", foreground="black")
        self.tree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        
        self.qtytotLabel = Label(self.root)
        self.qtytotLabel.place(relx=0.27,rely=0.915)
        self.qtytotLabel.configure(text="Qty Total")
        self.qtytotLabel.configure(bg="#ad995e")
        self.qtytotLabel.configure(fg="#6e5a20")
        self.qtytotLabel.configure(font=f5)
        self.qtytot = Entry(self.root)
        self.qtytot.place(relx=0.27,rely=0.95)
        self.qtytot.configure(width=10)
        self.qtytot.configure(bg="#e5e6d5")
        self.qtytot.configure(font=f2)
        self.qtytot.insert(0,0.0)
        self.qtytot.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.qtytot.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.discountLabel = Label(self.root)
        self.discountLabel.place(relx=0.37,rely=0.915)
        self.discountLabel.configure(text="Discount")
        self.discountLabel.configure(bg="#ad995e")
        self.discountLabel.configure(fg="#6e5a20")
        self.discountLabel.configure(font=f5)
        self.discount = Entry(self.root)
        self.discount.place(relx=0.37,rely=0.95)
        self.discount.configure(width=10)
        self.discount.configure(bg="#e5e6d5")
        self.discount.configure(font=f2)
        self.discount.configure(state="disabled",disabledbackground="#fce89d")
        self.discount.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.chargeLabel = Label(self.root)
        self.chargeLabel.place(relx=0.47,rely=0.915)
        self.chargeLabel.configure(text="Charge")
        self.chargeLabel.configure(bg="#ad995e")
        self.chargeLabel.configure(fg="#6e5a20")
        self.chargeLabel.configure(font=f5)
        self.charge = Entry(self.root)
        self.charge.place(relx=0.47,rely=0.95)
        self.charge.configure(width=10)
        self.charge.configure(bg="#e5e6d5")
        self.charge.configure(font=f2)
        self.charge.configure(state="disabled",disabledbackground="#fce89d")
        self.charge.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.roundOffLabel = Label(self.root)
        self.roundOffLabel.place(relx=0.57,rely=0.915)
        self.roundOffLabel.configure(text="Round Off")
        self.roundOffLabel.configure(bg="#ad995e")
        self.roundOffLabel.configure(fg="#6e5a20")
        self.roundOffLabel.configure(font=f5)
        self.roundOff = Entry(self.root)
        self.roundOff.place(relx=0.57,rely=0.95)
        self.roundOff.configure(width=10)
        self.roundOff.configure(bg="#e5e6d5")
        self.roundOff.configure(font=f2)
        self.roundOff.configure(state="disabled",disabledbackground="#fce89d")
        self.roundOff.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.totalLabel = Label(self.root)
        self.totalLabel.place(relx=0.67,rely=0.915)
        self.totalLabel.configure(text="Total")
        self.totalLabel.configure(bg="#ad995e")
        self.totalLabel.configure(fg="#6e5a20")
        self.totalLabel.configure(font=f5)
        self.total = Entry(self.root)
        self.total.place(relx=0.67,rely=0.95)
        self.total.configure(width=10)
        self.total.configure(bg="#e5e6d5")
        self.total.configure(font=f2)
        self.total.insert(0,0.0)
        self.total.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.total.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.netTotalLabel = Label(self.root)
        self.netTotalLabel.place(relx=0.77,rely=0.915)
        self.netTotalLabel.configure(text="Net Total")
        self.netTotalLabel.configure(bg="#ad995e")
        self.netTotalLabel.configure(fg="#6e5a20")
        self.netTotalLabel.configure(font=f5)
        self.netTotal = Entry(self.root)
        self.netTotal.place(relx=0.77,rely=0.95)
        self.netTotal.configure(width=10)
        self.netTotal.configure(bg="#e5e6d5")
        self.netTotal.configure(font=f2)
        self.netTotal.insert(0,0.0)
        self.netTotal.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.netTotal.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))

        self.addDcButton = Button(self.root, height=1)
        self.addDcButton.place(relx=0.878,rely=0.46)
        self.addDcButton.configure(text="Add D/C")
        self.addDcButton.configure(font=f1)
        self.addDcButton.configure(width=12)
        self.addDcButton.configure(activebackground="#ad995e")
        self.addDcButton.configure(bg="#e0cb8d")
        self.addDcButton.configure(command=self.addDC)

        self.searchDcButton = Button(self.root, height=1)
        self.searchDcButton.place(relx=0.878,rely=0.56)
        self.searchDcButton.configure(text="Search")
        self.searchDcButton.configure(font=f1)
        self.searchDcButton.configure(width=12)
        self.searchDcButton.configure(activebackground="#ad995e")
        self.searchDcButton.configure(bg="#e0cb8d")
        self.searchDcButton.configure(command=self.searchDC)

        self.updateDcButton = Button(self.root, height=1)
        self.updateDcButton.place(relx=0.878,rely=0.66)
        self.updateDcButton.configure(text="Update")
        self.updateDcButton.configure(font=f1)
        self.updateDcButton.configure(width=12)
        self.updateDcButton.configure(activebackground="#ad995e")
        self.updateDcButton.configure(bg="#e0cb8d")
        self.updateDcButton.configure(state='disabled')

        self.deleteDcButton = Button(self.root, height=1)
        self.deleteDcButton.place(relx=0.878,rely=0.76)
        self.deleteDcButton.configure(text="Delete")
        self.deleteDcButton.configure(font=f1)
        self.deleteDcButton.configure(width=12)
        self.deleteDcButton.configure(activebackground="#ad995e")
        self.deleteDcButton.configure(bg="#e0cb8d")
        self.deleteDcButton.configure(state='disabled')
        self.deleteDcButton.configure(command=self.deletedc)

        self.cancelDcButton = Button(self.root, height=1)
        self.cancelDcButton.place(relx=0.878,rely=0.86)
        self.cancelDcButton.configure(text="New D/C")
        self.cancelDcButton.configure(font=f1)
        self.cancelDcButton.configure(width=12)
        self.cancelDcButton.configure(activebackground="#ad995e")
        self.cancelDcButton.configure(bg="#e0cb8d")
        self.cancelDcButton.configure(command=self.newDc)

        self.mydb.commit()

    def deletedc(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        eno = self.entryNo.get()
        flag = True
        if eno.strip():
            query = "select * from purchase where purchasedcid = %s"
            cur.execute(query,[eno,])
            dcdata = cur.fetchall()
            for data in dcdata:
                if data[18] != data[30]:
                    flag = False
            # message = messagebox.askyesno("INFO","Are you sure to delete ?")
            if messagebox.askyesno("INFO","Are you sure to delete ?"):
                if flag:    
                    for data in dcdata:
                        sta = "del"
                        if data[29] == "dc" or data[29] == "inv":
                            query = "update purchase set status= %s where purchasedcid= %s" # srno= %s and
                            cur.execute(query,[sta,data[1]])
            else:
                print("not deleted")
            self.entryNo.delete(0,END)
            self.entryNo.configure(state='disabled')
            self.nextSearchButton.configure(state='disabled')
            self.newDc()

        mydb.commit()

    def searchDC(self):
        f6 = ('times', 10)
        self.newDc()
        self.entryNo.configure(state='normal')
        self.entryNo.delete(0,END)
        self.nextSearchButton = Button(self.root,height=1)
        self.nextSearchButton.place(relx=0.18,rely=0.018)
        self.nextSearchButton.configure(text="🔍")
        self.nextSearchButton.configure(width=5)
        self.nextSearchButton.configure(font=f6)
        self.nextSearchButton.configure(activebackground="#ad995e")
        self.nextSearchButton.configure(bg="#8bf78e")
        self.nextSearchButton.configure(command=self.nextSearch)
         
    def nextSearch(self):
        data = self.entryNo.get()
        if data.strip():
            mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
            cur = mydb.cursor()
            query = "select * from purchase where purchasedcid = %s"
            cur.execute(query,[data,])
            dcdata = cur.fetchall()
            if not dcdata:
                messagebox.showwarning("Warning","Entry number is invalid.")
                self.entryNo.delete(0,END)
                self.entryNo.configure(state='disabled')
                self.nextSearchButton.configure(state='disabled')
                self.newDc()
            elif dcdata[0][29] == "del":
                messagebox.showwarning("Warning","D/C Not found.")
                self.entryNo.delete(0,END)
                self.entryNo.configure(state='disabled')
                self.nextSearchButton.configure(state='disabled')
                self.newDc()
            else:
                todaydate = date.today()
                self.tree.delete(*self.tree.get_children())
                self.addButton.configure(state='disabled')
                self.addDcButton.configure(state='disabled')
                self.removeButton.configure(state='disabled')
                self.entryNo.configure(state='normal')
                self.type.configure(state='normal')
                self.supplierNo.configure(state='normal')
                self.supplierName.configure(state='normal')
                self.supplierLocation.configure(state='normal')
                self.dcNo.configure(state='normal')
                self.billNo.configure(state='normal')
                self.note.configure(state='normal')
                self.productName.configure(state='normal')
                self.lotNo.configure(state='normal')
                self.quantity.configure(state='normal')
                self.rate.configure(state='normal')
                self.taxAmount.configure(state='normal')
                self.gst.configure(state='normal')
                self.amount.configure(state='normal')
                self.code.configure(state='normal')
                self.removeButton.configure(state='normal')
                self.modifyButton.configure(state='normal')
                self.changeButton.configure(state='normal')
                self.qtytot.configure(state='normal')
                self.discount.configure(state='normal')
                self.charge.configure(state='normal')
                self.roundOff.configure(state='normal')
                self.total.configure(state='normal')
                self.netTotal.configure(state='normal')
                self.updateDcButton.configure(state='normal')
                self.deleteDcButton.configure(state='normal')
                try:
                    self.expDate.set_date(todaydate)
                    self.entryDate.set_date(dcdata[0][2])
                    self.dcDate.set_date(dcdata[0][9])
                    self.billDate.set_date(dcdata[0][11])
                except ValueError:
                    print("Invalid format of Expiry date")
                    
                self.type.current(0)
                self.supplierNo.delete(0,END)
                self.supplierName.delete(0,END)
                self.supplierLocation.delete(0,END)
                self.dcNo.delete(0,END)
                self.billNo.delete(0,END)
                self.note.delete(0,END)
                self.productName.delete(0,END)
                self.code.delete(0,END)
                self.lotNo.delete(0,END)
                self.quantity.delete(0,END)
                self.rate.delete(0,END)
                self.taxAmount.delete(0,END)
                self.gst.delete(0,END)
                self.amount.delete(0,END)
                self.qtytot.delete(0,END)
                self.discount.delete(0,END)
                self.charge.delete(0,END)
                self.roundOff.delete(0,END)
                self.total.delete(0,END)
                self.netTotal.delete(0,END)

                self.supplierNo.insert(0,dcdata[0][5])
                self.supplierName.insert(0,dcdata[0][6])
                self.supplierLocation.insert(0,dcdata[0][7])
                if dcdata[0][12] == "cash":
                    self.cashButton.select()
                else:
                    self.creditButton.select()
                self.dcNo.insert(0,dcdata[0][8])
                if dcdata[0][10] != None:
                    self.billNo.insert(0,dcdata[0][10])
                self.note.insert(0,dcdata[0][13])                
                if dcdata[0][28] != None:
                    self.netTotal.insert(0,dcdata[0][28]) 
                else:
                    self.netTotal.insert(0,0.0)                
                if dcdata[0][27] != None:
                    self.total.insert(0,float(dcdata[0][27]))
                else:
                    self.total.insert(0,0.0)                 
                if dcdata[0][24] != None:
                    self.discount.insert(0,dcdata[0][24])
                else:
                    self.discount.insert(0,0.0)                  
                if dcdata[0][23] != None:
                    self.qtytot.insert(0,dcdata[0][23])
                else:
                    self.qtytot.insert(0,0.0)                  
                if dcdata[0][25] != None:
                    self.charge.insert(0,dcdata[0][25])
                else:
                    self.charge.insert(0,0.0)                  
                if dcdata[0][26] != None:
                    self.roundOff.insert(0,dcdata[0][26])
                else:
                    self.roundOff.insert(0,0.0)  

                todaydate = date.today()
                for product in dcdata:
                    data = (product[14],product[15],product[16],product[17],product[18],product[19],product[20],product[21],product[22])
                    self.tree.insert("", "end", values=data,tags=("item",))

                self.type.configure(state='disabled')
                self.entryNo.configure(state='disabled')
                self.supplierNo.configure(state='disabled')
                self.supplierName.configure(state='disabled')
                self.supplierLocation.configure(state='disabled')
                self.dcNo.configure(state='disabled')
                self.billNo.configure(state='disabled')
                self.productName.configure(state='disabled')
                self.lotNo.configure(state='disabled')
                self.quantity.configure(state='disabled')
                self.rate.configure(state='disabled')
                self.taxAmount.configure(state='disabled')
                self.gst.configure(state='disabled')
                self.amount.configure(state='disabled')
                self.code.configure(state='disabled')
                self.qtytot.configure(state='disabled')
                self.discount.configure(state='disabled')
                self.charge.configure(state='disabled')
                self.roundOff.configure(state='disabled')
                self.total.configure(state='disabled')
                self.netTotal.configure(state='disabled')

            mydb.commit()
        else:
            messagebox.showwarning("Warning","Enter Entry Number")

    def newDc(self):
        todaydate = date.today()
        self.tree.delete(*self.tree.get_children())
        self.entryNo.configure(state='normal')
        self.type.configure(state='normal')
        self.supplierNo.configure(state='normal')
        self.supplierName.configure(state='normal')
        self.supplierLocation.configure(state='normal')
        self.dcNo.configure(state='normal')
        self.billNo.configure(state='normal')
        self.note.configure(state='normal')
        self.productName.configure(state='normal')
        self.lotNo.configure(state='normal')
        self.quantity.configure(state='normal')
        self.rate.configure(state='normal')
        self.taxAmount.configure(state='normal')
        self.gst.configure(state='normal')
        self.amount.configure(state='normal')
        self.code.configure(state='normal')
        self.removeButton.configure(state='normal')
        self.modifyButton.configure(state='normal')
        self.changeButton.configure(state='normal')
        self.addButton.configure(state='normal')
        self.addDcButton.configure(state='normal')
        self.qtytot.configure(state='normal')
        self.discount.configure(state='normal')
        self.charge.configure(state='normal')
        self.roundOff.configure(state='normal')
        self.total.configure(state='normal')
        self.netTotal.configure(state='normal')

        self.entryNo.delete(0,END)
        try:
            self.expDate.set_date(todaydate)
            self.entryDate.set_date(todaydate)
            self.dcDate.set_date(todaydate)
            self.billDate.set_date(todaydate)
        except ValueError:
            print("Invalid format of Expiry date")
        self.type.current(0)
        self.supplierNo.delete(0,END)
        self.supplierName.delete(0,END)
        self.supplierLocation.delete(0,END)
        self.dcNo.delete(0,END)
        self.billNo.delete(0,END)
        self.note.delete(0,END)
        self.productName.delete(0,END)
        self.code.delete(0,END)
        self.lotNo.delete(0,END)
        self.quantity.delete(0,END)
        self.rate.delete(0,END)
        self.taxAmount.delete(0,END)
        self.gst.delete(0,END)
        self.amount.delete(0,END)
        self.qtytot.delete(0,END)
        self.discount.delete(0,END)
        self.charge.delete(0,END)
        self.roundOff.delete(0,END)
        self.total.delete(0,END)
        self.netTotal.delete(0,END)
        self.total.insert(0,0.0)
        self.netTotal.insert(0,0.0)
        self.qtytot.insert(0,0.0)
        
        self.entryNo.configure(state='disabled')
        self.supplierNo.configure(state='disabled')
        self.supplierName.configure(state='disabled')
        self.supplierLocation.configure(state='disabled')
        self.dcNo.configure(state='disabled')
        self.billNo.configure(state='disabled')
        self.productName.configure(state='disabled')
        self.lotNo.configure(state='disabled')
        self.quantity.configure(state='disabled')
        self.rate.configure(state='disabled')
        self.taxAmount.configure(state='disabled')
        self.gst.configure(state='disabled')
        self.amount.configure(state='disabled')
        self.code.configure(state='disabled')
        self.qtytot.configure(state='disabled')
        self.discount.configure(state='disabled')
        self.charge.configure(state='disabled')
        self.roundOff.configure(state='disabled')
        self.total.configure(state='disabled')
        self.netTotal.configure(state='disabled')

    def disableall(self):
        self.clear()
        self.entryNo.configure(state='disabled')
        self.type.configure(state='disabled')
        self.productName.configure(state='disabled')
        self.dcNo.configure(state='disabled')
        self.billNo.configure(state='disabled')
        self.note.configure(state='disabled')
        self.supplierName.configure(state='disabled')
        self.lotNo.configure(state='disabled')
        self.quantity.configure(state='disabled')
        self.rate.configure(state='disabled')
        self.addButton.configure(state='disabled')
        self.changeButton.configure(state='disabled')
        self.modifyButton.configure(state='disabled')
        self.removeButton.configure(state='disabled')
        self.addDcButton.configure(state='disabled')
        self.discount.configure(state='disabled')
        self.charge.configure(state='disabled')
        self.roundOff.configure(state='disabled')

    def addDC(self):
        # "Pur D/C","Pur Bill"
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        PurchaseDcnumber = dcNumber()
        entdate = self.entryDate.get_date()
        typeof = self.type.get()
        sid = self.supplierNo.get()
        sname = self.supplierName.get()
        slocation = self.supplierLocation.get()
        dcno = self.dcNo.get()
        dcdate = self.dcDate.get_date()
        billno = self.billNo.get()
        billdate = self.billDate.get_date()
        paytype = self.radiooption.get()
        note = self.note.get()
        totalqty = self.qtytot.get()
        dis = self.discount.get()
        charge = self.charge.get()
        roundoff = self.roundOff.get()
        total = self.total.get()
        netTotal = self.netTotal.get()
        if self.type.get() == "Pur D/C":
            if typeof.strip():
                if sname.strip():
                    if dcno.strip():
                        if paytype.strip():
                            if dis == '':
                                dis = 0
                            if charge == '':
                                charge = 0
                            if roundoff == '':
                                roundoff = 0
                            netTotal = (float(charge) + float(roundoff) + float(total)) - float(dis)
                            self.netTotal.configure(state='normal')
                            self.entryNo.configure(state='normal')
                            self.netTotal.delete(0,END)
                            self.entryNo.delete(0,END)
                            self.netTotal.insert(0,netTotal)
                            self.entryNo.insert(0,PurchaseDcnumber)
                            self.netTotal.configure(state='disabled')
                            self.entryNo.configure(state='disabled')
                            status = "dc"
                            allData = self.tree.get_children()
                            for item in allData:
                                data = self.tree.item(item, "values")
                                descr = f"{data[0]} [{dcno}]"
                                selectQuery = "select selling_price from product where product_id = %s"
                                cur.execute(selectQuery,[data[1]])
                                sp = cur.fetchall()
                                insert = ("INSERT INTO purchase(srno, purchasedcid, purchasedcdate, purchaseid, purchasedate, supplierid, suppliername, supplierlocation, dcno, dcdate, billno, billdate, paytype, note, productname, productno, batch_lot, expiry, quantity, rate, taxableamt, gstrate, amount, qtytotal, discount, charge, roundoff, total, nettotal, status, returnqty, saleqty, salereturnqty, availableqty, entrydescription, sellingprice) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                                cur.execute(insert,[None,PurchaseDcnumber,entdate,None,None,sid,sname,slocation,dcno,dcdate,None,None,paytype,note,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],totalqty,0,0,0,0,0,status,0,0,0,data[4],descr,sp[0][0]])
                                
                            self.disableall()
                            messagebox.showinfo("",f"Purchase D/C Number is {PurchaseDcnumber}")
                        else:
                            messagebox.showwarning("Required","Select Cash OR Credit.")
                    else:
                        messagebox.showwarning("Required","Enter D/C Number.")
                else:
                    messagebox.showwarning("Required","Select Supplier Name.")
            else:
                messagebox.showwarning("Required","Is it Pur D/C OR Pur Bill")
        elif self.type.get() == "Pur Bill":
            if typeof.strip():
                if sname.strip():
                    if dcno.strip():
                        if paytype.strip():
                            if dis == '':
                                dis = 0
                            if charge == '':
                                charge = 0
                            if roundoff == '':
                                roundoff = 0
                            netTotal = (float(charge) + float(roundoff) + float(total)) - float(dis)
                            self.netTotal.configure(state='normal')
                            self.entryNo.configure(state='normal')
                            self.netTotal.delete(0,END)
                            self.entryNo.delete(0,END)
                            self.netTotal.insert(0,netTotal)
                            self.entryNo.insert(0,PurchaseDcnumber)
                            self.netTotal.configure(state='disabled')
                            self.entryNo.configure(state='disabled')
                            if paytype == "credit":
                                selectquery = "select credit from partys where partyid = %s"
                                cur.execute(selectquery,[sid])
                                prevCr = cur.fetchall()
                                newCr = float(prevCr[0][0]) + float(netTotal)
                                updatequery = "update partys set credit = %s where partyid = %s"
                                cur.execute(updatequery,[newCr,sid])
                            status = "inv"
                            allData = self.tree.get_children()
                            for item in allData:
                                data = self.tree.item(item, "values")
                                descr = f"{data[0]} [{dcno}]"
                                selectQuery = "select selling_price from product where product_id = %s"
                                cur.execute(selectQuery,[data[1]])
                                sp = cur.fetchall()
                                insert = ("INSERT INTO purchase(srno, purchasedcid, purchasedcdate, purchaseid, purchasedate, supplierid, suppliername, supplierlocation, dcno, dcdate, billno, billdate, paytype, note, productname, productno, batch_lot, expiry, quantity, rate, taxableamt, gstrate, amount, qtytotal, discount, charge, roundoff, total, nettotal, status, returnqty, saleqty, salereturnqty, availableqty, entrydescription, sellingprice) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                                cur.execute(insert,[None,PurchaseDcnumber,entdate,PurchaseDcnumber,entdate,sid,sname,slocation,dcno,dcdate,billno,billdate,paytype,note,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],totalqty,dis,charge,roundoff,total,netTotal,status,0,0,0,data[4],descr,sp[0][0]])
                                
                            self.disableall()
                            messagebox.showinfo("",f"Purchase D/C Number is {PurchaseDcnumber}")
                        else:
                            messagebox.showwarning("Required","Select Cash OR Credit.")
                    else:
                        messagebox.showwarning("Required","Enter D/C Number.")
                else:
                    messagebox.showwarning("Required","Select Supplier Name.")
            else:
                messagebox.showwarning("Required","Is it Pur D/C OR Pur Bill")
        else:
            messagebox.showwarning("Required","Is it Pur D/C OR Pur Bill")
        mydb.commit()

    def modifyProduct(self):
        self.productName.configure(state='normal')
        self.lotNo.configure(state='normal')
        self.quantity.configure(state='normal')
        self.rate.configure(state='normal')
    
    def changeProduct(self):
        selected_item = self.tree.selection()
        pname = self.productName.get()
        code = self.code.get()
        lno = self.lotNo.get()
        exp = self.expDate.get_date()
        qty = self.quantity.get()
        rate = self.rate.get()
        amt = self.amount.get()
        gst = self.gst.get()
        taxamt = self.taxAmount.get()
        totqty = self.qtytot.get()
        totamt = self.total.get()
        item = self.tree.focus()
        if item:
            olddata = self.tree.item(item, "values")
        if rate == "":
            rate = 0.0
            amt = 0.0
            taxamt = 0.0
        if pname.strip() and qty.strip():
            todaydate = date.today()
            if exp == todaydate:
                exp = None
            newdata = (pname,code,lno,exp,qty,rate,amt,gst,taxamt)
            if selected_item:
                self.tree.item(selected_item, values=newdata)
                self.qtytot.configure(state='normal')
                self.total.configure(state='normal')
                self.qtytot.delete(0,END)
                self.total.delete(0,END)
                if float(newdata[4]) > float(olddata[4]):
                    totqty = float(totqty) + (float(newdata[4]) - float(olddata[4]))
                    self.qtytot.insert(0,totqty)
                else:
                    totqty = float(totqty) - (float(olddata[4]) - float(newdata[4]))
                    self.qtytot.insert(0,totqty)
                
                if float(newdata[8]) > float(olddata[8]):
                    totamt = float(totamt) + (float(newdata[8]) - float(olddata[8]))
                    self.total.insert(0,totamt)
                else:
                    totamt = float(totamt) - (float(olddata[8]) - float(newdata[8]))
                    self.total.insert(0,totamt)

                self.qtytot.configure(state='disabled')
                self.total.configure(state='disabled')
            self.clear()
            self.num = ""

    def toRemoveProductfromCart(self):
        totqty = self.qtytot.get()
        totamt = self.total.get()
        selected_items = self.tree.selection()
        item = self.tree.focus()
        if item:
            data = self.tree.item(item, "values")
            totqty = float(totqty) - float(data[4])
            totamt = float(totamt) - float(data[8])
            self.qtytot.configure(state='normal')
            self.total.configure(state='normal')
            self.qtytot.delete(0,END)
            self.total.delete(0,END)
            self.qtytot.insert(0,totqty)
            self.total.insert(0,totamt)
            self.qtytot.configure(state='disabled')
            self.total.configure(state='disabled')
        
        for item in selected_items:
            self.tree.delete(item)
        self.clear()
        self.num = ""
    
    def onTreeSelect(self,event):
        selected_item = self.tree.focus()
        if selected_item:
            self.clear()
            data = self.tree.item(selected_item, "values")
            self.lotNo.configure(state='normal')
            self.quantity.configure(state='normal')
            self.rate.configure(state='normal')
            self.amount.configure(state='normal')
            self.gst.configure(state='normal')
            self.taxAmount.configure(state='normal')
            self.code.configure(state='normal')
            self.productName.configure(state='normal')
            self.productName.delete(0,END)
            self.code.delete(0,END)
            self.lotNo.delete(0,END)
            self.quantity.delete(0,END)
            self.rate.delete(0,END)
            self.amount.delete(0,END)
            self.gst.delete(0,END)
            self.taxAmount.delete(0,END)
            self.productName.insert(0,data[0])
            self.code.insert(0,data[1])
            self.lotNo.insert(0,data[2])
            self.quantity.insert(0,data[4])
            self.rate.insert(0,data[5])
            self.amount.insert(0,data[6])
            self.gst.insert(0,data[7])
            # self.expDate.set_date(data[3])
            try:
                selected_date = datetime.strptime(data[3], "%Y-%m-%d")
                self.expDate.set_date(selected_date)
            except ValueError:
                print("Invalid format of Expiry date")
            self.taxAmount.insert(0,data[8])
            self.lotNo.configure(state='disabled')
            self.quantity.configure(state='disabled')
            self.rate.configure(state='disabled')
            self.amount.configure(state='disabled')
            self.gst.configure(state='disabled')
            self.taxAmount.configure(state='disabled')
            self.code.configure(state='disabled')
            self.addButton.configure(state='disabled')
    
    def addToCart(self):
        pname = self.productName.get()
        code = self.code.get()
        lno = self.lotNo.get()
        exp = self.expDate.get_date()
        qty = self.quantity.get()
        rate = self.rate.get()
        amt = self.amount.get()
        gst = self.gst.get()
        totqty = self.qtytot.get()
        taxamt = self.taxAmount.get()
        totamt = self.total.get()
        if self.type.get() == "Pur Bill":
            self.discount.configure(state='normal')
            self.charge.configure(state='normal')
            self.roundOff.configure(state='normal')
        if rate == "":
            rate = 0.0
            amt = 0.0
            taxamt = 0.0
        if self.type.get() == "Pur D/C":
            if pname.strip() and qty.strip():
                todaydate = date.today()
                if exp == todaydate:
                    exp = None
                data = (pname,code,lno,exp,qty,rate,amt,gst,taxamt)
                self.tree.insert("", "end", values=data,tags=("item",))
                totqty = float(totqty) + float(qty)
                totamt = float(totamt) + float(taxamt)
                self.qtytot.configure(state='normal')
                self.total.configure(state='normal')
                self.netTotal.configure(state='normal')
                self.qtytot.delete(0,END)
                self.total.delete(0,END)
                self.netTotal.delete(0,END)
                self.qtytot.insert(0,totqty)
                self.total.insert(0,totamt)
                self.qtytot.configure(state='disabled')
                self.total.configure(state='disabled')
                self.netTotal.configure(state='disabled')
                self.clear()
                self.num = ""
            else:
                self.clear()
                self.num = ""
                messagebox.showwarning("Oops...","Re-Enter all details.\nEntry can not be doen.")
        else:
            try:
                if pname.strip() and qty.strip() and rate.strip() and amt.strip() and taxamt.strip():
                    todaydate = date.today()
                    if exp == todaydate:
                        exp = None
                    data = (pname,code,lno,exp,qty,rate,amt,gst,taxamt)
                    self.tree.insert("", "end", values=data,tags=("item",))
                    totqty = float(totqty) + float(qty)
                    totamt = float(totamt) + float(taxamt)
                    self.qtytot.configure(state='normal')
                    self.total.configure(state='normal')
                    self.netTotal.configure(state='normal')
                    self.qtytot.delete(0,END)
                    self.total.delete(0,END)
                    self.netTotal.delete(0,END)
                    self.qtytot.insert(0,totqty)
                    self.total.insert(0,totamt)
                    self.qtytot.configure(state='disabled')
                    self.total.configure(state='disabled')
                    self.netTotal.configure(state='disabled')
                    self.clear()
                    self.num = ""
                else:
                    self.clear()
                    self.num = ""
                    messagebox.showwarning("Oops...","Re-Enter all details.\nEntry can not be doen.")
            except Exception as e:
                self.clear()
                self.num = ""
                messagebox.showwarning("Oops...",f"Re-Enter all details.\nEntry can not be doen.\nBeacouse of {e}")

    def validateFloat(self, value, action_type):
        if action_type == '1':
            try:
                if value == '.':
                    return True
                float(value)
                return True
            except ValueError:
                return False
        return True
    
    def keyWorkRate(self,event):
        try:
            if self.validateFloat(event.char,'1'):
                if float(self.gst.get()) > 0:
                    self.amount.configure(state="normal")
                    self.taxAmount.configure(state="normal")
                    self.amount.delete(0,END)
                    self.taxAmount.delete(0,END)
                    self.num = self.num + event.char
                    number = float(self.num)*float(self.quantity.get())
                    x = float(number) - (float(number) / (100 + float(self.gst.get()))) * float(self.gst.get())
                    # x = float(self.num) - (float(self.num) / (100 + float(self.gst.get()))) * float(self.gst.get())
                    self.amount.insert(0,x)
                    self.taxAmount.insert(0,(number))
                    self.amount.configure(state="disabled")
                    self.taxAmount.configure(state="disabled")
                else:
                    self.amount.configure(state="normal")
                    self.taxAmount.configure(state="normal")
                    self.amount.delete(0,END)
                    self.taxAmount.delete(0,END)
                    self.num = self.num + event.char
                    number = float(self.num)*float(self.quantity.get())
                    self.amount.insert(0,number)
                    self.taxAmount.insert(0,number)
                    self.amount.configure(state="disabled")
                    self.taxAmount.configure(state="disabled")
            else:
                    self.amount.configure(state="normal")
                    self.taxAmount.configure(state="normal")
                    self.amount.delete(0,END)
                    self.taxAmount.delete(0,END)
                    self.amount.insert(0,0.00)
                    self.taxAmount.insert(0,0.00)
                    self.amount.configure(state="disabled")
                    self.taxAmount.configure(state="disabled")
                    self.num = ''
                    self.rate.delete(0,END)

        except Exception as e:
            self.clear()
            self.num = ""
            messagebox.showerror("Error",f"Error: {e}")
            self.rate.delete(0, END)
            self.rate.configure(state="disabled")
            self.taxAmount.configure(state="disabled")
     
    def clear(self):
        self.productName.delete(0, END)
        self.amount.configure(state="normal")
        self.gst.configure(state="normal")
        self.taxAmount.configure(state="normal")
        self.code.configure(state="normal")
        self.rate.configure(state="normal")
        self.lotNo.configure(state="normal")
        self.quantity.configure(state="normal")
        self.amount.delete(0, END)
        self.lotNo.delete(0, END)
        self.quantity.delete(0, END)
        self.rate.delete(0, END)
        self.gst.delete(0, END)
        self.taxAmount.delete(0, END)
        self.code.delete(0, END)
        self.amount.configure(state="disabled")
        self.gst.configure(state="disabled")
        self.lotNo.configure(state="disabled")
        self.quantity.configure(state="disabled")
        self.rate.configure(state="disabled")
        self.taxAmount.configure(state="disabled")
        self.code.configure(state="disabled")
        self.addButton.configure(state='normal')
        todaydate = date.today()
        try:
            self.expDate.set_date(todaydate)
        except ValueError:
            print("Invalid format of Expiry date")