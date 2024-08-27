# ==================( IMPORT )==================
from tkinter import *
import re
import string
import mysql.connector
import random
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


def random_party_no():
    # letters = string.ascii_uppercase
    result = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
    result0 = random.randint(1000,9999)
    bill_number = f"{result}{result0}"
    return bill_number

class NewParty:
    
    def __init__(self,canvas_widget):

        f1 = ("Times", 12)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 13)

        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.22,rely=0.2)
        self.root.configure(width=800,height=500)
        self.root.configure(bg="#ad995e")

        self.validInteger = self.root.register(self.testint)

        self.partyNameLabel = Label(self.root)
        self.partyNameLabel.place(relx=0.1,rely=0.02)
        self.partyNameLabel.configure(text="Party Name")
        self.partyNameLabel.configure(bg="#ad995e")
        self.partyNameLabel.configure(font=f1)
        self.partyName = Entry(self.root)
        self.partyName.place(relx=0.1,rely=0.07)
        self.partyName.configure(width=30)
        self.partyName.configure(bg="#e5e6d5")
        self.partyName.configure(font=f2)
        
        self.gstinnoLabel = Label(self.root)
        self.gstinnoLabel.place(relx=0.1,rely=0.15)
        self.gstinnoLabel.configure(text="GSTIN No:")
        self.gstinnoLabel.configure(bg="#ad995e")
        self.gstinnoLabel.configure(font=f1)
        self.gstinno = Entry(self.root)
        self.gstinno.place(relx=0.1,rely=0.2)
        self.gstinno.configure(width=30)
        self.gstinno.configure(bg="#e5e6d5")
        self.gstinno.configure(font=f2)
        
        self.locationLabel = Label(self.root)
        self.locationLabel.place(relx=0.1,rely=0.28)
        self.locationLabel.configure(text="Location:")
        self.locationLabel.configure(bg="#ad995e")
        self.locationLabel.configure(font=f1)
        self.location = Entry(self.root)
        self.location.place(relx=0.1,rely=0.33)
        self.location.configure(width=30)
        self.location.configure(bg="#e5e6d5")
        self.location.configure(font=f2)
        
        self.ownerNameLabel = Label(self.root)
        self.ownerNameLabel.place(relx=0.1,rely=0.41)
        self.ownerNameLabel.configure(text="Owner Name:")
        self.ownerNameLabel.configure(bg="#ad995e")
        self.ownerNameLabel.configure(font=f1)
        self.ownerName = Entry(self.root)
        self.ownerName.place(relx=0.1,rely=0.46)
        self.ownerName.configure(width=30)
        self.ownerName.configure(bg="#e5e6d5")
        self.ownerName.configure(font=f2)
        
        self.monoLabel = Label(self.root)
        self.monoLabel.place(relx=0.1,rely=0.54)
        self.monoLabel.configure(text="Mobile No:")
        self.monoLabel.configure(bg="#ad995e")
        self.monoLabel.configure(font=f1)
        self.mono = Entry(self.root)
        self.mono.place(relx=0.1,rely=0.59)
        self.mono.configure(width=30)
        self.mono.configure(bg="#e5e6d5")
        self.mono.configure(font=f2)
        self.mono.configure(validate="key", validatecommand=(self.validInteger, "%P"))
        
        self.disLabel = Label(self.root)
        self.disLabel.place(relx=0.5,rely=0.02)
        self.disLabel.configure(text="District:")
        self.disLabel.configure(bg="#ad995e")
        self.disLabel.configure(font=f1)
        self.dis = Entry(self.root)
        self.dis.place(relx=0.5,rely=0.07)
        self.dis.configure(width=30)
        self.dis.configure(bg="#e5e6d5")
        self.dis.configure(font=f2)
        
        self.shopNoLabel = Label(self.root)
        self.shopNoLabel.place(relx=0.5,rely=0.15)
        self.shopNoLabel.configure(text="Shop No:")
        self.shopNoLabel.configure(bg="#ad995e")
        self.shopNoLabel.configure(font=f1)
        self.shopNo = Entry(self.root)
        self.shopNo.place(relx=0.5,rely=0.2)
        self.shopNo.configure(width=30)
        self.shopNo.configure(bg="#e5e6d5")
        self.shopNo.configure(font=f2)
        
        self.talLabel = Label(self.root)
        self.talLabel.place(relx=0.5,rely=0.28)
        self.talLabel.configure(text="Taluka:")
        self.talLabel.configure(bg="#ad995e")
        self.talLabel.configure(font=f1)
        self.tal = Entry(self.root)
        self.tal.place(relx=0.5,rely=0.33)
        self.tal.configure(width=30)
        self.tal.configure(bg="#e5e6d5")
        self.tal.configure(font=f2)
        
        self.stateLabel = Label(self.root)
        self.stateLabel.place(relx=0.5,rely=0.41)
        self.stateLabel.configure(text="State:")
        self.stateLabel.configure(bg="#ad995e")
        self.stateLabel.configure(font=f1)
        self.state = Entry(self.root)
        self.state.place(relx=0.5,rely=0.46)
        self.state.configure(width=30)
        self.state.configure(bg="#e5e6d5")
        self.state.configure(font=f2)
        
        self.emailLabel = Label(self.root)
        self.emailLabel.place(relx=0.5,rely=0.54)
        self.emailLabel.configure(text="E-mail ID:")
        self.emailLabel.configure(bg="#ad995e")
        self.emailLabel.configure(font=f1)
        self.email = Entry(self.root)
        self.email.place(relx=0.5,rely=0.59)
        self.email.configure(width=30)
        self.email.configure(bg="#e5e6d5")
        self.email.configure(font=f2)

        self.addButton = Button(self.root)
        self.addButton.place(relx=0.18,rely=0.75)
        self.addButton.configure(text="ADD")
        self.addButton.configure(font=f3)
        self.addButton.configure(width=11)
        self.addButton.configure(bg="#e5e6d5")
        self.addButton.configure(fg="#ad995e")
        self.addButton.configure(command=self.addToDatabase)
        
        self.clearButton = Button(self.root)
        self.clearButton.place(relx=0.60,rely=0.75)
        self.clearButton.configure(text="CLEAR")
        self.clearButton.configure(font=f3)
        self.clearButton.configure(width=11)
        self.clearButton.configure(bg="#e5e6d5")
        self.clearButton.configure(fg="#ad995e")
        self.clearButton.configure(command=self.clearall)

    def addToDatabase(self):
        pname = self.partyName.get()
        gstno = self.gstinno.get()
        locat = self.location.get()
        mono = self.mono.get()
        ownern = self.ownerName.get()
        dis = self.dis.get()
        sno = self.shopNo.get()
        tal = self.tal.get()
        sta = self.state.get()
        emai = self.email.get()

        if pname.strip():
            if gstno.strip() and self.isValidgstin(gstno):
                if locat.strip():
                    if mono.strip() and self.isValidPhone(mono):
                        if ownern.strip():
                            mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
                            cur = mydb.cursor()
                            insert = "INSERT INTO partys(partyno,partyid, partyname, gstinno, location, mobileno, ownername, email, district, shopno, taluka, state, status, debit,credit) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            cur.execute(insert, [None, random_party_no(),pname,gstno,locat,mono,ownern,emai,dis,sno,tal,sta,"active",None,None])
                            messagebox.showinfo("Done","Party added successfully")
                            self.clearall()
                            mydb.commit()
                        else:
                            messagebox.showwarning("Warning","Enter owner name.")
                    else:
                        messagebox.showwarning("Warning","Enter valid mobile number.")
                else:
                    messagebox.showwarning("Warning","Enter location of shop.")
            else:
                messagebox.showwarning("Warning","Enter GSTIN valid number.")
        else:
            messagebox.showwarning("Warning","Enter party name.")
    
    def isValidPhone(self,phn):
        if re.match(r"[789]\d{9}$", phn):
            return True
        return False
    
    def isValidemail(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        match = re.match(pattern,email)
        return bool(match)
    
    def isValidgstin(self,gstin):
        pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[0-9A-Z]{1}[Z]{1}[0-9A-Z]{1}$'
        match = re.match(pattern,gstin)
        return bool(match)    
    
    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False
    
    def clearall(self):
        self.partyName.delete(0, END)
        self.gstinno.delete(0, END)
        self.location.delete(0, END)
        self.dis.delete(0, END)
        self.mono.delete(0, END)
        self.ownerName.delete(0, END)
        self.shopNo.delete(0, END)
        self.tal.delete(0, END)
        self.state.delete(0, END)
        self.email.delete(0, END)

class deleteParty:
    def __init__(self,canvas_widget):
        
        f1 = ("Times", 12)
        f2 = ("Courier New", 12)
        f3 = ("Arial", 13)
        f4 = ("Courier New", 11)

        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.17,rely=0.2)
        self.root.configure(width=1000,height=500)
        self.root.configure(bg="#ad995e")

        self.partyIdLabel = Label(self.root)
        self.partyIdLabel.place(relx=0.02,rely=0.02)
        self.partyIdLabel.configure(text="Party ID")
        self.partyIdLabel.configure(bg="#ad995e")
        self.partyIdLabel.configure(font=f1)
        self.partyId = Entry(self.root)
        self.partyId.place(relx=0.02,rely=0.07)
        self.partyId.configure(width=15)
        self.partyId.configure(bg="#e5e6d5")
        self.partyId.configure(font=f2)
        self.partyId.configure(state='disabled', disabledforeground="#043d10")

        self.partyNameLabel = Label(self.root)
        self.partyNameLabel.place(relx=0.2,rely=0.02)
        self.partyNameLabel.configure(text="Party Name")
        self.partyNameLabel.configure(bg="#ad995e")
        self.partyNameLabel.configure(font=f1)
        self.partyName = Entry(self.root)
        self.partyName.place(relx=0.2,rely=0.07)
        self.partyName.configure(width=25)
        self.partyName.configure(bg="#e5e6d5")
        self.partyName.configure(font=f2)
        self.partyName.configure(state='disabled', disabledforeground="#043d10")

        self.gstInNoLabel = Label(self.root)
        self.gstInNoLabel.place(relx=0.48,rely=0.02)
        self.gstInNoLabel.configure(text="GSTIN No")
        self.gstInNoLabel.configure(bg="#ad995e")
        self.gstInNoLabel.configure(font=f1)
        self.gstInNo = Entry(self.root)
        self.gstInNo.place(relx=0.48,rely=0.07)
        self.gstInNo.configure(width=25)
        self.gstInNo.configure(bg="#e5e6d5")
        self.gstInNo.configure(font=f2)
        self.gstInNo.configure(state='disabled', disabledforeground="#043d10")
        
        self.locationLabel = Label(self.root)
        self.locationLabel.place(relx=0.76,rely=0.02)
        self.locationLabel.configure(text="Location")
        self.locationLabel.configure(bg="#ad995e")
        self.locationLabel.configure(font=f1)
        self.location = Entry(self.root)
        self.location.place(relx=0.76,rely=0.07)
        self.location.configure(width=21)
        self.location.configure(bg="#e5e6d5")
        self.location.configure(font=f2)
        self.location.configure(state='disabled', disabledforeground="#043d10")
        
        self.ownerNameLabel = Label(self.root)
        self.ownerNameLabel.place(relx=0.02,rely=0.14)
        self.ownerNameLabel.configure(text="Owner Name")
        self.ownerNameLabel.configure(bg="#ad995e")
        self.ownerNameLabel.configure(font=f1)
        self.ownerName = Entry(self.root)
        self.ownerName.place(relx=0.02,rely=0.19)
        self.ownerName.configure(width=21)
        self.ownerName.configure(bg="#e5e6d5")
        self.ownerName.configure(font=f2)
        self.ownerName.configure(state='disabled', disabledforeground="#043d10")
        
        self.mobilenoLabel = Label(self.root)
        self.mobilenoLabel.place(relx=0.265,rely=0.14)
        self.mobilenoLabel.configure(text="Mobile No")
        self.mobilenoLabel.configure(bg="#ad995e")
        self.mobilenoLabel.configure(font=f1)
        self.mobileno = Entry(self.root)
        self.mobileno.place(relx=0.265,rely=0.19)
        self.mobileno.configure(width=21)
        self.mobileno.configure(bg="#e5e6d5")
        self.mobileno.configure(font=f2)
        self.mobileno.configure(state='disabled', disabledforeground="#043d10")
        
        self.deleteButton = Button(self.root)
        self.deleteButton.place(relx=0.8,rely=0.14)
        self.deleteButton.configure(text="Delete")
        self.deleteButton.configure(font=f3)
        self.deleteButton.configure(width=11)
        self.deleteButton.configure(bg="#e5e6d5")
        self.deleteButton.configure(fg="black")
        self.deleteButton.configure(command=self.deletePartyaData)
        
        self.clearButton = Button(self.root)
        self.clearButton.place(relx=0.8,rely=0.23)
        self.clearButton.configure(text="Cancel")
        self.clearButton.configure(font=f3)
        self.clearButton.configure(width=11)
        self.clearButton.configure(bg="#e5e6d5")
        self.clearButton.configure(fg="black")
        self.clearButton.configure(command=self.clearall)

        self.scrollbarx = Scrollbar(self.root, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.02, rely=0.34, width=942, height=15)

        self.scrollbary = Scrollbar(self.root, orient=VERTICAL)
        self.scrollbary.place(relx=0.966, rely=0.35, width=18, height=310)

        self.tree = ttk.Treeview(self.root)
        self.tree.place(relx=0.02, rely=0.38, width=942, height=300)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.configure(command=self.tree.yview)
        
        self.tree.configure(
            columns=(
                "Party ID",
                "Party Name",
                "GSTIN No",
                "Location",
                "Owner Name",
                "Mobile No"
            )
        )

        self.tree.heading("Party ID", text="Party ID", anchor=W)
        self.tree.heading("Party Name", text="Party Name", anchor=W)
        self.tree.heading("GSTIN No", text="GSTIN No", anchor=W)
        self.tree.heading("Location", text="Location", anchor=W)
        self.tree.heading("Owner Name", text="Owner Name", anchor=W)
        self.tree.heading("Mobile No", text="Mobile No", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=90)
        self.tree.column("#2", stretch=NO, minwidth=0, width=175)
        self.tree.column("#3", stretch=NO, minwidth=0, width=170)
        self.tree.column("#4", stretch=NO, minwidth=0, width=170)
        self.tree.column("#5", stretch=NO, minwidth=0, width=175)
        self.tree.column("#6", stretch=NO, minwidth=0, width=160)
        self.tree.configure(selectmode="extended")
        self.tree.tag_configure("item", background="#fce89d", foreground="black",font=f4)
        self.tree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        self.addTreeData()
    
    def deletePartyaData(self):
        if self.partyId.get() != '':
            selected_item = self.tree.focus()
            responce = messagebox.askyesno("Responce","Are you sure you want to delete party.")
            if responce:
                if selected_item:
                    self.clearall()
                    data = self.tree.item(selected_item, "values")
                    mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
                    cursor = mydb.cursor()
                    query = "update partys set status = %s where partyid = %s"
                    cursor.execute(query,["del",data[0]])
                    mydb.commit()
                    self.addTreeData()  
            else:
                self.clearall()
        else:
            messagebox.showwarning("","Select Party from table.")
    
    def addTreeData(self):
        self.tree.delete(*self.tree.get_children())
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cursor = mydb.cursor()
        query = "select partyid,partyname,gstinno,location,ownername,mobileno from partys where status = %s"
        cursor.execute(query,["active"])
        data = cursor.fetchall()
        for item in data:
            row = (item[0],item[1],item[2],item[3],item[4],item[5])
            self.tree.insert("", "end", values=row,tags=("item",))
        mydb.commit()

    def onTreeSelect(self,event):
        selected_item = self.tree.focus()
        if selected_item:
            data = self.tree.item(selected_item, "values")
            self.partyId.configure(state='normal')
            self.partyName.configure(state='normal')
            self.gstInNo.configure(state='normal')
            self.location.configure(state='normal')
            self.ownerName.configure(state='normal')
            self.mobileno.configure(state='normal')
            
            self.partyId.delete(0,END)
            self.partyName.delete(0,END)
            self.gstInNo.delete(0,END)
            self.location.delete(0,END)
            self.ownerName.delete(0,END)
            self.mobileno.delete(0,END)
            
            self.partyId.insert(0,data[0])
            self.partyName.insert(0,data[1])
            self.gstInNo.insert(0,data[2])
            self.location.insert(0,data[3])
            self.ownerName.insert(0,data[4])
            self.mobileno.insert(0,data[5])
            
            self.partyId.configure(state='disabled')
            self.partyName.configure(state='disabled')
            self.gstInNo.configure(state='disabled')
            self.location.configure(state='disabled')
            self.ownerName.configure(state='disabled')
            self.mobileno.configure(state='disabled')

    def clearall(self):
            self.partyId.configure(state='normal')
            self.partyName.configure(state='normal')
            self.gstInNo.configure(state='normal')
            self.location.configure(state='normal')
            self.ownerName.configure(state='normal')
            self.mobileno.configure(state='normal')
            
            self.partyId.delete(0,END)
            self.partyName.delete(0,END)
            self.gstInNo.delete(0,END)
            self.location.delete(0,END)
            self.ownerName.delete(0,END)
            self.mobileno.delete(0,END)
            
            self.partyId.configure(state='disabled')
            self.partyName.configure(state='disabled')
            self.gstInNo.configure(state='disabled')
            self.location.configure(state='disabled')
            self.ownerName.configure(state='disabled')
            self.mobileno.configure(state='disabled')

