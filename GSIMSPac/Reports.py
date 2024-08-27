# ==================( IMPORT )==================
from tkinter import *
import re
import string
import mysql.connector
import random
import psutil
from datetime import date, timedelta, datetime
from tkinter import ttk
from GSIMSPac import fun
from GSIMSPac import Product
from GSIMSPac import Partys
from GSIMSPac import PurchaseDC
from GSIMSPac import PurchaseInvoice
# from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
# ===============================================

class ItemWiseReport:
    def __init__(self,canvas_widget):

        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        self.cursor = self.mydb.cursor()

        f1 = ("Times", 11)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 13)
        f4 = ("Arial Black", 11)
        f5 = ("Arial Black", 10)

        current_year = datetime.now().year
        fromDate = str(current_year) + "-01-01"
        toDate = str(current_year) + "-12-31"
        
        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.1,rely=0.165)
        self.root.configure(width=1200,height=610)
        self.root.configure(bg="#ad995e")

        self.fromDateLabel = Label(self.root)
        self.fromDateLabel.place(relx=0.1,rely=0.025)
        self.fromDateLabel.configure(text="From")
        self.fromDateLabel.configure(bg="#ad995e")
        self.fromDateLabel.configure(fg="#6e5a20")
        self.fromDateLabel.configure(font=f3)
        self.fromDate = DateEntry(self.root)
        self.fromDate.place(relx=0.15,rely=0.025)
        self.fromDate.configure(background='#6e5a20', foreground='#ad995e')
        self.fromDate.configure(width=10)
        
        self.toDateLabel = Label(self.root)
        self.toDateLabel.place(relx=0.265,rely=0.025)
        self.toDateLabel.configure(text="To")
        self.toDateLabel.configure(bg="#ad995e")
        self.toDateLabel.configure(fg="#6e5a20")
        self.toDateLabel.configure(font=f3)
        self.toDate = DateEntry(self.root)
        self.toDate.place(relx=0.295,rely=0.025)
        self.toDate.configure(background='#6e5a20', foreground='#ad995e')
        self.toDate.configure(width=10)

        try:
            selectedFromdate = datetime.strptime(fromDate, "%Y-%m-%d")
            selectedTOdate = datetime.strptime(toDate, "%Y-%m-%d")
            self.fromDate.set_date(selectedFromdate)
            self.toDate.set_date(selectedTOdate)
        except ValueError:
            print("Invalid format of Expiry date")

        self.showReportButton = Button(self.root)
        self.showReportButton.place(relx=0.43,rely=0.026)
        self.showReportButton.configure(text="Show")
        self.showReportButton.configure(font=f1)
        self.showReportButton.configure(width=12)
        self.showReportButton.configure(activebackground="#ad995e")
        self.showReportButton.configure(bg="#e0cb8d")
        self.showReportButton.configure(command=self.addTreeData)

        self.productNoLabel = Label(self.root)
        self.productNoLabel.place(relx=0.1, rely=0.09)
        self.productNoLabel.configure(text="Product No:")
        self.productNoLabel.configure(bg="#ad995e")
        self.productNoLabel.configure(fg="#6e5a20")
        self.productNoLabel.configure(font=f3)
        self.productNo = Entry(self.root)
        self.productNo.place(relx=0.1,rely=0.135)
        self.productNo.configure(width=12)
        self.productNo.configure(bg="#e5e6d5")
        self.productNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.productTypeLabel = Label(self.root)
        self.productTypeLabel.place(relx=0.33, rely=0.09)
        self.productTypeLabel.configure(text="Product Category:")
        self.productTypeLabel.configure(bg="#ad995e")
        self.productTypeLabel.configure(fg="#6e5a20")
        self.productTypeLabel.configure(font=f3)
        self.productType = ttk.Combobox(self.root)  
        self.productType.place(relx=0.33, rely=0.135) 
        self.productType['values'] = ('All','Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.productType.current(0)
        self.productType.configure(state='readonly')
        self.productType.configure(width=20)
        self.productType.configure(font=f2)
        self.productType.bind("<<ComboboxSelected>>",self.addTreeData)

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.08, rely=0.2, width=1000, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.915, rely=0.20, width=18, height=395)

        self.reportTree = ttk.Treeview(self.root)
        self.reportTree.place(relx=0.08, rely=0.23, width=1000, height=380)
        self.reportTree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.reportTree.xview)
        self.scrollbary.configure(command=self.reportTree.yview)
        
        self.reportTree.configure(
            columns=(
                "Item no",
                "Item Name",
                "Opening Qty",
                "Purchase Qty",
                "Purchase[R] Qty",
                "Sale Qty",
                "Sale[R] Qty",
                "Stock Qty"
            )
        )

        self.reportTree.heading("Item no", text="Item no", anchor=W)
        self.reportTree.heading("Item Name", text="Item Name", anchor=W)
        self.reportTree.heading("Opening Qty", text="Opening Qty", anchor=W)
        self.reportTree.heading("Purchase Qty", text="Purchase Qty", anchor=W)
        self.reportTree.heading("Purchase[R] Qty", text="Purchase[R] Qty", anchor=W)
        self.reportTree.heading("Sale Qty", text="Sale Qty", anchor=W)
        self.reportTree.heading("Sale[R] Qty", text="Sale[R] Qty", anchor=W)
        self.reportTree.heading("Stock Qty", text="Stock Qty", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=200)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=135)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=112)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#8", stretch=NO, minwidth=0, width=119)
        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeData()
        # self.reportTree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        # self.reportTree.bind("<Double-1>", self.showPartyData)
        
    def addTreeData(self,event = "1"): 

        self.reportTree.delete(*self.reportTree.get_children())
        if self.productType.get() == "All":
            self.cursor.execute("select product_id,product_description from product where status = %s",["active"])
        else:
            self.cursor.execute("select product_id,product_description from product where product_category = %s and status = %s",[self.productType.get(),"active"])

        products = self.cursor.fetchall()
        for product in products:
            pQty = 0.0
            pRQty = 0.0
            sQty = 0.0
            sRQty = 0.0
            stQty = 0.0
            openingQty = 0.0
            productId = product[0]
            
            self.cursor.execute("select availableqty from purchase where (status = %s or status = %s) and productno = %s and purchasedcdate < %s",["dc","inv",productId,self.fromDate.get_date()])
            opening = self.cursor.fetchall()
            for rowdata in opening:
                openingQty = float(openingQty) + float(rowdata[0])
            
            self.cursor.execute("select quantity,returnqty,saleqty,salereturnqty,availableqty,purchasedcdate,productname from purchase where (status = %s or status = %s) and productno = %s and purchasedcdate >= %s and purchasedcdate <= %s",["dc","inv",productId,self.fromDate.get_date(),self.toDate.get_date()])
            productRowData = self.cursor.fetchall()
            for data in productRowData:
                pQty = float(pQty) + float(data[0])
                pRQty = float(pRQty) + float(data[1])
                sQty = float(sQty) + float(data[2])
                sRQty = float(sRQty) + float(data[3])
                stQty = float(stQty) + float(data[4])
            # if productRowData:
            listItem = [product[0], product[1], openingQty, pQty, pRQty, sQty, sRQty, (stQty + openingQty)] 
            self.reportTree.insert("", "end", values=listItem,tags=("item",))
            self.mydb.commit()

