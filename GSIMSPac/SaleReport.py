# ==================( IMPORT )==================
import calendar
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

class SaleReport:
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
        self.showReportButton.configure(command=self.addTreeDataOfSale)

        self.EntryNoLabel = Label(self.root)
        self.EntryNoLabel.place(relx=0.1, rely=0.09)
        self.EntryNoLabel.configure(text="Entry No:")
        self.EntryNoLabel.configure(bg="#ad995e")
        self.EntryNoLabel.configure(fg="#6e5a20")
        self.EntryNoLabel.configure(font=f3)
        self.EntryNo = Entry(self.root)
        self.EntryNo.place(relx=0.1,rely=0.135)
        self.EntryNo.configure(width=12)
        self.EntryNo.configure(bg="#e5e6d5")
        self.EntryNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.billTypeLabel = Label(self.root)
        self.billTypeLabel.place(relx=0.33, rely=0.09)
        self.billTypeLabel.configure(text="Bill Type:")
        self.billTypeLabel.configure(bg="#ad995e")
        self.billTypeLabel.configure(fg="#6e5a20")
        self.billTypeLabel.configure(font=f3)
        self.billType = ttk.Combobox(self.root)  
        self.billType.place(relx=0.33, rely=0.135) 
        self.billType['values'] = ('All','cash','credit')
        self.billType.current(0)
        self.billType.configure(state='readonly')
        self.billType.configure(width=20)
        self.billType.configure(font=f2)
        self.billType.bind("<<ComboboxSelected>>",self.addTreeDataOfSale)

        
        self.quantityLabel = Label(self.root)
        self.quantityLabel.place(relx=0.2, rely=0.85)
        self.quantityLabel.configure(text="Quantity:")
        self.quantityLabel.configure(bg="#ad995e")
        self.quantityLabel.configure(fg="#6e5a20")
        self.quantityLabel.configure(font=f3)
        self.quantity = Entry(self.root)
        self.quantity.place(relx=0.2,rely=0.9)
        self.quantity.configure(width=12)
        self.quantity.configure(bg="#e5e6d5")
        self.quantity.configure(font=f2)
        
        self.DiscountLabel = Label(self.root)
        self.DiscountLabel.place(relx=0.32, rely=0.85)
        self.DiscountLabel.configure(text="Discount:")
        self.DiscountLabel.configure(bg="#ad995e")
        self.DiscountLabel.configure(fg="#6e5a20")
        self.DiscountLabel.configure(font=f3)
        self.Discount = Entry(self.root)
        self.Discount.place(relx=0.32,rely=0.9)
        self.Discount.configure(width=12)
        self.Discount.configure(bg="#e5e6d5")
        self.Discount.configure(font=f2)
        
        self.ChargeLabel = Label(self.root)
        self.ChargeLabel.place(relx=0.44, rely=0.85)
        self.ChargeLabel.configure(text="Charge:")
        self.ChargeLabel.configure(bg="#ad995e")
        self.ChargeLabel.configure(fg="#6e5a20")
        self.ChargeLabel.configure(font=f3)
        self.Charge = Entry(self.root)
        self.Charge.place(relx=0.44,rely=0.9)
        self.Charge.configure(width=12)
        self.Charge.configure(bg="#e5e6d5")
        self.Charge.configure(font=f2)
        
        self.RoundOffLabel = Label(self.root)
        self.RoundOffLabel.place(relx=0.56, rely=0.85)
        self.RoundOffLabel.configure(text="Round Off:")
        self.RoundOffLabel.configure(bg="#ad995e")
        self.RoundOffLabel.configure(fg="#6e5a20")
        self.RoundOffLabel.configure(font=f3)
        self.RoundOff = Entry(self.root)
        self.RoundOff.place(relx=0.56,rely=0.9)
        self.RoundOff.configure(width=12)
        self.RoundOff.configure(bg="#e5e6d5")
        self.RoundOff.configure(font=f2)
        
        self.TotalLabel = Label(self.root)
        self.TotalLabel.place(relx=0.68, rely=0.85)
        self.TotalLabel.configure(text="Total:")
        self.TotalLabel.configure(bg="#ad995e")
        self.TotalLabel.configure(fg="#6e5a20")
        self.TotalLabel.configure(font=f3)
        self.Total = Entry(self.root)
        self.Total.place(relx=0.68,rely=0.9)
        self.Total.configure(width=12)
        self.Total.configure(bg="#e5e6d5")
        self.Total.configure(font=f2)
        
        self.NetTotalLabel = Label(self.root)
        self.NetTotalLabel.place(relx=0.80, rely=0.85)
        self.NetTotalLabel.configure(text="Net Total:")
        self.NetTotalLabel.configure(bg="#ad995e")
        self.NetTotalLabel.configure(fg="#6e5a20")
        self.NetTotalLabel.configure(font=f3)
        self.NetTotal = Entry(self.root)
        self.NetTotal.place(relx=0.80,rely=0.9)
        self.NetTotal.configure(width=12)
        self.NetTotal.configure(bg="#e5e6d5")
        self.NetTotal.configure(font=f2)

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
                "Inv No",
                "Inv Date",
                "Customer Name",
                "Custo Id",
                "Quantity Tot",
                "Discount",
                "Charge",
                "Rou off",
                "Total Amt",
                "Net Tot Amt",
                "Bill Type"
            )
        )

        self.reportTree.heading("Inv No", text="Inv No", anchor=W)
        self.reportTree.heading("Inv Date", text="Inv Date", anchor=W)
        self.reportTree.heading("Customer Name", text="Customer Name", anchor=W)
        self.reportTree.heading("Custo Id", text="Custo Id", anchor=W)
        self.reportTree.heading("Quantity Tot", text="Quantity Tot", anchor=W)
        self.reportTree.heading("Discount", text="Discount", anchor=W)
        self.reportTree.heading("Charge", text="Charge", anchor=W)
        self.reportTree.heading("Rou off", text="Rou off", anchor=W)
        self.reportTree.heading("Total Amt", text="Total Amt", anchor=W)
        self.reportTree.heading("Net Tot Amt", text="Net Tot Amt", anchor=W)
        self.reportTree.heading("Bill Type", text="Bill Type", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=200)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=135)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=112)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#8", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#9", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#10", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#11", stretch=NO, minwidth=0, width=119)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeDataOfSale()
        # self.reportTree.bind("<Double-1>", self.itemDetail)
        # self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        

    def addTreeDataOfSale(self,event = '1'):
        self.reportTree.delete(*self.reportTree.get_children())
        date = self.isDate.get_date()
        tqty = 0
        tntot = 0
        dits = 0
        tcharg = 0
        trod = 0
        ttot = 0
        if self.billType.get() == "All":
            self.cursor.execute("select entryno,entrydate,customername,customerid,totalqty,discount,charge,roundoff,total,nettotal,paytype from sale where status = %s and entrydate = %s",["active",date])
        else:
            self.cursor.execute("select entryno,entrydate,customername,customerid,totalqty,discount,charge,roundoff,total,nettotal,paytype from sale where status = %s and entrydate = %s and paytype = %s",["active",date,self.billType.get()])
        data = self.cursor.fetchall()
        for row in data:
            allData = self.reportTree.get_children()
            flag = True
            for myrow in allData:
                a = self.reportTree.item(myrow, "values")
                if row[0] in a:
                    flag = False
                    break
            if flag:
                listItem = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]] 
                self.reportTree.insert("", "end", values=listItem,tags=("item",))
                tqty += row[4]
                dits += row[5]
                tcharg += row[6]
                trod += row[7]
                ttot += row[8]
                tntot += row[9]

        self.quantity.configure(state='normal')
        self.Discount.configure(state='normal')
        self.Charge.configure(state='normal')
        self.RoundOff.configure(state='normal')
        self.Total.configure(state='normal')
        self.NetTotal.configure(state='normal')

        self.quantity.delete(0,END)
        self.Discount.delete(0,END)
        self.Charge.delete(0,END)
        self.RoundOff.delete(0,END)
        self.Total.delete(0,END)
        self.NetTotal.delete(0,END)
        
        self.quantity.insert(0,tqty)
        self.Discount.insert(0,dits)
        self.Charge.insert(0,tcharg)
        self.RoundOff.insert(0,trod)
        self.Total.insert(0,ttot)
        self.NetTotal.insert(0,tntot)

        self.quantity.configure(state='disabled')
        self.Discount.configure(state='disabled')
        self.Charge.configure(state='disabled')
        self.RoundOff.configure(state='disabled')
        self.Total.configure(state='disabled')
        self.NetTotal.configure(state='disabled')
        
        # print(f"tqty - {tqty}")
        # print(f"dits - {dits}")
        # print(f"tcharg - {tcharg}")
        # print(f"trod - {trod}")
        # print(f"ttot - {ttot}")
        # print(f"tntot - {tntot}")
        
