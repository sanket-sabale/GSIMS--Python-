# ==================( IMPORT )==================
from tkinter import *
# import re
# import string
import mysql.connector
# import random
# import psutil
# from datetime import date
from tkinter import ttk
# from GSIMSPac import fun
# from GSIMSPac import Product
# from GSIMSPac import Partys
# from GSIMSPac import PurchaseDC
# from GSIMSPac import PurchaseInvoice
# from datetime import datetime
# from tkcalendar import DateEntry
from tkinter import messagebox
# ===============================================

class partyReports:
    def __init__(self,canvas_widget):
        
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        self.cursor = self.mydb.cursor()

        self.f1 = ("Times", 11)
        self.f2 = ("Courier New", 12)
        self.f3 = ("Arial Black", 12)
        self.f4 = ("Arial Black", 11)
        self.f5 = ("Arial Black", 10)
        
        self.radiooption = StringVar()

        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.1,rely=0.165)
        self.root.configure(width=1200,height=610)
        self.root.configure(bg="#ad995e")

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.08, rely=0.1, width=1000, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.915, rely=0.10, width=18, height=395)

        self.partyTree = ttk.Treeview(self.root)
        self.partyTree.place(relx=0.08, rely=0.13, width=1000, height=380)
        self.partyTree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.partyTree.xview)
        self.scrollbary.configure(command=self.partyTree.yview)
        
        self.partyTree.configure(
            columns=(
                "Party ID",
                "Party Name",
                "GSTIN No",
                "Location",
                "Owner Name",
                "Mobile No",
                "E-mail",
                "District",
                "Shop No",
                "Taluka",
                "State"
            )
        )

        self.partyTree.heading("Party ID", text="Party ID", anchor=W)
        self.partyTree.heading("Party Name", text="Party Name", anchor=W)
        self.partyTree.heading("GSTIN No", text="GSTIN No", anchor=W)
        self.partyTree.heading("Location", text="Location", anchor=W)
        self.partyTree.heading("Owner Name", text="Owner Name", anchor=W)
        self.partyTree.heading("Mobile No", text="Mobile No", anchor=W)
        self.partyTree.heading("E-mail", text="E-mail", anchor=W)
        self.partyTree.heading("District", text="District", anchor=W)
        self.partyTree.heading("Shop No", text="Shop No", anchor=W)
        self.partyTree.heading("Taluka", text="Taluka", anchor=W)
        self.partyTree.heading("State", text="State", anchor=W)

        self.partyTree.column("#0", stretch=NO, minwidth=0, width=0)
        self.partyTree.column("#1", stretch=NO, minwidth=0, width=110)
        self.partyTree.column("#2", stretch=NO, minwidth=0, width=200)
        self.partyTree.column("#3", stretch=NO, minwidth=0, width=150)
        self.partyTree.column("#4", stretch=NO, minwidth=0, width=110)
        self.partyTree.column("#5", stretch=NO, minwidth=0, width=150)
        self.partyTree.column("#6", stretch=NO, minwidth=0, width=110)
        self.partyTree.column("#7", stretch=NO, minwidth=0, width=180)
        self.partyTree.column("#8", stretch=NO, minwidth=0, width=120)
        self.partyTree.column("#9", stretch=NO, minwidth=0, width=110)
        self.partyTree.column("#10", stretch=NO, minwidth=0, width=130)
        self.partyTree.column("#11", stretch=NO, minwidth=0, width=130)
        self.partyTree.configure(selectmode="extended")
        self.partyTree.tag_configure("item", background="#fce89d", foreground="black", font=self.f1)
        self.addTreeData()
        # self.partyTree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        self.partyTree.bind("<Double-1>", self.showPartyData)
        
    def showPartyData(self,event):
        self.dataroot = Canvas(self.root)
        self.dataroot.place(relx=0.0,rely=0.0)
        self.dataroot.configure(width=1200,height=610)
        self.dataroot.configure(bg="#ad995e")

        self.closeButton = Button(self.dataroot)
        self.closeButton.place(relx = 0.97, rely=0.009)
        self.closeButton.configure(text="❌", font=("arial", 10))
        self.closeButton.configure(bg="#ad995e", activebackground="#63412c", fg="#fce89d", activeforeground="#fce89d")
        self.closeButton.configure(command=self.closePartyData)
        
        self.scrollbarx = Scrollbar(self.dataroot, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.08, rely=0.15, width=1000, height=15)

        self.scrollbary = Scrollbar(self.dataroot, orient=VERTICAL)
        self.scrollbary.place(relx=0.915, rely=0.15, width=18, height=395)

        self.tree = ttk.Treeview(self.dataroot)
        self.tree.place(relx=0.08, rely=0.18, width=1000, height=380)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.configure(command=self.tree.yview)
        
        self.tree.configure(
            columns=(
                "Entry ID",
                "Entry Date",
                "Bill/DC no",
                "Bill/DC date",
                "Bill Type",
                "Total QTY",
                "Discount",
                "Charge",
                "Rou Off",
                "Total",
                "Net Total"
            )
        )

        self.tree.heading("Entry ID", text="Entry ID", anchor=W)
        self.tree.heading("Entry Date", text="Entry Date", anchor=W)
        self.tree.heading("Bill/DC no", text="Bill/DC no", anchor=W)
        self.tree.heading("Bill/DC date", text="Bill/DC date", anchor=W)
        self.tree.heading("Bill Type", text="Bill Type", anchor=W)
        self.tree.heading("Total QTY", text="Total QTY", anchor=W)
        self.tree.heading("Discount", text="Discount", anchor=W)
        self.tree.heading("Charge", text="Charge", anchor=W)
        self.tree.heading("Rou Off", text="Rou Off", anchor=W)
        self.tree.heading("Total", text="Total", anchor=W)
        self.tree.heading("Net Total", text="Net Total", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=170)
        self.tree.column("#2", stretch=NO, minwidth=0, width=170)
        self.tree.column("#3", stretch=NO, minwidth=0, width=170)
        self.tree.column("#4", stretch=NO, minwidth=0, width=170)
        self.tree.column("#5", stretch=NO, minwidth=0, width=170)
        self.tree.column("#6", stretch=NO, minwidth=0, width=170)
        self.tree.column("#7", stretch=NO, minwidth=0, width=170)
        self.tree.column("#8", stretch=NO, minwidth=0, width=170)
        self.tree.column("#9", stretch=NO, minwidth=0, width=170)
        self.tree.column("#10", stretch=NO, minwidth=0, width=170)
        self.tree.column("#11", stretch=NO, minwidth=0, width=170)
        # self.tree.configure(selectmode="extended")
        self.tree.tag_configure("item", background="#fce89d", foreground="black", font=self.f1)

        item = self.partyTree.selection()
        if item:
            data = self.partyTree.item(item, "values")
        
        self.partyIdLabel = Label(self.dataroot)
        self.partyIdLabel.place(relx=0.12,rely=0.045)
        self.partyIdLabel.configure(text="Party Name:")
        self.partyIdLabel.configure(bg="#ad995e")
        self.partyIdLabel.configure(fg="#6e5a20")
        self.partyIdLabel.configure(font=self.f3)
        self.partyId = Entry(self.dataroot)
        self.partyId.place(relx=0.22,rely=0.05)
        self.partyId.configure(width=8)
        self.partyId.configure(bg="#e5e6d5")
        self.partyId.configure(font=self.f2)
        self.partyId.insert(END,data[0])
        self.partyId.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        self.partyName = Entry(self.dataroot)
        self.partyName.place(relx=0.3,rely=0.05)
        self.partyName.configure(width=25)
        self.partyName.configure(bg="#e5e6d5")
        self.partyName.configure(font=self.f2)
        self.partyName.insert(END,data[1])
        self.partyName.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')

        self.payType = ttk.Combobox(self.dataroot)  
        self.payType.place(relx=0.55,rely=0.05)
        self.payType['values'] = ("All","Cash","Credit")
        self.payType.current(0)
        self.payType.configure(width=10)
        self.payType.configure(font=self.f2)
        self.payType.configure(state='readonly')
        self.payType.bind("<<ComboboxSelected>>", self.onSelectType)

        self.type = ttk.Combobox(self.dataroot)  
        self.type.place(relx=0.66,rely=0.05)
        self.type['values'] = ("Select","Purchase Invo","Purchase D/C")
        self.type.current(0)
        self.type.configure(width=15)
        self.type.configure(font=self.f2)
        self.type.configure(state='readonly')
        self.type.bind("<<ComboboxSelected>>", self.onSelectType)
        
        self.qtytotLabel = Label(self.dataroot)
        self.qtytotLabel.place(relx=0.31,rely=0.85)
        self.qtytotLabel.configure(text="Qty Total")
        self.qtytotLabel.configure(bg="#ad995e")
        self.qtytotLabel.configure(fg="#6e5a20")
        self.qtytotLabel.configure(font=self.f5)
        self.qtytot = Entry(self.dataroot)
        self.qtytot.place(relx=0.37,rely=0.85)
        self.qtytot.configure(width=10)
        self.qtytot.configure(bg="#e5e6d5")
        self.qtytot.configure(font=self.f2)
        self.qtytot.insert(0,0.0)
        self.qtytot.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')

        self.discountLabel = Label(self.dataroot)
        self.discountLabel.place(relx=0.51,rely=0.85)
        self.discountLabel.configure(text="Discount")
        self.discountLabel.configure(bg="#ad995e")
        self.discountLabel.configure(fg="#6e5a20")
        self.discountLabel.configure(font=self.f5)
        self.discount = Entry(self.dataroot)
        self.discount.place(relx=0.57,rely=0.85)
        self.discount.configure(width=10)
        self.discount.configure(bg="#e5e6d5")
        self.discount.configure(font=self.f2)
        self.discount.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        
        self.chargeLabel = Label(self.dataroot)
        self.chargeLabel.place(relx=0.52,rely=0.9)
        self.chargeLabel.configure(text="Charge")
        self.chargeLabel.configure(bg="#ad995e")
        self.chargeLabel.configure(fg="#6e5a20")
        self.chargeLabel.configure(font=self.f5)
        self.charge = Entry(self.dataroot)
        self.charge.place(relx=0.57,rely=0.9)
        self.charge.configure(width=10)
        self.charge.configure(bg="#e5e6d5")
        self.charge.configure(font=self.f2)
        self.charge.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        
        self.roundOffLabel = Label(self.dataroot)
        self.roundOffLabel.place(relx=0.3,rely=0.9)
        self.roundOffLabel.configure(text="Round Off")
        self.roundOffLabel.configure(bg="#ad995e")
        self.roundOffLabel.configure(fg="#6e5a20")
        self.roundOffLabel.configure(font=self.f5)
        self.roundOff = Entry(self.dataroot)
        self.roundOff.place(relx=0.37,rely=0.9)
        self.roundOff.configure(width=10)
        self.roundOff.configure(bg="#e5e6d5")
        self.roundOff.configure(font=self.f2)
        self.roundOff.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        
        self.totalLabel = Label(self.dataroot)
        self.totalLabel.place(relx=0.711,rely=0.85)
        self.totalLabel.configure(text="Total")
        self.totalLabel.configure(bg="#ad995e")
        self.totalLabel.configure(fg="#6e5a20")
        self.totalLabel.configure(font=self.f5)
        self.total = Entry(self.dataroot)
        self.total.place(relx=0.75,rely=0.85)
        self.total.configure(width=10)
        self.total.configure(bg="#e5e6d5")
        self.total.configure(font=self.f2)
        self.total.insert(0,0.0)
        self.total.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')
        
        self.netTotalLabel = Label(self.dataroot)
        self.netTotalLabel.place(relx=0.688,rely=0.90)
        self.netTotalLabel.configure(text="Net Total")
        self.netTotalLabel.configure(bg="#ad995e")
        self.netTotalLabel.configure(fg="#6e5a20")
        self.netTotalLabel.configure(font=self.f5)
        self.netTotal = Entry(self.dataroot)
        self.netTotal.place(relx=0.75,rely=0.90)
        self.netTotal.configure(width=10)
        self.netTotal.configure(bg="#e5e6d5")
        self.netTotal.configure(font=self.f2)
        self.netTotal.insert(0,0.0)
        self.netTotal.configure(state="disabled",disabledbackground="#fce89d",disabledforeground='black')

    def onSelectType(self,event):        
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cursor = mydb.cursor()

        partyname = self.partyName.get()
        partyid = self.partyId.get()
        paytype = self.payType.get()
        mytype = self.type.get()
        mydata = []
        totalqty = 0
        discount = 0
        charge = 0
        roff = 0
        total = 0
        nettotal = 0
        
        if mytype == "Purchase Invo":
            if paytype == "All":
                query = "select purchaseid,purchasedate,billno,billdate,paytype,qtytotal,discount,charge,roundoff,total,nettotal from purchase where supplierid = %s and suppliername = %s and status = %s"
                cursor.execute(query,[partyid,partyname,"inv"])
                mydata = cursor.fetchall()
            elif paytype == "Cash":
                query = "select purchaseid,purchasedate,billno,billdate,paytype,qtytotal,discount,charge,roundoff,total,nettotal from purchase where supplierid = %s and suppliername = %s and status = %s and paytype = %s"
                cursor.execute(query,[partyid,partyname,"inv","cash"])
                mydata = cursor.fetchall()
            else:
                query = "select purchaseid,purchasedate,billno,billdate,paytype,qtytotal,discount,charge,roundoff,total,nettotal from purchase where supplierid = %s and suppliername = %s and status = %s and paytype = %s"
                cursor.execute(query,[partyid,partyname,"inv","credit"])
                mydata = cursor.fetchall()
        elif mytype == "Purchase D/C":
            query = "select purchasedcid,purchasedcdate,dcno,dcdate,paytype,qtytotal,discount,charge,roundoff,total,nettotal from purchase where supplierid = %s and suppliername = %s and status = %s"
            cursor.execute(query,[partyid,partyname,"dc"])
            mydata = cursor.fetchall()
        else:
            pass

        mydb.commit()
        if mydata:
            self.tree.delete(*self.tree.get_children())
            for item in mydata:
                allData = self.tree.get_children()
                self.tree.insert("", "end", values=item,tags=("item",))
                flag = True
                for row in allData:
                    a = self.tree.item(row, "values")
                    if item[0] in a:
                        flag = False
                        break
                if flag:
                    totalqty = float(totalqty) + float(item[5])
                    discount = float(discount) + float(item[6])
                    charge = float(charge) + float(item[7])
                    roff = float(roff) + float(item[8])
                    total = float(total) + float(item[9])
                    nettotal = float(nettotal) + float(item[10])
            # to check here this block of code gives wrong output beacouse logical error 
            # we need to calculate i think, it's need to create a flage and then calculate those values
            self.qtytot.configure(state='normal')
            self.discount.configure(state='normal')
            self.charge.configure(state='normal')
            self.roundOff.configure(state='normal')
            self.total.configure(state='normal')
            self.netTotal.configure(state='normal')
            
            self.qtytot.delete(0,END)
            self.discount.delete(0,END)
            self.charge.delete(0,END)
            self.roundOff.delete(0,END)
            self.total.delete(0,END)
            self.netTotal.delete(0,END)
            
            self.qtytot.insert(END,totalqty)
            self.discount.insert(END,discount)
            self.charge.insert(END,charge)
            self.roundOff.insert(END,roff)
            self.total.insert(END,total)
            self.netTotal.insert(END,nettotal)
            
            self.qtytot.configure(state='disabled')
            self.discount.configure(state='disabled')
            self.charge.configure(state='disabled')
            self.roundOff.configure(state='disabled')
            self.total.configure(state='disabled')
            self.netTotal.configure(state='disabled')
        else:
            self.qtytot.configure(state='normal')
            self.discount.configure(state='normal')
            self.charge.configure(state='normal')
            self.roundOff.configure(state='normal')
            self.total.configure(state='normal')
            self.netTotal.configure(state='normal')
            self.qtytot.delete(0,END)
            self.discount.delete(0,END)
            self.charge.delete(0,END)
            self.roundOff.delete(0,END)
            self.total.delete(0,END)
            self.netTotal.delete(0,END)
            self.qtytot.configure(state='disabled')
            self.discount.configure(state='disabled')
            self.charge.configure(state='disabled')
            self.roundOff.configure(state='disabled')
            self.total.configure(state='disabled')
            self.netTotal.configure(state='disabled')
            self.tree.delete(*self.tree.get_children())
            messagebox.showinfo("",f"No such Data   : (")

    def closePartyData(self):
        for widget in self.dataroot.winfo_children():
            widget.destroy()
        self.dataroot.destroy()
    
    def addTreeData(self):
        self.partyTree.delete(*self.partyTree.get_children())
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cursor = mydb.cursor()
        query = "select * from partys where status = %s"
        cursor.execute(query,["active"])
        data = cursor.fetchall()
        for item in data:
            row = (item[1],item[2],item[3],item[4],item[6],item[5],item[7],item[8],item[9],item[10],item[11])
            self.partyTree.insert("", "end", values=row,tags=("item",))
        mydb.commit()