class ExpWiseReport:
    def __init__(self,canvas_widget):

        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        self.cursor = self.mydb.cursor()

        f1 = ("Times", 11)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 13)
        f4 = ("Arial Black", 11)
        f5 = ("Arial Black", 10)
        
        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.1,rely=0.165)
        self.root.configure(width=1200,height=610)
        self.root.configure(bg="#ad995e")

        self.fromDateLabel = Label(self.root)
        self.fromDateLabel.place(relx=0.1,rely=0.025)
        self.fromDateLabel.configure(text="Date:")
        self.fromDateLabel.configure(bg="#ad995e")
        self.fromDateLabel.configure(fg="#6e5a20")
        self.fromDateLabel.configure(font=f3)
        self.isDate = DateEntry(self.root)
        self.isDate.place(relx=0.15,rely=0.025)
        self.isDate.configure(background='#6e5a20', foreground='#ad995e')
        self.isDate.configure(width=10)
        
        self.showReportButton = Button(self.root)
        self.showReportButton.place(relx=0.27,rely=0.026)
        self.showReportButton.configure(text="Show")
        self.showReportButton.configure(font=f1)
        self.showReportButton.configure(width=12)
        self.showReportButton.configure(activebackground="#ad995e")
        self.showReportButton.configure(bg="#e0cb8d")
        self.showReportButton.configure(command=self.addTreeDataOfExp)
        
        self.dataType = ttk.Combobox(self.root)  
        self.dataType.place(relx=0.38, rely=0.026) 
        self.dataType['values'] = ('Expired','Comming soon')
        self.dataType.current(0)
        self.dataType.configure(state='readonly')
        self.dataType.configure(width=14)
        self.dataType.configure(font=f2)
        self.dataType.bind("<<ComboboxSelected>>",self.addTreeDataOfExp)

        self.productNoLabel = Label(self.root)
        self.productNoLabel.place(relx=0.1, rely=0.09)
        self.productNoLabel.configure(text="Product No:")
        self.productNoLabel.configure(bg="#ad995e")
        self.productNoLabel.configure(fg="#6e5a20")
        self.productNoLabel.configure(font=f3)
        self.productNo = Entry(self.root)
        self.productNo.place(relx=0.1,rely=0.135)
        self.productNo.configure(width=12)
        self.productNo.configure(bg="#e5e6d5")
        self.productNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.productTypeLabel = Label(self.root)
        self.productTypeLabel.place(relx=0.33, rely=0.09)
        self.productTypeLabel.configure(text="Product Category:")
        self.productTypeLabel.configure(bg="#ad995e")
        self.productTypeLabel.configure(fg="#6e5a20")
        self.productTypeLabel.configure(font=f3)
        self.productType = ttk.Combobox(self.root)  
        self.productType.place(relx=0.33, rely=0.135) 
        self.productType['values'] = ('All','Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.productType.current(0)
        self.productType.configure(state='readonly')
        self.productType.configure(width=20)
        self.productType.configure(font=f2)
        self.productType.bind("<<ComboboxSelected>>",self.addTreeDataOfExp)

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.08, rely=0.2, width=1000, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.915, rely=0.20, width=18, height=395)

        self.reportTree = ttk.Treeview(self.root)
        self.reportTree.place(relx=0.08, rely=0.23, width=1000, height=380)
        self.reportTree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.reportTree.xview)
        self.scrollbary.configure(command=self.reportTree.yview)
        # self.reportTree.configure()
        
        self.reportTree.configure(
            columns=(
                "Item no",
                "Item Name",
                "Exp Date",
                "Purchase Qty",
                "Purchase[R] Qty",
                "Sale Qty",
                "Sale[R] Qty",
                "Stock Qty",
                "DC Number",
                "Purchase No"
            )
        )

        self.reportTree.heading("Item no", text="Item no", anchor=W)
        self.reportTree.heading("Item Name", text="Item Name", anchor=W)
        self.reportTree.heading("Exp Date", text="Exp Date", anchor=W)
        self.reportTree.heading("Purchase Qty", text="Purchase Qty", anchor=W)
        self.reportTree.heading("Purchase[R] Qty", text="Purchase[R] Qty", anchor=W)
        self.reportTree.heading("Sale Qty", text="Sale Qty", anchor=W)
        self.reportTree.heading("Sale[R] Qty", text="Sale[R] Qty", anchor=W)
        self.reportTree.heading("Stock Qty", text="Stock Qty", anchor=W)
        self.reportTree.heading("DC Number", text="DC Number", anchor=W)
        self.reportTree.heading("Purchase No", text="Purchase No", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=200)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=135)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=112)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#8", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#9", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#10", stretch=NO, minwidth=0, width=119)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeDataOfExp()
        self.reportTree.bind("<Double-1>", self.itemDetail)
        self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        
    def itemDetail(self,event):
        # messagebox.showinfo("","ok sir")

        f1 = ("Times", 11)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 11)
        f4 = ("Arial Black", 11)
        f5 = ("Arial Black", 10)

        self.dataroot = Canvas(self.root)
        self.dataroot.place(relx=0.13,rely=0.05)
        self.dataroot.configure(width=900,height=500)
        self.dataroot.configure(bg="#c9b577")
        
        self.closeButton = Button(self.dataroot)
        self.closeButton.place(relx = 0.958, rely=0.02)
        self.closeButton.configure(text="❌", font=("arial", 10))
        # self.closeButton.configure(bg="#ad995e", activebackground="#63412c", fg="#fce89d", activeforeground="#fce89d")
        self.closeButton.configure(bg="#ad995e", activebackground="#63412c", fg="black", activeforeground="#fce89d")
        self.closeButton.configure(command=self.closeproductreport)
        
        self.dcEntryNumberLabel = Label(self.dataroot)
        self.dcEntryNumberLabel.place(relx=0.05,rely=0.1)
        self.dcEntryNumberLabel.configure(text="DC Entry No")
        self.dcEntryNumberLabel.configure(bg="#c9b577")
        self.dcEntryNumberLabel.configure(fg="#6e5a20")
        self.dcEntryNumberLabel.configure(font=f3)
        self.dcEntryNumber = Entry(self.dataroot)
        self.dcEntryNumber.place(relx=0.05,rely=0.15)
        self.dcEntryNumber.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.dcEntryNumber.configure(width=11)
        self.dcEntryNumber.configure(bg="#e5e6d5")
        self.dcEntryNumber.configure(font=f2)
        
        self.dcNumberLabel = Label(self.dataroot)
        self.dcNumberLabel.place(relx=0.227,rely=0.1)
        self.dcNumberLabel.configure(text="DC No")
        self.dcNumberLabel.configure(bg="#c9b577")
        self.dcNumberLabel.configure(fg="#6e5a20")
        self.dcNumberLabel.configure(font=f3)
        self.dcNumber = Entry(self.dataroot)
        self.dcNumber.place(relx=0.227,rely=0.15)
        self.dcNumber.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.dcNumber.configure(width=11)
        self.dcNumber.configure(bg="#e5e6d5")
        self.dcNumber.configure(font=f2)
        
        self.invEntryNumberLabel = Label(self.dataroot)
        self.invEntryNumberLabel.place(relx=0.42,rely=0.1)
        self.invEntryNumberLabel.configure(text="Pur Date")
        self.invEntryNumberLabel.configure(bg="#c9b577")
        self.invEntryNumberLabel.configure(fg="#6e5a20")
        self.invEntryNumberLabel.configure(font=f3)
        self.invEntryNumber = Entry(self.dataroot)
        self.invEntryNumber.place(relx=0.42,rely=0.15)
        self.invEntryNumber.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.invEntryNumber.configure(width=11)
        self.invEntryNumber.configure(bg="#e5e6d5")
        self.invEntryNumber.configure(font=f2)

        self.invNumberLabel = Label(self.dataroot)
        self.invNumberLabel.place(relx=0.62,rely=0.1)
        self.invNumberLabel.configure(text="Pur Date")
        self.invNumberLabel.configure(bg="#c9b577")
        self.invNumberLabel.configure(fg="#6e5a20")
        self.invNumberLabel.configure(font=f3)
        self.invNumber = Entry(self.dataroot)
        self.invNumber.place(relx=0.62,rely=0.15)
        self.invNumber.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.invNumber.configure(width=11)
        self.invNumber.configure(bg="#e5e6d5")
        self.invNumber.configure(font=f2)

        self.purchaseDateLabel = Label(self.dataroot)
        self.purchaseDateLabel.place(relx=0.82,rely=0.1)
        self.purchaseDateLabel.configure(text="Pur Date")
        self.purchaseDateLabel.configure(bg="#c9b577")
        self.purchaseDateLabel.configure(fg="#6e5a20")
        self.purchaseDateLabel.configure(font=f3)
        self.purchaseDate = Entry(self.dataroot)
        self.purchaseDate.place(relx=0.82,rely=0.15)
        self.purchaseDate.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.purchaseDate.configure(width=11)
        self.purchaseDate.configure(bg="#e5e6d5")
        self.purchaseDate.configure(font=f2)

        
        self.supplierIdLabel = Label(self.dataroot)
        self.supplierIdLabel.place(relx=0.05,rely=0.25)
        self.supplierIdLabel.configure(text="Supplier ID")
        self.supplierIdLabel.configure(bg="#c9b577")
        self.supplierIdLabel.configure(fg="#6e5a20")
        self.supplierIdLabel.configure(font=f3)
        self.supplierId = Entry(self.dataroot)
        self.supplierId.place(relx=0.05,rely=0.3)
        self.supplierId.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.supplierId.configure(width=11)
        self.supplierId.configure(bg="#e5e6d5")
        self.supplierId.configure(font=f2)
           
        self.supplierNameLabel = Label(self.dataroot)
        self.supplierNameLabel.place(relx=0.227,rely=0.25)
        self.supplierNameLabel.configure(text="Supplier Name")
        self.supplierNameLabel.configure(bg="#c9b577")
        self.supplierNameLabel.configure(fg="#6e5a20")
        self.supplierNameLabel.configure(font=f3)
        self.supplierName = Entry(self.dataroot)
        self.supplierName.place(relx=0.227,rely=0.3)
        self.supplierName.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.supplierName.configure(width=28)
        self.supplierName.configure(bg="#e5e6d5")
        self.supplierName.configure(font=f2)
        
        self.supplierAddressLabel = Label(self.dataroot)
        self.supplierAddressLabel.place(relx=0.62,rely=0.25)
        self.supplierAddressLabel.configure(text="Supplier Address")
        self.supplierAddressLabel.configure(bg="#c9b577")
        self.supplierAddressLabel.configure(fg="#6e5a20")
        self.supplierAddressLabel.configure(font=f3)
        self.supplierAddress = Entry(self.dataroot)
        self.supplierAddress.place(relx=0.62,rely=0.3)
        self.supplierAddress.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.supplierAddress.configure(width=28)
        self.supplierAddress.configure(bg="#e5e6d5")
        self.supplierAddress.configure(font=f2)


        self.productCanvas = Canvas(self.dataroot)
        self.productCanvas.place(relx=0.05,rely=0.4)
        self.productCanvas.configure(width=800,height=250)
        self.productCanvas.configure(bg="#ad995e")

        self.productNameLabel = Label(self.productCanvas)
        self.productNameLabel.place(relx=0.05,rely=0.05)
        self.productNameLabel.configure(text="Product Name")
        self.productNameLabel.configure(bg="#ad995e")
        self.productNameLabel.configure(fg="#6e5a20")
        self.productNameLabel.configure(font=f3)
        self.productName = Entry(self.productCanvas)
        self.productName.place(relx=0.05,rely=0.15)
        self.productName.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.productName.configure(width=20)
        self.productName.configure(bg="#e5e6d5")
        self.productName.configure(font=f2)

        self.productNoLabel = Label(self.productCanvas)
        self.productNoLabel.place(relx=0.38,rely=0.05)
        self.productNoLabel.configure(text="P No")
        self.productNoLabel.configure(bg="#ad995e")
        self.productNoLabel.configure(fg="#6e5a20")
        self.productNoLabel.configure(font=f3)
        self.productNo = Entry(self.productCanvas)
        self.productNo.place(relx=0.38,rely=0.15)
        self.productNo.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.productNo.configure(width=8)
        self.productNo.configure(bg="#e5e6d5")
        self.productNo.configure(font=f2)

        self.lotNoLabel = Label(self.productCanvas)
        self.lotNoLabel.place(relx=0.56,rely=0.05)
        self.lotNoLabel.configure(text="Batch No")
        self.lotNoLabel.configure(bg="#ad995e")
        self.lotNoLabel.configure(fg="#6e5a20")
        self.lotNoLabel.configure(font=f3)
        self.lotNo = Entry(self.productCanvas)
        self.lotNo.place(relx=0.56,rely=0.15)
        self.lotNo.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.lotNo.configure(width=12)
        self.lotNo.configure(bg="#e5e6d5")
        self.lotNo.configure(font=f2)

        self.expiryLabel = Label(self.productCanvas)
        self.expiryLabel.place(relx=0.8,rely=0.05)
        self.expiryLabel.configure(text="Expiry")
        self.expiryLabel.configure(bg="#ad995e")
        self.expiryLabel.configure(fg="#6e5a20")
        self.expiryLabel.configure(font=f3)
        self.expiry = Entry(self.productCanvas)
        self.expiry.place(relx=0.8,rely=0.15)
        self.expiry.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.expiry.configure(width=12)
        self.expiry.configure(bg="#e5e6d5")
        self.expiry.configure(font=f2)

        self.purchaseqtyLabel = Label(self.productCanvas)
        self.purchaseqtyLabel.place(relx=0.1,rely=0.3)
        self.purchaseqtyLabel.configure(text="Purchase Qty")
        self.purchaseqtyLabel.configure(bg="#ad995e")
        self.purchaseqtyLabel.configure(fg="#6e5a20")
        self.purchaseqtyLabel.configure(font=f3)
        self.purchaseqty = Entry(self.productCanvas)
        self.purchaseqty.place(relx=0.1,rely=0.4)
        self.purchaseqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.purchaseqty.configure(width=12)
        self.purchaseqty.configure(bg="#e5e6d5")
        self.purchaseqty.configure(font=f2)

        self.purchaseRqtyLabel = Label(self.productCanvas)
        self.purchaseRqtyLabel.place(relx=0.3,rely=0.3)
        self.purchaseRqtyLabel.configure(text="Purchase[R] Qty")
        self.purchaseRqtyLabel.configure(bg="#ad995e")
        self.purchaseRqtyLabel.configure(fg="#6e5a20")
        self.purchaseRqtyLabel.configure(font=f3)
        self.purchaseRqty = Entry(self.productCanvas)
        self.purchaseRqty.place(relx=0.3,rely=0.4)
        self.purchaseRqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.purchaseRqty.configure(width=12)
        self.purchaseRqty.configure(bg="#e5e6d5")
        self.purchaseRqty.configure(font=f2)

        self.saleqtyLabel = Label(self.productCanvas)
        self.saleqtyLabel.place(relx=0.1,rely=0.55)
        self.saleqtyLabel.configure(text="Sale Qty")
        self.saleqtyLabel.configure(bg="#ad995e")
        self.saleqtyLabel.configure(fg="#6e5a20")
        self.saleqtyLabel.configure(font=f3)
        self.saleqty = Entry(self.productCanvas)
        self.saleqty.place(relx=0.1,rely=0.65)
        self.saleqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.saleqty.configure(width=12)
        self.saleqty.configure(bg="#e5e6d5")
        self.saleqty.configure(font=f2)

        self.saleRqtyLabel = Label(self.productCanvas)
        self.saleRqtyLabel.place(relx=0.3,rely=0.55)
        self.saleRqtyLabel.configure(text="Sale[R] Qty")
        self.saleRqtyLabel.configure(bg="#ad995e")
        self.saleRqtyLabel.configure(fg="#6e5a20")
        self.saleRqtyLabel.configure(font=f3)
        self.saleRqty = Entry(self.productCanvas)
        self.saleRqty.place(relx=0.3,rely=0.65)
        self.saleRqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.saleRqty.configure(width=12)
        self.saleRqty.configure(bg="#e5e6d5")
        self.saleRqty.configure(font=f2)

        self.stockqtyLabel = Label(self.productCanvas)
        self.stockqtyLabel.place(relx=0.56,rely=0.425)
        self.stockqtyLabel.configure(text="Stock Qty")
        self.stockqtyLabel.configure(bg="#ad995e")
        self.stockqtyLabel.configure(fg="#6e5a20")
        self.stockqtyLabel.configure(font=f3)
        self.stockqty = Entry(self.productCanvas)
        self.stockqty.place(relx=0.56,rely=0.525)
        self.stockqty.configure(state="disabled",disabledbackground="#fce89d",disabledforeground="black")
        self.stockqty.configure(width=12)
        self.stockqty.configure(bg="#e5e6d5")
        self.stockqty.configure(font=f2)

        selected_item = self.reportTree.focus()
        if selected_item:
            data = self.reportTree.item(selected_item, "values")
            self.cursor.execute("select * from purchase where purchasedcid = %s and productname = %s",[data[8],data[1]])
            messagebox.showinfo("",f"{self.cursor.fetchall()}")

    def onSingleclick(self,event):
        selected_item = self.reportTree.focus()
        if selected_item:
            data = self.reportTree.item(selected_item, "values")
            self.cursor.execute("select billno, purchasedcid from purchase where purchasedcid = %s and productname = %s",[data[8],data[1]])
            d = self.cursor.fetchall()
            messagebox.showinfo("",f"Purchase Bill No: {d[0][0]}\nPurchase DC ID: {d[0][1]}")

    def closeproductreport(self):
        for widget in self.dataroot.winfo_children():
            widget.destroy()
        self.dataroot.destroy()

    def addTreeDataOfExp(self,event = "1"): 
        currentDate = self.isDate.get_date()
        self.reportTree.delete(*self.reportTree.get_children())
        if self.dataType.get() == "Expired":
            self.cursor.execute("select productno,productname,expiry,quantity,returnqty,saleqty,salereturnqty,availableqty,purchasedcid,purchaseid from purchase where (status = %s or status = %s) and availableqty > %s",["inv", "dc", 0])
            rowData = self.cursor.fetchall()
            for data in rowData:
                if data[2] != "None":
                    date_obj = datetime.strptime(data[2], "%Y-%m-%d").date()
                    if date_obj <= currentDate:                    
                        listItem = [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]] 
                        self.reportTree.insert("", "end", values=listItem,tags=("item",))
        else:
            start_date = self.isDate.get_date()
            endDate = start_date + timedelta(days=60)
            for delta in range((endDate - start_date).days + 1):
                current = start_date + timedelta(days=delta)
                current_date = datetime.strptime(str(current), "%Y-%m-%d")
                date = current_date.strftime("%Y-%m-%d")
                self.cursor.execute("select productno,productname,expiry,quantity,returnqty,saleqty,salereturnqty,availableqty,purchasedcid,purchaseid from purchase where (status = %s or status = %s) and availableqty > %s and expiry = %s",["inv", "dc", 0, str(date)])
                tabledata = self.cursor.fetchall()
                if tabledata:
                    for row in tabledata:
                        listItem = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]] 
                        self.reportTree.insert("", "end", values=listItem,tags=("item",))
        