class SaleDailyReport: 
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
        self.showReportButton.configure(command=self.addTreeDataOfSale)

        self.EntryNoLabel = Label(self.root)
        self.EntryNoLabel.place(relx=0.1, rely=0.09)
        self.EntryNoLabel.configure(text="Product No:")
        self.EntryNoLabel.configure(bg="#ad995e")
        self.EntryNoLabel.configure(fg="#6e5a20")
        self.EntryNoLabel.configure(font=f3)
        self.EntryNo = Entry(self.root)
        self.EntryNo.place(relx=0.1,rely=0.135)
        self.EntryNo.configure(width=12)
        self.EntryNo.configure(bg="#e5e6d5")
        self.EntryNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.billTypeLabel = Label(self.root)
        self.billTypeLabel.place(relx=0.33, rely=0.09)
        self.billTypeLabel.configure(text="Bill Type:")
        self.billTypeLabel.configure(bg="#ad995e")
        self.billTypeLabel.configure(fg="#6e5a20")
        self.billTypeLabel.configure(font=f3)
        self.billType = ttk.Combobox(self.root)  
        self.billType.place(relx=0.33, rely=0.135) 
        self.billType['values'] = ('All','cash','credit')
        self.billType.current(0)
        self.billType.configure(state='readonly')
        self.billType.configure(width=20)
        self.billType.configure(font=f2)
        self.billType.bind("<<ComboboxSelected>>",self.addTreeDataOfSale)

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
                "Sr No",
                "Product ID",
                "Product Name",
                "Sale Qty",
                "Return Qty",
                "Avai[R] Qty",
                "Selling Price",
            )
        )

        self.reportTree.heading("Sr No", text="Sr No", anchor=W)
        self.reportTree.heading("Product ID", text="Product ID", anchor=W)
        self.reportTree.heading("Product Name", text="Product Name", anchor=W)
        self.reportTree.heading("Sale Qty", text="Sale Qty", anchor=W)
        self.reportTree.heading("Return Qty", text="Return Qty", anchor=W)
        self.reportTree.heading("Avai[R] Qty", text="Avai[R] Qty", anchor=W)
        self.reportTree.heading("Selling Price", text="Selling Price", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=236)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=136)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeDataOfSale()
        # self.reportTree.bind("<Double-1>", self.itemDetail)
        # self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        
    def addTreeDataOfSale(self,event = '1'):
        self.reportTree.delete(*self.reportTree.get_children())
        date = self.isDate.get_date()

        self.cursor.execute("select product_id,product_description from product where status = %s",["active"])
        productIds = self.cursor.fetchall()
        srno = 0

        for productId in productIds:
            srno = srno + 1
            billType = self.billType.get()
            if self.billType.get() == "All":
                self.cursor.execute("select productno,productname,quantity,returnqty,avforreturnqty,sellingprice from sale where status = %s and entrydate = %s and productno = %s",["active",date,productId[0]])
            else:
                self.cursor.execute("select productno,productname,quantity,returnqty,avforreturnqty,sellingprice from sale where status = %s and entrydate = %s and productno = %s and paytype = %s",["active",date,productId[0],billType])
            
            data = self.cursor.fetchall()
            sqty = 0
            retqty = 0
            forreturnqty = 0
            sellp = 0
            for item in data:
                sqty = float(sqty) + float(item[2])
                retqty = float(retqty) + float(item[3])
                forreturnqty = float(forreturnqty) + float(item[4])
                sellp = float(sellp) + float(item[5])

            listItem = [srno,productId[0],productId[1],sqty,retqty,forreturnqty,sellp] 
            self.reportTree.insert("", "end", values=listItem,tags=("item",))

