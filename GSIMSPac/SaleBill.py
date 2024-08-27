# ==================( IMPORT )==================
from datetime import date
from tkinter import *
import re
import string
import mysql.connector
import random
# import psutil
# from datetime import date
from tkinter import ttk
from GSIMSPac import fun
# from GSIMSPac import Product
# from GSIMSPac import Partys
# from GSIMSPac import PurchaseDC
# from GSIMSPac import PurchaseInvoice
# from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
# ===============================================

def valid_adhar(adhar):
    if re.match(r"\d{12}$", adhar) or adhar == "":
        return True
    return False

def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn) or phn == "":
        return True
    return False

def cid():
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for _ in range(2))
    result0 = random.randint(1000,9999)
    number = f"{result}{result0}"
    return number

def saleBillId():
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for _ in range(2))
    result0 = random.randint(100000,999999)
    bill_number = f"{result}{result0}"
    return bill_number

class SaleBill:
    def __init__(self,canvas_widget):
        
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        self.cursor = self.mydb.cursor()
        self.num = ""
        self.numqty = ""
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
        self.entryNo.configure(width=10)
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

        self.customerId = Entry(self.root)
        self.customerId.place(relx=0.571,rely=0.02)
        self.customerId.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="#05591c")
        self.customerId.configure(width=10)
        self.customerId.configure(bg="#e5e6d5")
        self.customerId.configure(font=f2)

        self.customerNameVar = StringVar()
        self.customerNameLabel = Label(self.root)
        self.customerNameLabel.place(relx=0.05,rely=0.07)
        self.customerNameLabel.configure(text="customer Name:")
        self.customerNameLabel.configure(bg="#ad995e")
        self.customerNameLabel.configure(fg="#6e5a20")
        self.customerNameLabel.configure(font=f3)
        self.cursor.execute("SELECT customername FROM customer")
        self.customer = self.cursor.fetchall()
        self.customerName = ttk.Combobox(self.root,values=[cus[0] for cus in self.customer],textvariable=self.customerNameVar)
        self.customerNameConboVal = [cus[0] for cus in self.customer]
        self.customerName.place(relx=0.05,rely=0.11)
        self.customerName.configure(width=28)
        self.customerName.configure(font=f2)
        def customers(event):
            self.customerId.configure(state='normal')
            self.customerMoNo.delete(0,END)
            self.customerLocation.delete(0,END)
            self.customerAdhar.delete(0,END)
            self.customerId.delete(0,END)
            self.customerId.configure(state='disabled')
            currentCustomer = self.customerNameVar.get().lower()
            matching_items = [item for item in self.customerNameConboVal if currentCustomer in item.lower()]
            self.customerName['values'] = matching_items
        self.customerName.bind("<KeyRelease>", customers)
        def onSelectCustomerName(event):
            selected_item = self.customerName.get()
            select_query3 = "select customermobileno,customeraddress,customeradharno,customerid from customer where customername = %s"
            self.cursor.execute(select_query3,[selected_item,])
            data = self.cursor.fetchall()
            self.customerId.configure(state='normal')
            self.customerMoNo.delete(0,END)
            self.customerLocation.delete(0,END)
            self.customerAdhar.delete(0,END)
            self.customerId.delete(0,END)
            self.customerMoNo.insert(END, data[0][0])
            self.customerLocation.insert(END, data[0][1])
            self.customerAdhar.insert(END, data[0][2])
            self.customerId.insert(END, data[0][3])
            self.customerId.configure(state='disabled')
        self.customerName.bind("<<ComboboxSelected>>", onSelectCustomerName)

        self.customerMoNoLabel = Label(self.root)
        self.customerMoNoLabel.place(relx=0.315,rely=0.07)
        self.customerMoNoLabel.configure(text="Mobile No:")
        self.customerMoNoLabel.configure(bg="#ad995e")
        self.customerMoNoLabel.configure(fg="#6e5a20")
        self.customerMoNoLabel.configure(font=f3)
        self.customerMoNo = Entry(self.root)
        self.customerMoNo.place(relx=0.315,rely=0.11)
        self.customerMoNo.configure(width=13)
        self.customerMoNo.configure(bg="#e5e6d5")
        self.customerMoNo.configure(font=f2)
        # self.customerMoNo.configure(state="disabled")

        self.customerlocaLabel = Label(self.root)
        self.customerlocaLabel.place(relx=0.443,rely=0.07)
        self.customerlocaLabel.configure(text="Address:")
        self.customerlocaLabel.configure(bg="#ad995e")
        self.customerlocaLabel.configure(fg="#6e5a20")
        self.customerlocaLabel.configure(font=f3)
        self.customerLocation = Entry(self.root)
        self.customerLocation.place(relx=0.443,rely=0.11)
        self.customerLocation.configure(width=13)
        self.customerLocation.configure(bg="#e5e6d5")
        self.customerLocation.configure(font=f2)
        # self.customerLocation.configure(state="disabled")
        
        self.customerAdharLabel = Label(self.root)
        self.customerAdharLabel.place(relx=0.571,rely=0.07)
        self.customerAdharLabel.configure(text="Adhar No:")
        self.customerAdharLabel.configure(bg="#ad995e")
        self.customerAdharLabel.configure(fg="#6e5a20")
        self.customerAdharLabel.configure(font=f3)
        self.customerAdhar = Entry(self.root)
        self.customerAdhar.place(relx=0.571,rely=0.11)
        self.customerAdhar.configure(width=13)
        self.customerAdhar.configure(bg="#e5e6d5")
        self.customerAdhar.configure(font=f2)
        # self.customerAdhar.configure(state="disabled")
                
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
        self.pname = ""
        self.productNameLabel = Label(self.root)
        self.productNameLabel.place(relx=0.02,rely=0.21)
        self.productNameLabel.configure(text="Item Name")
        self.productNameLabel.configure(bg="#ad995e")
        self.productNameLabel.configure(fg="#6e5a20")
        self.productNameLabel.configure(font=f4)
        self.cursor.execute("SELECT entrydescription FROM purchase where availableqty > %s and (status = %s or status = %s)",[0,"dc","inv"])
        # self.cursor.execute("SELECT entrydescription FROM purchase where availableqty > %s",[0])
        self.products = self.cursor.fetchall()
        self.productName = ttk.Combobox(self.root,values=[prod[0] for prod in self.products],textvariable=self.productNameVar)
        self.productNameConboVal = [prod[0] for prod in self.products]
        self.productName.place(relx=0.02,rely=0.258)
        self.productName.configure(width=20)
        self.productName.configure(font=f2)
        # self.productName.configure(state="disabled")
        def update_combobox(event):
            current_input = self.productNameVar.get().lower()
            matching_items = [item for item in self.productNameConboVal if current_input in item.lower()]
            self.productName['values'] = matching_items
        self.productName.bind("<KeyRelease>", update_combobox)
        def onSelectProductName(event):
            selectedProduct = self.productName.get()
            self.cursor.execute("SELECT gstrate,purchasedcid,expiry,batch_lot,availableqty,rate,sellingprice,productname FROM purchase where entrydescription=%s",[selectedProduct,])
            data = self.cursor.fetchall()
            self.gst.configure(state="normal")
            self.rate.configure(state='normal')
            self.code.configure(state="normal")
            self.expDate.configure(state="normal")
            self.lotNo.configure(state="normal")
            self.availableqty.configure(state="normal")
            self.cRate.configure(state="normal")
            self.gst.delete(0,END)
            self.code.delete(0,END)
            self.expDate.delete(0,END)
            self.lotNo.delete(0,END)
            self.availableqty.delete(0,END)
            self.cRate.delete(0,END)
            self.rate.delete(0,END)
            self.gst.insert(0, data[0][0])
            self.code.insert(0, data[0][1])
            self.expDate.insert(0, data[0][2])
            self.lotNo.insert(0, data[0][3])
            self.availableqty.insert(0,data[0][4])
            self.cRate.insert(0,data[0][5])
            self.rate.insert(0,data[0][6])
            self.pname = data[0][7]
            self.gst.configure(state="disabled")
            self.lotNo.configure(state="disabled")
            self.code.configure(state="disabled")
            self.lotNo.configure(state="disabled")
            self.expDate.configure(state="disabled")
            self.availableqty.configure(state="disabled")
            self.cRate.configure(state="disabled")
            self.quantity.configure(state="normal")
        self.productName.bind("<<ComboboxSelected>>", onSelectProductName)

        self.code = Entry(self.root)
        self.code.place(relx=0.02,rely=0.32)
        self.code.configure(width=6)
        self.code.configure(bg="#e5e6d5")
        self.code.configure(font=f2)
        self.code.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black") 
        
        self.availableqty = Entry(self.root)
        self.availableqty.place(relx=0.08,rely=0.32)
        self.availableqty.configure(width=6)
        self.availableqty.configure(bg="#e5e6d5")
        self.availableqty.configure(font=f2)
        self.availableqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black") 
        
        self.cRate = Entry(self.root)
        self.cRate.place(relx=0.14,rely=0.32)
        self.cRate.configure(width=6)
        self.cRate.configure(bg="#e5e6d5")
        self.cRate.configure(font=f2)
        self.cRate.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")  
        
        self.gstRate = Entry(self.root)
        self.gstRate.place(relx=0.22,rely=0.32)
        self.gstRate.configure(width=6)
        self.gstRate.configure(bg="#e5e6d5")
        self.gstRate.configure(font=f2)
        self.gstRate.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")        
        
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
        self.expDate = Entry(self.root)
        self.expDate.place(relx=0.32,rely=0.258)
        self.expDate.configure(width=10)
        self.expDate.configure(font=f2)
        self.expDate.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        
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
        self.quantity.bind("<Key>", self.keyWorkQty)
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
        self.scrollbary.place(relx=0.845, rely=0.41, width=18, height=255)

        self.tree = ttk.Treeview(self.root)
        self.tree.place(relx=0.01, rely=0.44, width=1000, height=240)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.configure(command=self.tree.yview)
        
        self.tree.configure(
            columns=(
                "Item Name",
                "Batch/Lot",
                "Expiry",
                "Quantity",
                "Rate",
                "Taxable amt",
                "GST %",
                "GST Amt",
                "Amount",
                "Description",
                "Item No",
                "PurD/C ID",
                "Cost Rate"
            )
        )

        self.tree.heading("Item Name", text="Item Name", anchor=W)
        self.tree.heading("Batch/Lot", text="Batch/Lot", anchor=W)
        self.tree.heading("Expiry", text="Expiry", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Rate", text="Rate", anchor=W)
        self.tree.heading("Taxable amt", text="Taxable amt", anchor=W)
        self.tree.heading("GST %", text="GST %", anchor=W)
        self.tree.heading("GST Amt", text="GST Amt", anchor=W)
        self.tree.heading("Amount", text="Amount", anchor=W)
        self.tree.heading("Description", text="Description", anchor=W)
        self.tree.heading("Item No", text="Item No", anchor=W)
        self.tree.heading("PurD/C ID", text="PurD/C ID", anchor=W)
        self.tree.heading("Cost Rate", text="Cost Rate", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=230)
        self.tree.column("#2", stretch=NO, minwidth=0, width=91)
        self.tree.column("#3", stretch=NO, minwidth=0, width=110)
        self.tree.column("#4", stretch=NO, minwidth=0, width=80)
        self.tree.column("#5", stretch=NO, minwidth=0, width=100)
        self.tree.column("#6", stretch=NO, minwidth=0, width=110)
        self.tree.column("#7", stretch=NO, minwidth=0, width=80)
        self.tree.column("#8", stretch=NO, minwidth=0, width=110)
        self.tree.column("#9", stretch=NO, minwidth=0, width=100)
        self.tree.column("#10", stretch=NO, minwidth=0, width=270)
        self.tree.column("#11", stretch=NO, minwidth=0, width=100)
        self.tree.column("#12", stretch=NO, minwidth=0, width=110)
        self.tree.column("#13", stretch=NO, minwidth=0, width=110)
        self.tree.configure(selectmode="extended")
        self.tree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.tree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        
        self.qtytotLabel = Label(self.root)
        self.qtytotLabel.place(relx=0.31,rely=0.85)
        self.qtytotLabel.configure(text="Qty Total")
        self.qtytotLabel.configure(bg="#ad995e")
        self.qtytotLabel.configure(fg="#6e5a20")
        self.qtytotLabel.configure(font=f5)
        self.qtytot = Entry(self.root)
        self.qtytot.place(relx=0.37,rely=0.85)
        self.qtytot.configure(width=10)
        self.qtytot.configure(bg="#e5e6d5")
        self.qtytot.configure(font=f2)
        self.qtytot.insert(0,0.0)
        self.qtytot.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.qtytot.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.discountLabel = Label(self.root)
        self.discountLabel.place(relx=0.51,rely=0.85)
        self.discountLabel.configure(text="Discount")
        self.discountLabel.configure(bg="#ad995e")
        self.discountLabel.configure(fg="#6e5a20")
        self.discountLabel.configure(font=f5)
        self.discount = Entry(self.root)
        self.discount.place(relx=0.57,rely=0.85)
        self.discount.configure(width=10)
        self.discount.configure(bg="#e5e6d5")
        self.discount.configure(font=f2)
        self.discount.configure(state="disabled",disabledbackground="#fce89d")
        self.discount.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.chargeLabel = Label(self.root)
        self.chargeLabel.place(relx=0.52,rely=0.9)
        self.chargeLabel.configure(text="Charge")
        self.chargeLabel.configure(bg="#ad995e")
        self.chargeLabel.configure(fg="#6e5a20")
        self.chargeLabel.configure(font=f5)
        self.charge = Entry(self.root)
        self.charge.place(relx=0.57,rely=0.9)
        self.charge.configure(width=10)
        self.charge.configure(bg="#e5e6d5")
        self.charge.configure(font=f2)
        self.charge.configure(state="disabled",disabledbackground="#fce89d")
        self.charge.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.roundOffLabel = Label(self.root)
        self.roundOffLabel.place(relx=0.5,rely=0.95)
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
        self.totalLabel.place(relx=0.711,rely=0.85)
        self.totalLabel.configure(text="Total")
        self.totalLabel.configure(bg="#ad995e")
        self.totalLabel.configure(fg="#6e5a20")
        self.totalLabel.configure(font=f5)
        self.total = Entry(self.root)
        self.total.place(relx=0.75,rely=0.85)
        self.total.configure(width=10)
        self.total.configure(bg="#e5e6d5")
        self.total.configure(font=f2)
        self.total.insert(0,0.0)
        self.total.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.total.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        
        self.netTotalLabel = Label(self.root)
        self.netTotalLabel.place(relx=0.688,rely=0.90)
        self.netTotalLabel.configure(text="Net Total")
        self.netTotalLabel.configure(bg="#ad995e")
        self.netTotalLabel.configure(fg="#6e5a20")
        self.netTotalLabel.configure(font=f5)
        self.netTotal = Entry(self.root)
        self.netTotal.place(relx=0.75,rely=0.90)
        self.netTotal.configure(width=10)
        self.netTotal.configure(bg="#e5e6d5")
        self.netTotal.configure(font=f2)
        self.netTotal.insert(0,0.0)
        self.netTotal.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.netTotal.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))

        self.addBillButton = Button(self.root, height=1)
        self.addBillButton.place(relx=0.878,rely=0.46)
        self.addBillButton.configure(text="Add Bill")
        self.addBillButton.configure(font=f1)
        self.addBillButton.configure(width=12)
        self.addBillButton.configure(activebackground="#ad995e")
        self.addBillButton.configure(bg="#e0cb8d")
        self.addBillButton.configure(command=self.addBill)

        self.searchBillButton = Button(self.root, height=1)
        self.searchBillButton.place(relx=0.878,rely=0.52)
        self.searchBillButton.configure(text="Search")
        self.searchBillButton.configure(font=f1)
        self.searchBillButton.configure(width=12)
        self.searchBillButton.configure(activebackground="#ad995e")
        self.searchBillButton.configure(bg="#e0cb8d")
        self.searchBillButton.configure(command=self.searchButton)
        
        self.printBillButton = Button(self.root, height=1)
        self.printBillButton.place(relx=0.878,rely=0.58)
        self.printBillButton.configure(text="Print")
        self.printBillButton.configure(font=f1)
        self.printBillButton.configure(width=12)
        self.printBillButton.configure(activebackground="#ad995e")
        self.printBillButton.configure(bg="#e0cb8d")
        self.printBillButton.configure(state='disabled')
        self.printBillButton.configure(command=self.printSaleBill)

        self.updateBillButton = Button(self.root, height=1)
        self.updateBillButton.place(relx=0.878,rely=0.64)
        self.updateBillButton.configure(text="Update")
        self.updateBillButton.configure(font=f1)
        self.updateBillButton.configure(width=12)
        self.updateBillButton.configure(activebackground="#ad995e")
        self.updateBillButton.configure(bg="#e0cb8d")
        self.updateBillButton.configure(state='disabled')

        self.deleteBillButton = Button(self.root, height=1)
        self.deleteBillButton.place(relx=0.878,rely=0.70)
        self.deleteBillButton.configure(text="Delete")
        self.deleteBillButton.configure(font=f1)
        self.deleteBillButton.configure(width=12)
        self.deleteBillButton.configure(activebackground="#ad995e")
        self.deleteBillButton.configure(bg="#e0cb8d")
        self.deleteBillButton.configure(state='disabled')
        # self.deleteBillButton.configure(command=self.deleteBill)

        self.cancelBillButton = Button(self.root, height=1)
        self.cancelBillButton.place(relx=0.878,rely=0.76)
        self.cancelBillButton.configure(text="New Bill")
        self.cancelBillButton.configure(font=f1)
        self.cancelBillButton.configure(width=12)
        self.cancelBillButton.configure(activebackground="#ad995e")
        self.cancelBillButton.configure(bg="#e0cb8d")
        self.cancelBillButton.configure(command=self.newBill)

        self.mydb.commit()
        
    def searchButton(self):
        # print("Its Work")
        f6 = ('times', 8)
        self.newBill()
        self.close()
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
            query = "select * from sale where entryno = %s"
            cur.execute(query,[data,])
            billData = cur.fetchall()
            
            if not billData:
                messagebox.showwarning("Warning","Invoice number is invalid.")
                self.entryNo.delete(0,END)
                self.entryNo.configure(state='disabled')
                self.nextSearchButton.configure(state='disabled')
                self.newBill()
                
            elif billData[0][29] == "del":
                messagebox.showwarning("Warning","Invoice Not found.")
                self.entryNo.delete(0,END)
                self.entryNo.configure(state='disabled')
                self.nextSearchButton.configure(state='disabled')
                self.newBill()
                
            else:
                self.open()
                self.tree.delete(*self.tree.get_children())
                try:
                    print(billData[0][2])
                    print(type(billData[0][2]))
                    # MyTestDate = "2023-01-01"
                    self.entryDate.set_date(billData[0][2])
                except ValueError:
                    print("Invalid format of date")

                self.note.delete(0,END)
                self.customerId.delete(0,END)
                self.customerName.delete(0,END)
                self.customerMoNo.delete(0,END)
                self.customerLocation.delete(0,END)
                self.customerAdhar.delete(0,END)
                self.productName.delete(0,END)
                self.code.delete(0,END)
                self.expDate.delete(0,END)
                self.availableqty.delete(0,END)
                self.gstRate.delete(0,END)
                self.cRate.delete(0,END)
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

                if billData[0][8] == "cash":
                    self.cashButton.select()
                else:
                    self.creditButton.select()
                                   
                if billData[0][28] != None:
                    self.netTotal.insert(0,billData[0][28]) 
                else:
                    self.netTotal.insert(0,0.0)                
                    
                if billData[0][27] != None:
                    self.total.insert(0,float(billData[0][27]))
                else:
                    self.total.insert(0,0.0)                 
                    
                if billData[0][24] != None:
                    self.discount.insert(0,billData[0][24])
                else:
                    self.discount.insert(0,0.0)                  
                    
                if billData[0][23] != None:
                    self.qtytot.insert(0,billData[0][23])
                else:
                    self.qtytot.insert(0,0.0)                  
                    
                if billData[0][25] != None:
                    self.charge.insert(0,billData[0][25])
                else:
                    self.charge.insert(0,0.0)                  

                if billData[0][26] != None:
                    self.roundOff.insert(0,billData[0][26])
                else:
                    self.roundOff.insert(0,0.0)  

                self.customerId.insert(0,billData[0][4])
                self.customerName.insert(0,billData[0][3])
                self.customerMoNo.insert(0,billData[0][5])
                self.customerLocation.insert(0,billData[0][6])
                self.customerAdhar.insert(0,billData[0][7])
                self.note.insert(0,billData[0][9])

                todaydate = date.today()
                
                for product in billData:
                    data = (product[10],product[11],product[12],product[13],product[14],product[15],product[16],product[17],product[18],product[19],product[20],product[21],product[22])
                    self.tree.insert("", "end", values=data,tags=("item",))

                self.close()
                self.printBillButton.configure(state='normal')
            mydb.commit()
        else:
            messagebox.showwarning("Warning","Enter Entry Number")

    def printSaleBill(self):
        if self.entryNo.get():
            fun.generate_invoice(self.entryNo.get())

    def disabledall(self):
        self.clear()
        self.entryNo.configure(state='disabled')
        self.customerLocation.configure(state='disabled')
        self.productName.configure(state='disabled')
        self.customerAdhar.configure(state='disabled')
        self.customerMoNo.configure(state='disabled')
        self.note.configure(state='disabled')
        self.customerName.configure(state='disabled')
        self.lotNo.configure(state='disabled')
        self.quantity.configure(state='disabled')
        self.rate.configure(state='disabled')
        self.addButton.configure(state='disabled')
        self.changeButton.configure(state='disabled')
        self.modifyButton.configure(state='disabled')
        self.removeButton.configure(state='disabled')
        self.addBillButton.configure(state='disabled')
        self.discount.configure(state='disabled')
        self.charge.configure(state='disabled')
        self.roundOff.configure(state='disabled')
        self.printBillButton.configure(state='normal')
        
    def keyWorkRate(self,event):
        try:
            if self.validateFloat(event.char,'1'):
                if float(self.gst.get()) > 0:
                    self.amount.configure(state="normal")
                    self.taxAmount.configure(state="normal")
                    self.gstRate.configure(state="normal")
                    self.amount.delete(0,END)
                    self.taxAmount.delete(0,END)
                    self.gstRate.delete(0,END)
                    self.num = self.num + event.char
                    number = float(self.num)*float(self.quantity.get())
                    x = float(number) - (float(number) / (100 + float(self.gst.get()))) * float(self.gst.get())
                    self.amount.insert(0,x)
                    self.taxAmount.insert(0,(number))
                    self.gstRate.insert(0,(float(number) - x))
                    self.amount.configure(state="disabled")
                    self.taxAmount.configure(state="disabled")
                    self.gstRate.configure(state="disabled")
                else:
                    self.amount.configure(state="normal")
                    self.taxAmount.configure(state="normal")
                    self.gstRate.configure(state="normal")
                    self.amount.delete(0,END)
                    self.taxAmount.delete(0,END)
                    self.gstRate.delete(0,END)
                    self.num = self.num + event.char
                    number = float(self.num)*float(self.quantity.get())
                    self.amount.insert(0,number)
                    self.taxAmount.insert(0,number)
                    self.gstRate.insert(0,0.0)
                    self.amount.configure(state="disabled")
                    self.taxAmount.configure(state="disabled")
                    self.gstRate.configure(state="disabled")
            else:
                    self.num = ''

        except Exception as e:
            self.clear()
            self.num = ""
            messagebox.showerror("Error",f"Error: {e}")
            self.rate.delete(0, END)
            self.rate.configure(state="disabled")
            self.taxAmount.configure(state="disabled")

    def modifyProduct(self):
        self.quantity.configure(state='normal')
        self.rate.configure(state='normal')

    def changeProduct(self):
        selected_item = self.tree.selection()
        productname = self.productName.get()
        code = self.code.get()
        lno = self.lotNo.get()
        exp = self.expDate.get()
        qty = self.quantity.get()
        rate = self.rate.get()
        amt = self.amount.get()
        crate = self.cRate.get()
        gst = self.gst.get()
        gstrate = self.gstRate.get()
        totqty = self.qtytot.get()
        taxamt = self.taxAmount.get()
        totamt = self.total.get()
        item = self.tree.focus()

        self.cursor.execute("select availableqty from purchase where entrydescription = %s and purchasedcid = %s",[productname,code])
        pData = self.cursor.fetchall()
        if productname.strip() and qty.strip() and rate.strip():
            result = float(pData[0][0]) - float(qty)
            if selected_item:
                if item:
                    olddata = self.tree.item(item, "values")
                if productname.strip() and qty.strip() and rate.strip():
                    newdata = (olddata[0],lno,exp,qty,rate,amt,gst,gstrate,taxamt,productname,olddata[10],code,crate)
                    if result >= 0:
                        self.tree.item(selected_item, values=newdata)
                        self.qtytot.configure(state='normal')
                        self.total.configure(state='normal')
                        self.qtytot.delete(0,END)
                        self.total.delete(0,END)
                        if float(newdata[3]) > float(olddata[3]):
                            totqty = float(totqty) + (float(newdata[3]) - float(olddata[3]))
                            self.qtytot.insert(0,totqty)
                        else:
                            totqty = float(totqty) - (float(olddata[3]) - float(newdata[3]))
                            self.qtytot.insert(0,totqty)

                        if float(newdata[8]) > float(olddata[8]):
                            totamt = float(totamt) + (float(newdata[8]) - float(olddata[8]))
                            self.total.insert(0,totamt)
                        else:
                            totamt = float(totamt) - (float(olddata[8]) - float(newdata[8]))
                            self.total.insert(0,totamt)

                        self.qtytot.configure(state='disabled')
                        self.total.configure(state='disabled')
                        self.addBillButton.configure(state='normal')
                        self.addButton.configure(state='normal')
                        self.clear()
                        self.num = ""
                        self.numqty = ""
                    else:
                        messagebox.showinfo("",f"This transaction can not be doen\nbeacuse available quantity is {pData[0][0]} for sale.")
                        self.clear()
                        self.num = ""
                        self.numqty = ""

    def toRemoveProductfromCart(self):
        totqty = self.qtytot.get()
        totamt = self.total.get()
        selected_items = self.tree.selection()
        item = self.tree.focus()
        if selected_items:
            if item:
                data = self.tree.item(item, "values")
                totqty = float(totqty) - float(data[3])
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
            self.numqty = ""
            self.addBillButton.configure(state='normal')
            self.addButton.configure(state='normal')

    def keyWorkQty(self,event):
        r = self.rate.get()
        try:
            if r.strip():
                if self.validateFloat(event.char,'1'):
                    if float(self.gst.get()) > 0:
                        self.amount.configure(state="normal")
                        self.taxAmount.configure(state="normal")
                        self.gstRate.configure(state="normal")
                        self.amount.delete(0,END)
                        self.taxAmount.delete(0,END)
                        self.gstRate.delete(0,END)
                        self.numqty = self.numqty + event.char
                        number = float(self.numqty)*float(r)
                        x = float(number) - (float(number) / (100 + float(self.gst.get()))) * float(self.gst.get())
                        self.amount.insert(0,x)
                        self.taxAmount.insert(0,(number))
                        self.gstRate.insert(0,(float(number) - x))
                        self.amount.configure(state="disabled")
                        self.taxAmount.configure(state="disabled")
                        self.gstRate.configure(state="disabled")
                    else:
                        self.amount.configure(state="normal")
                        self.taxAmount.configure(state="normal")
                        self.gstRate.configure(state="normal")
                        self.amount.delete(0,END)
                        self.taxAmount.delete(0,END)
                        self.gstRate.delete(0,END)
                        self.numqty = self.numqty + event.char
                        number = float(self.numqty)*float(r)
                        self.amount.insert(0,number)
                        self.taxAmount.insert(0,number)
                        self.gstRate.insert(0,0.0)
                        self.amount.configure(state="disabled")
                        self.taxAmount.configure(state="disabled")
                    self.gstRate.configure(state="disabled")
                else:
                        self.numqty = ''

        except Exception as e:
            self.clear()
            self.numqty = ""
            messagebox.showerror("Error",f"Error: {e}")
            self.rate.delete(0, END)
            self.rate.configure(state="disabled")
            self.taxAmount.configure(state="disabled")
    
    def clear(self):
        self.productName.configure(state="normal")
        self.productName.delete(0, END)
        self.amount.configure(state="normal")
        self.gst.configure(state="normal")
        self.taxAmount.configure(state="normal")
        self.code.configure(state="normal")
        self.rate.configure(state="normal")
        self.lotNo.configure(state="normal")
        self.quantity.configure(state="normal")
        self.cRate.configure(state="normal")
        self.availableqty.configure(state="normal")
        self.expDate.configure(state="normal")
        self.gstRate.configure(state="normal")
        self.amount.delete(0, END)
        self.lotNo.delete(0, END)
        self.quantity.delete(0, END)
        self.rate.delete(0, END)
        self.gst.delete(0, END)
        self.taxAmount.delete(0, END)
        self.code.delete(0, END)
        self.cRate.delete(0, END)
        self.availableqty.delete(0, END)
        self.expDate.delete(0, END)
        self.gstRate.delete(0, END)
        self.amount.configure(state="disabled")
        self.gst.configure(state="disabled")
        self.lotNo.configure(state="disabled")
        self.quantity.configure(state="disabled")
        self.rate.configure(state="disabled")
        self.taxAmount.configure(state="disabled")
        self.code.configure(state="disabled")
        self.cRate.configure(state="disabled")
        self.availableqty.configure(state="disabled")
        self.expDate.configure(state="disabled")
        self.gstRate.configure(state="disabled")
        self.addButton.configure(state='normal')

    def addBill(self):
        customerid = self.customerId.get()
        customername = self.customerName.get()
        customermono = self.customerMoNo.get()
        customeraddress = self.customerLocation.get()
        customeradhar = self.customerAdhar.get()
        cidno = cid()
        saleBillNo = saleBillId()
        totalqty = self.qtytot.get()
        dis = self.discount.get()
        charge = self.charge.get()
        roundoff = self.roundOff.get()
        total = self.total.get()
        netTotal = self.netTotal.get()
        paytype = self.radiooption.get()
        entrydate = self.entryDate.get_date()
        note = self.note.get()

        if customername.strip():
            
            query = "select * from customer where customername = %s and customerid = %s"
            self.cursor.execute(query,[customername,customerid])
            customerData = self.cursor.fetchall()
            self.mydb.commit()
            if customermono == "":
                customermono = ""
            if customeraddress == "":
                customeraddress = ""
            if customeradhar == "":
                customeradhar = ""
            if customerData:
                updateCustomer = "update customer set customermobileno = %s, customeraddress = %s, customeradharno = %s where customerid = %s and customername = %s"
                self.cursor.execute(updateCustomer,[customermono,customeraddress,customeradhar,customerid,customername])
                self.mydb.commit()
            else:
                query = "select * from customer where customername = %s"
                self.cursor.execute(query,[customername])
                customerData = self.cursor.fetchall()
                self.mydb.commit()
                if customerData:
                    self.customerId.configure(state='normal')
                    self.customerId.delete(0,END)
                    self.customerId.insert(END,customerData[0][1])
                    self.customerId.configure(state='disabled')
                    updateCustomer = "update customer set customermobileno = %s, customeraddress = %s, customeradharno = %s where customername = %s"
                    self.cursor.execute(updateCustomer,[customermono,customeraddress,customeradhar,customername])
                    self.mydb.commit()
                else:
                    newCustomer = "insert into customer(srno,customerid,customername,customermobileno,customeraddress,customeradharno,debit,credit) value(%s,%s,%s,%s,%s,%s,%s,%s)"
                    self.cursor.execute(newCustomer,[None,cidno,customername,customermono,customeraddress,customeradhar,0,0])
                    customerid = cidno
                    self.customerId.configure(state='normal')
                    self.customerId.delete(0,END)
                    self.customerId.insert(END,cidno)
                    self.customerId.configure(state='disabled')
                    self.mydb.commit()
        else:
            customername = "Cash"
            customerid = "UZ9014"
            customermono = ""
            customeraddress = ""
            customeradhar = ""

        allData = self.tree.get_children()
        if paytype == "cash":
            if valid_phone(customermono):
                if valid_adhar(customeradhar):
                    if allData:
                        # messagebox.showinfo("",f"Id - {customerid}\nname - {customername}\nMobile no - {customermono}\naddress - {customeraddress}\nAdhar no - {customeradhar}")
                        if dis == '':
                            dis = 0
                        if charge == '':
                            charge = 0
                        if roundoff == '':
                            roundoff = 0
                        netTotal = (float(charge) + float(roundoff) + float(total)) - float(dis)
                        for item in allData:
                            data = self.tree.item(item, "values")
                            self.cursor.execute("select saleqty,availableqty from purchase where entrydescription = %s and purchasedcid = %s",[data[9],data[11]])
                            oldQty = self.cursor.fetchall()
                            self.cursor.execute("update purchase set saleqty = %s, availableqty = %s where entrydescription = %s and purchasedcid = %s",[(float(oldQty[0][0]) + float(data[3])),(float(oldQty[0][1]) - float(data[3])),data[9],data[11]])
                            insertQuery = "insert into sale(srno,entryno,entrydate,customername,customerid,customermobileno,customeraddress,customeradharno,paytype,note,productname,batch_lot,expiry,quantity,sellingprice,taxableamt,gstrate,gstamt,amount,description,productno,purchasedcid,costprice,totalqty,discount,charge,roundoff,total,nettotal,status,returnqty,avforreturnqty) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            self.cursor.execute(insertQuery,[None,saleBillNo,entrydate,customername,customerid,customermono,customeraddress,customeradhar,paytype,note,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],totalqty,dis,charge,roundoff,total,netTotal,"active",0,data[3]])        
                            self.mydb.commit()
                        self.netTotal.configure(state='normal')
                        self.entryNo.configure(state='normal')
                        self.netTotal.delete(0,END)
                        self.entryNo.delete(0,END)
                        self.netTotal.insert(0,netTotal)
                        self.entryNo.insert(0,saleBillNo)
                        self.netTotal.configure(state='disabled')
                        self.entryNo.configure(state='disabled')
                        self.disabledall()
                        messagebox.showinfo("",f"Sale invoice No: ({saleBillNo})")

                    else:
                        messagebox.showinfo("","Cart is empty")
                else:
                    messagebox.showinfo("","Invalid adhar number")    
            else:
                messagebox.showinfo("","Invalid mobile number")
        #-----------------------------------------------------------------------------------------------------------             
        elif paytype == "credit":
            if customername.strip() and customermono.strip() and customeraddress.strip() and customeradhar.strip():
                if valid_phone(customermono):
                    if valid_adhar(customeradhar):
                        if allData:
                            # messagebox.showinfo("",f"Id - {customerid}\nname - {customername}\nMobile no - {customermono}\naddress - {customeraddress}\nAdhar no - {customeradhar}")
                            if dis == '':
                                dis = 0
                            if charge == '':
                                charge = 0
                            if roundoff == '':
                                roundoff = 0
                            netTotal = (float(charge) + float(roundoff) + float(total)) - float(dis)
                            for item in allData:
                                data = self.tree.item(item, "values")
                                self.cursor.execute("select saleqty,availableqty from purchase where entrydescription = %s and purchasedcid = %s",[data[9],data[11]])
                                oldQty = self.cursor.fetchall()
                                self.cursor.execute("update purchase set saleqty = %s, availableqty = %s where entrydescription = %s and purchasedcid = %s",[(float(oldQty[0][0]) + float(data[3])),(float(oldQty[0][1]) - float(data[3])),data[9],data[11]])
                                insertQuery = "insert into sale(srno,entryno,entrydate,customername,customerid,customermobileno,customeraddress,customeradharno,paytype,note,productname,batch_lot,expiry,quantity,sellingprice,taxableamt,gstrate,gstamt,amount,description,productno,purchasedcid,costprice,totalqty,discount,charge,roundoff,total,nettotal,status,returnqty,avforreturnqty) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                self.cursor.execute(insertQuery,[None,saleBillNo,entrydate,customername,customerid,customermono,customeraddress,customeradhar,paytype,note,data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],totalqty,dis,charge,roundoff,total,netTotal,"active",0,data[3]])        
                                self.mydb.commit()
                                
                            self.cursor.execute("select credit from customer where customerid = %s and customername = %s",[customerid,customername])
                            oldCredit = self.cursor.fetchall()
                            self.cursor.execute("update customer set credit = %s where customerid = %s and customername = %s",[(float(oldCredit[0][0]) + float(netTotal)),customerid,customername])
                            self.mydb.commit()
                            self.netTotal.configure(state='normal')
                            self.entryNo.configure(state='normal')
                            self.netTotal.delete(0,END)
                            self.entryNo.delete(0,END)
                            self.netTotal.insert(0,netTotal)
                            self.entryNo.insert(0,saleBillNo)
                            self.netTotal.configure(state='disabled')
                            self.entryNo.configure(state='disabled')
                            self.disabledall()
                            messagebox.showinfo("",f"Sale invoice No: ({saleBillNo})")

                        else:
                            messagebox.showinfo("","Cart is empty")
                    else:
                        messagebox.showinfo("","Invalid adhar number")    
                else:
                    messagebox.showinfo("","Invalid mobile number")
            else:
                messagebox.showinfo("","Enter customer's all details")
        #-----------------------------------------------------------------------------------------------------------
        else:
            messagebox.showinfo("","Is Bill Cash or Credit")
           
    def addToCart(self):
        productname = self.productName.get()
        code = self.code.get()
        lno = self.lotNo.get()
        exp = self.expDate.get()
        qty = self.quantity.get()
        rate = self.rate.get()
        amt = self.amount.get()
        crate = self.cRate.get()
        gst = self.gst.get()
        gstrate = self.gstRate.get()
        totqty = self.qtytot.get()
        taxamt = self.taxAmount.get()
        totamt = self.total.get()
        alldata = self.tree.get_children()
        flag = True
        if alldata:
            for item in alldata: # This loop is for checking where entered item is exist or not.
                data = self.tree.item(item, "values")
                if productname in data:
                    messagebox.showinfo("","This Item already exist in cart")
                    flag = False
                    self.clear()
                    self.num = ""
                    self.numqty = ""
                    break
                else:
                    flag = True
            if flag:
                self.cursor.execute("select availableqty,productname,productno from purchase where entrydescription = %s and purchasedcid = %s",[productname,code])
                pData = self.cursor.fetchall()
                if productname.strip() and qty.strip() and rate.strip():
                    result = float(pData[0][0]) - float(qty)
                    if result >= 0:
                        data = (pData[0][1],lno,exp,qty,rate,amt,gst,gstrate,taxamt,productname,pData[0][2],code,crate)
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
                        self.numqty = ""
                    else:
                        messagebox.showinfo("",f"This transaction can not be doen\nbeacuse available quantity is {pData[0][0]} for sale.")
                        self.clear()
                        self.num = ""
                        self.numqty = ""
        else:
            self.cursor.execute("select availableqty,productname,productno from purchase where entrydescription = %s and purchasedcid = %s",[productname,code])
            pData = self.cursor.fetchall()
            if productname.strip() and qty.strip() and rate.strip():
                result = float(pData[0][0]) - float(qty)
                if result >= 0:
                    data = (pData[0][1],lno,exp,qty,rate,amt,gst,gstrate,taxamt,productname,pData[0][2],code,crate)
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
                    self.numqty = ""
                else:
                    messagebox.showinfo("",f"This transaction can not be doen\nbeacuse available quantity is {pData[0][0]} for sale.")
                    self.clear()
                    self.num = ""
                    self.numqty = ""
        self.discount.configure(state='normal')
        self.charge.configure(state='normal')
        self.roundOff.configure(state='normal')
 
    def onTreeSelect(self,event):
        selected_item = self.tree.focus()
        if selected_item:
            self.clear()
            data = self.tree.item(selected_item, "values")
            self.lotNo.configure(state='normal')
            self.expDate.configure(state='normal')
            self.quantity.configure(state='normal')
            self.rate.configure(state='normal')
            self.amount.configure(state='normal')
            self.gst.configure(state='normal')
            self.gstRate.configure(state='normal')
            self.taxAmount.configure(state='normal')
            self.productName.configure(state='normal')
            self.code.configure(state='normal')
            self.cRate.configure(state='normal')
            
            self.lotNo.delete(0,END)
            self.expDate.delete(0,END)
            self.quantity.delete(0,END)
            self.rate.delete(0,END)
            self.amount.delete(0,END)
            self.gst.delete(0,END)
            self.gstRate.delete(0,END)
            self.taxAmount.delete(0,END)
            self.productName.delete(0,END)
            self.code.delete(0,END)
            self.cRate.delete(0,END)
            
            self.lotNo.insert(0,data[1])
            self.expDate.insert(0,data[2])
            self.quantity.insert(0,data[3])
            self.rate.insert(0,data[4])
            self.amount.insert(0,data[5])
            self.gst.insert(0,data[6])
            self.gstRate.insert(0,data[7])
            self.taxAmount.insert(0,data[8])
            self.productName.insert(0,data[9])
            self.code.insert(0,data[11])
            self.cRate.insert(0,data[12])

            self.lotNo.configure(state='disabled')
            self.expDate.configure(state='disabled')
            self.quantity.configure(state='disabled')
            self.rate.configure(state='disabled')
            self.amount.configure(state='disabled')
            self.gst.configure(state='disabled')
            self.gstRate.configure(state='disabled')
            self.taxAmount.configure(state='disabled')
            self.code.configure(state='disabled')
            self.cRate.configure(state='disabled')
            self.productName.configure(state='disabled')

            self.addButton.configure(state='disabled')
            self.addBillButton.configure(state='disabled')
    
    def newBill(self):
        self.clear()
        self.tree.delete(*self.tree.get_children())
        self.entryNo.configure(state='normal')
        self.customerName.configure(state='normal')
        self.customerId.configure(state='normal')
        self.customerLocation.configure(state='normal')
        self.customerMoNo.configure(state='normal')
        self.customerAdhar.configure(state='normal')
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
        self.addBillButton.configure(state='normal')
        self.qtytot.configure(state='normal')
        self.discount.configure(state='normal')
        self.charge.configure(state='normal')
        self.roundOff.configure(state='normal')
        self.total.configure(state='normal')
        self.netTotal.configure(state='normal')
        self.clearButton.configure(state='normal')

        self.entryNo.delete(0,END)
        self.customerName.delete(0,END)
        self.customerId.delete(0,END)
        self.customerLocation.delete(0,END)
        self.customerMoNo.delete(0,END)
        self.customerAdhar.delete(0,END)
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
        self.customerId.configure(state='disabled')
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
        self.printBillButton.configure(state='disabled')
              
    def open(self):
        self.entryNo.configure(state='normal')
        self.customerLocation.configure(state='normal')
        self.customerId.configure(state='normal')
        self.productName.configure(state='normal')
        self.customerAdhar.configure(state='normal')
        self.customerMoNo.configure(state='normal')
        self.note.configure(state='normal')
        self.customerName.configure(state='normal')
        self.expDate.configure(state='normal')
        self.lotNo.configure(state='normal')
        self.quantity.configure(state='normal')
        self.rate.configure(state='normal')
        self.amount.configure(state='normal')
        self.gst.configure(state='normal')
        self.taxAmount.configure(state='normal')
        self.code.configure(state='normal')
        self.availableqty.configure(state='normal')
        self.gstRate.configure(state='normal')
        self.qtytot.configure(state='normal')
        self.total.configure(state='normal')
        self.netTotal.configure(state='normal')
        self.addButton.configure(state='normal')
        self.cRate.configure(state='normal')
        self.changeButton.configure(state='normal')
        self.modifyButton.configure(state='normal')
        self.removeButton.configure(state='normal')
        self.addBillButton.configure(state='normal')
        self.discount.configure(state='normal')
        self.charge.configure(state='normal')
        self.roundOff.configure(state='normal')
        self.printBillButton.configure(state='normal')
        self.clearButton.configure(state='normal')
      
    def close(self):
        self.entryNo.configure(state='disabled')
        self.customerLocation.configure(state='disabled')
        self.customerId.configure(state='disabled')
        self.productName.configure(state='disabled')
        self.customerAdhar.configure(state='disabled')
        self.customerMoNo.configure(state='disabled')
        self.note.configure(state='disabled')
        self.customerName.configure(state='disabled')
        self.expDate.configure(state='disabled')
        self.lotNo.configure(state='disabled')
        self.quantity.configure(state='disabled')
        self.rate.configure(state='disabled')
        self.amount.configure(state='disabled')
        self.gst.configure(state='disabled')
        self.taxAmount.configure(state='disabled')
        self.code.configure(state='disabled')
        self.availableqty.configure(state='disabled')
        self.gstRate.configure(state='disabled')
        self.qtytot.configure(state='disabled')
        self.total.configure(state='disabled')
        self.netTotal.configure(state='disabled')
        self.addButton.configure(state='disabled')
        self.cRate.configure(state='disabled')
        self.changeButton.configure(state='disabled')
        self.modifyButton.configure(state='disabled')
        self.removeButton.configure(state='disabled')
        self.addBillButton.configure(state='disabled')
        self.discount.configure(state='disabled')
        self.charge.configure(state='disabled')
        self.roundOff.configure(state='disabled')
        self.printBillButton.configure(state='disabled')
        self.clearButton.configure(state='disabled')
    
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