class SaleReturnReport:
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
        self.showReportButton.configure(command=self.addTreeDataOfSale)

        self.EntryNoLabel = Label(self.root)
        self.EntryNoLabel.place(relx=0.1, rely=0.09)
        self.EntryNoLabel.configure(text="Entry No:")
        self.EntryNoLabel.configure(bg="#ad995e")
        self.EntryNoLabel.configure(fg="#6e5a20")
        self.EntryNoLabel.configure(font=f3)
        self.EntryNo = Entry(self.root)
        self.EntryNo.place(relx=0.1,rely=0.135)
        self.EntryNo.configure(width=12)
        self.EntryNo.configure(bg="#e5e6d5")
        self.EntryNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.billTypeLabel = Label(self.root)
        self.billTypeLabel.place(relx=0.33, rely=0.09)
        self.billTypeLabel.configure(text="Bill Type:")
        self.billTypeLabel.configure(bg="#ad995e")
        self.billTypeLabel.configure(fg="#6e5a20")
        self.billTypeLabel.configure(font=f3)
        self.billType = ttk.Combobox(self.root)  
        self.billType.place(relx=0.33, rely=0.135) 
        self.billType['values'] = ('All','cash','credit')
        self.billType.current(0)
        self.billType.configure(state='readonly')
        self.billType.configure(width=20)
        self.billType.configure(font=f2)
        self.billType.bind("<<ComboboxSelected>>",self.addTreeDataOfSale)

        
        self.quantityLabel = Label(self.root)
        self.quantityLabel.place(relx=0.2, rely=0.85)
        self.quantityLabel.configure(text="Quantity:")
        self.quantityLabel.configure(bg="#ad995e")
        self.quantityLabel.configure(fg="#6e5a20")
        self.quantityLabel.configure(font=f3)
        self.quantity = Entry(self.root)
        self.quantity.place(relx=0.2,rely=0.9)
        self.quantity.configure(width=12)
        self.quantity.configure(bg="#e5e6d5")
        self.quantity.configure(font=f2)
        
        self.DiscountLabel = Label(self.root)
        self.DiscountLabel.place(relx=0.32, rely=0.85)
        self.DiscountLabel.configure(text="Discount:")
        self.DiscountLabel.configure(bg="#ad995e")
        self.DiscountLabel.configure(fg="#6e5a20")
        self.DiscountLabel.configure(font=f3)
        self.Discount = Entry(self.root)
        self.Discount.place(relx=0.32,rely=0.9)
        self.Discount.configure(width=12)
        self.Discount.configure(bg="#e5e6d5")
        self.Discount.configure(font=f2)
        
        self.ChargeLabel = Label(self.root)
        self.ChargeLabel.place(relx=0.44, rely=0.85)
        self.ChargeLabel.configure(text="Charge:")
        self.ChargeLabel.configure(bg="#ad995e")
        self.ChargeLabel.configure(fg="#6e5a20")
        self.ChargeLabel.configure(font=f3)
        self.Charge = Entry(self.root)
        self.Charge.place(relx=0.44,rely=0.9)
        self.Charge.configure(width=12)
        self.Charge.configure(bg="#e5e6d5")
        self.Charge.configure(font=f2)
        
        self.RoundOffLabel = Label(self.root)
        self.RoundOffLabel.place(relx=0.56, rely=0.85)
        self.RoundOffLabel.configure(text="Round Off:")
        self.RoundOffLabel.configure(bg="#ad995e")
        self.RoundOffLabel.configure(fg="#6e5a20")
        self.RoundOffLabel.configure(font=f3)
        self.RoundOff = Entry(self.root)
        self.RoundOff.place(relx=0.56,rely=0.9)
        self.RoundOff.configure(width=12)
        self.RoundOff.configure(bg="#e5e6d5")
        self.RoundOff.configure(font=f2)
        
        self.TotalLabel = Label(self.root)
        self.TotalLabel.place(relx=0.68, rely=0.85)
        self.TotalLabel.configure(text="Total:")
        self.TotalLabel.configure(bg="#ad995e")
        self.TotalLabel.configure(fg="#6e5a20")
        self.TotalLabel.configure(font=f3)
        self.Total = Entry(self.root)
        self.Total.place(relx=0.68,rely=0.9)
        self.Total.configure(width=12)
        self.Total.configure(bg="#e5e6d5")
        self.Total.configure(font=f2)
        
        self.NetTotalLabel = Label(self.root)
        self.NetTotalLabel.place(relx=0.80, rely=0.85)
        self.NetTotalLabel.configure(text="Net Total:")
        self.NetTotalLabel.configure(bg="#ad995e")
        self.NetTotalLabel.configure(fg="#6e5a20")
        self.NetTotalLabel.configure(font=f3)
        self.NetTotal = Entry(self.root)
        self.NetTotal.place(relx=0.80,rely=0.9)
        self.NetTotal.configure(width=12)
        self.NetTotal.configure(bg="#e5e6d5")
        self.NetTotal.configure(font=f2)

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
                "CrNote No",
                "CrNote Date",
                "Inv No",
                "Inv Date",
                "Customer Name",
                "Custo Id",
                "Quantity Tot",
                "Discount",
                "Charge",
                "Rou off",
                "Total Amt",
                "Net Tot Amt",
                "Bill Type"
            )
        )

        self.reportTree.heading("CrNote No", text="CrNote No", anchor=W)
        self.reportTree.heading("CrNote Date", text="CrNote Date", anchor=W)
        self.reportTree.heading("Inv No", text="Inv No", anchor=W)
        self.reportTree.heading("Inv Date", text="Inv Date", anchor=W)
        self.reportTree.heading("Customer Name", text="Customer Name", anchor=W)
        self.reportTree.heading("Custo Id", text="Custo Id", anchor=W)
        self.reportTree.heading("Quantity Tot", text="Quantity Tot", anchor=W)
        self.reportTree.heading("Discount", text="Discount", anchor=W)
        self.reportTree.heading("Charge", text="Charge", anchor=W)
        self.reportTree.heading("Rou off", text="Rou off", anchor=W)
        self.reportTree.heading("Total Amt", text="Total Amt", anchor=W)
        self.reportTree.heading("Net Tot Amt", text="Net Tot Amt", anchor=W)
        self.reportTree.heading("Bill Type", text="Bill Type", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=100)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=200)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=135)
        self.reportTree.column("#8", stretch=NO, minwidth=0, width=112)
        self.reportTree.column("#9", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#10", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#11", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#12", stretch=NO, minwidth=0, width=119)
        self.reportTree.column("#13", stretch=NO, minwidth=0, width=119)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        # self.addTreeDataOfSale()
        # self.reportTree.bind("<Double-1>", self.itemDetail)
        # self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        
    def addTreeDataOfSale(self,event = '1'):
        self.reportTree.delete(*self.reportTree.get_children())
        date = self.isDate.get_date()
        
        tqty = 0
        tntot = 0
        dits = 0
        tcharg = 0
        trod = 0
        ttot = 0

        if self.billType.get() == "All":
            self.cursor.execute("select crnoteno,crnotedate,invoiceno,invoicedate,customername,customerid,totalqty,discount,charge,roundoff,total,nettotal,paytype from salereturn where status = %s and crnotedate = %s",["active",date])
        else:
            self.cursor.execute("select crnoteno,crnotedate,invoiceno,invoicedate,customername,customerid,totalqty,discount,charge,roundoff,total,nettotal,paytype from salereturn where status = %s and crnotedate = %s and paytype = %s",["active",date,self.billType.get()])
        data = self.cursor.fetchall()
        for row in data:
            allData = self.reportTree.get_children()
            flag = True
            for myrow in allData:
                a = self.reportTree.item(myrow, "values")
                if row[0] in a:
                    flag = False
                    break
            if flag:
                listItem = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]] 
                self.reportTree.insert("", "end", values=listItem,tags=("item",))
                tqty += row[6]
                dits += row[7]
                tcharg += row[8]
                trod += row[9]
                ttot += row[10]
                tntot += row[11]

        
        self.quantity.configure(state='normal')
        self.Discount.configure(state='normal')
        self.Charge.configure(state='normal')
        self.RoundOff.configure(state='normal')
        self.Total.configure(state='normal')
        self.NetTotal.configure(state='normal')

        self.quantity.delete(0,END)
        self.Discount.delete(0,END)
        self.Charge.delete(0,END)
        self.RoundOff.delete(0,END)
        self.Total.delete(0,END)
        self.NetTotal.delete(0,END)
        
        self.quantity.insert(0,tqty)
        self.Discount.insert(0,dits)
        self.Charge.insert(0,tcharg)
        self.RoundOff.insert(0,trod)
        self.Total.insert(0,ttot)
        self.NetTotal.insert(0,tntot)

        self.quantity.configure(state='disabled')
        self.Discount.configure(state='disabled')
        self.Charge.configure(state='disabled')
        self.RoundOff.configure(state='disabled')
        self.Total.configure(state='disabled')
        self.NetTotal.configure(state='disabled')

class SaleReturnDailyReport: 
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
        self.showReportButton.configure(command=self.addTreeDataOfSale)

        self.EntryNoLabel = Label(self.root)
        self.EntryNoLabel.place(relx=0.1, rely=0.09)
        self.EntryNoLabel.configure(text="Product No:")
        self.EntryNoLabel.configure(bg="#ad995e")
        self.EntryNoLabel.configure(fg="#6e5a20")
        self.EntryNoLabel.configure(font=f3)
        self.EntryNo = Entry(self.root)
        self.EntryNo.place(relx=0.1,rely=0.135)
        self.EntryNo.configure(width=12)
        self.EntryNo.configure(bg="#e5e6d5")
        self.EntryNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.billTypeLabel = Label(self.root)
        self.billTypeLabel.place(relx=0.33, rely=0.09)
        self.billTypeLabel.configure(text="Bill Type:")
        self.billTypeLabel.configure(bg="#ad995e")
        self.billTypeLabel.configure(fg="#6e5a20")
        self.billTypeLabel.configure(font=f3)
        self.billType = ttk.Combobox(self.root)  
        self.billType.place(relx=0.33, rely=0.135) 
        self.billType['values'] = ('All','cash','credit')
        self.billType.current(0)
        self.billType.configure(state='readonly')
        self.billType.configure(width=20)
        self.billType.configure(font=f2)
        self.billType.bind("<<ComboboxSelected>>",self.addTreeDataOfSale)

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.08, rely=0.2, width=727, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.685, rely=0.20, width=18, height=395)

        self.reportTree = ttk.Treeview(self.root)
        self.reportTree.place(relx=0.08, rely=0.23, width=727, height=380)
        self.reportTree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.reportTree.xview)
        self.scrollbary.configure(command=self.reportTree.yview)
        # self.reportTree.configure()
        
        self.reportTree.configure(
            columns=(
                "Sr No",
                "Product ID",
                "Product Name",
                "Return Qty",
                "Stock Qty"
            )
        )

        self.reportTree.heading("Sr No", text="Sr No", anchor=W)
        self.reportTree.heading("Product ID", text="Product ID", anchor=W)
        self.reportTree.heading("Product Name", text="Product Name", anchor=W)
        self.reportTree.heading("Return Qty", text="Return Qty", anchor=W)
        self.reportTree.heading("Stock Qty", text="Stock Qty", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=236)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=136)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeDataOfSale()
        # self.reportTree.bind("<Double-1>", self.itemDetail)
        # self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        
    def addTreeDataOfSale(self,event = '1'):
        self.reportTree.delete(*self.reportTree.get_children())
        date = self.isDate.get_date()

        self.cursor.execute("select product_id,product_description from product where status = %s",["active"])
        productIds = self.cursor.fetchall()
        srno = 0

        for productId in productIds:
            billType = self.billType.get()
            if self.billType.get() == "All":
                self.cursor.execute("select quantity from salereturn where status = %s and crnotedate = %s and productnumber = %s",["active",date,productId[0]])
            else:
                self.cursor.execute("select quantity from salereturn where status = %s and crnotedate = %s and productnumber = %s and paytype = %s",["active",date,productId[0],billType])
            
            data = self.cursor.fetchall()
            self.cursor.execute("select availableqty from purchase where (status = %s or status = %s) and productno = %s",["dc","inv",productId[0]])
            purchaseData = self.cursor.fetchall()
            avqty = 0
            for qty in purchaseData:
                avqty = float(avqty) + float(qty[0])
            retqty = 0
            for item in data:
                retqty = float(retqty) + float(item[0])

            if retqty > 0:
                srno = srno + 1
                listItem = [srno,productId[0],productId[1],retqty,avqty] 
                self.reportTree.insert("", "end", values=listItem,tags=("item",))

class SaleMonthlyReport: 
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
        self.fromDateLabel.configure(text="From:")
        self.fromDateLabel.configure(bg="#ad995e")
        self.fromDateLabel.configure(fg="#6e5a20")
        self.fromDateLabel.configure(font=f3)
        self.fromDate = DateEntry(self.root)
        self.fromDate.place(relx=0.15,rely=0.029)
        self.fromDate.configure(background='#6e5a20', foreground='#ad995e')
        self.fromDate.configure(width=10)
                
        self.toDateLabel = Label(self.root)
        self.toDateLabel.place(relx=0.27,rely=0.025)
        self.toDateLabel.configure(text="To:")
        self.toDateLabel.configure(bg="#ad995e")
        self.toDateLabel.configure(fg="#6e5a20")
        self.toDateLabel.configure(font=f3)
        self.toDate = DateEntry(self.root)
        self.toDate.place(relx=0.3,rely=0.029)
        self.toDate.configure(background='#6e5a20', foreground='#ad995e')
        self.toDate.configure(width=10)

        now = datetime.now()
        lastDay = calendar.monthrange(now.year, now.month)

        try:
                selected_date = datetime.strptime(f"{str(now.year)}-{str(now.month)}-{1}", "%Y-%m-%d")
                self.fromDate.set_date(selected_date)
                selected_date = datetime.strptime(f"{str(now.year)}-{str(now.month)}-{lastDay[1]}", "%Y-%m-%d")
                self.toDate.set_date(selected_date)
        except ValueError:
                print("Invalid format of Expiry date")
                
        self.showReportButton = Button(self.root)
        self.showReportButton.place(relx=0.41,rely=0.026)
        self.showReportButton.configure(text="Show")
        self.showReportButton.configure(font=f1)
        self.showReportButton.configure(width=12)
        self.showReportButton.configure(activebackground="#ad995e")
        self.showReportButton.configure(bg="#e0cb8d")
        self.showReportButton.configure(command=self.addTreeDataOfSale)

        self.EntryNoLabel = Label(self.root)
        self.EntryNoLabel.place(relx=0.1, rely=0.09)
        self.EntryNoLabel.configure(text="Product No:")
        self.EntryNoLabel.configure(bg="#ad995e")
        self.EntryNoLabel.configure(fg="#6e5a20")
        self.EntryNoLabel.configure(font=f3)
        self.EntryNo = Entry(self.root)
        self.EntryNo.place(relx=0.1,rely=0.135)
        self.EntryNo.configure(width=12)
        self.EntryNo.configure(bg="#e5e6d5")
        self.EntryNo.configure(font=f2)

        self.searchButton = Button(self.root)
        self.searchButton.place(relx=0.217,rely=0.131)
        self.searchButton.configure(text="Search")
        self.searchButton.configure(font=f1)
        self.searchButton.configure(width=12)
        self.searchButton.configure(activebackground="#ad995e")
        self.searchButton.configure(bg="#e0cb8d")
        
        self.billTypeLabel = Label(self.root)
        self.billTypeLabel.place(relx=0.33, rely=0.09)
        self.billTypeLabel.configure(text="Bill Type:")
        self.billTypeLabel.configure(bg="#ad995e")
        self.billTypeLabel.configure(fg="#6e5a20")
        self.billTypeLabel.configure(font=f3)
        self.billType = ttk.Combobox(self.root)  
        self.billType.place(relx=0.33, rely=0.135) 
        self.billType['values'] = ('All','cash','credit')
        self.billType.current(0)
        self.billType.configure(state='readonly')
        self.billType.configure(width=20)
        self.billType.configure(font=f2)
        self.billType.bind("<<ComboboxSelected>>",self.addTreeDataOfSale)

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
                "Sr No",
                "Product ID",
                "Product Name",
                "Sale Qty",
                "Return Qty",
                "Avai[R] Qty",
                "Selling Price",
            )
        )

        self.reportTree.heading("Sr No", text="Sr No", anchor=W)
        self.reportTree.heading("Product ID", text="Product ID", anchor=W)
        self.reportTree.heading("Product Name", text="Product Name", anchor=W)
        self.reportTree.heading("Sale Qty", text="Sale Qty", anchor=W)
        self.reportTree.heading("Return Qty", text="Return Qty", anchor=W)
        self.reportTree.heading("Avai[R] Qty", text="Avai[R] Qty", anchor=W)
        self.reportTree.heading("Selling Price", text="Selling Price", anchor=W)

        self.reportTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.reportTree.column("#1", stretch=NO, minwidth=0, width=80)
        self.reportTree.column("#2", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#3", stretch=NO, minwidth=0, width=236)
        self.reportTree.column("#4", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#5", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#6", stretch=NO, minwidth=0, width=136)
        self.reportTree.column("#7", stretch=NO, minwidth=0, width=136)

        self.reportTree.configure(selectmode="extended")
        self.reportTree.tag_configure("item", background="#fce89d", foreground="black", font=f1)
        self.addTreeDataOfSale()
        # self.reportTree.bind("<Double-1>", self.itemDetail)
        # self.reportTree.bind("<<TreeviewSelect>>", self.onSingleclick)
        
    def addTreeDataOfSale(self,event = '1'):
        self.reportTree.delete(*self.reportTree.get_children())
        fromdate = self.fromDate.get_date()
        todate = self.toDate.get_date()
        self.cursor.execute("select product_id,product_description from product where status = %s",["active"])
        productIds = self.cursor.fetchall()
        srno = 0

        for productId in productIds:
            srno = srno + 1
            billType = self.billType.get()
            if self.billType.get() == "All":
                self.cursor.execute("select productno,productname,quantity,returnqty,avforreturnqty,sellingprice from sale where status = %s and (entrydate > %s or entrydate < %s) and productno = %s",["active",fromdate,todate,productId[0]])
            else:
                self.cursor.execute("select productno,productname,quantity,returnqty,avforreturnqty,sellingprice from sale where status = %s and (entrydate > %s or entrydate < %s) and productno = %s and paytype = %s",["active",fromdate,todate,productId[0],billType])
            
            data = self.cursor.fetchall()
            sqty = 0
            retqty = 0
            forreturnqty = 0
            sellp = 0
            for item in data:
                sqty = float(sqty) + float(item[2])
                retqty = float(retqty) + float(item[3])
                forreturnqty = float(forreturnqty) + float(item[4])
                sellp = float(sellp) + float(item[5])

            listItem = [srno,productId[0],productId[1],sqty,retqty,forreturnqty,sellp] 
            self.reportTree.insert("", "end", values=listItem,tags=("item",))
