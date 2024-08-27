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


class AddProduct: 
    def __init__(self,canvas_widget):
        
        f1 = ("Times", 12)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 13)
        
        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.25,rely=0.18)
        self.root.configure(width=800,height=450)
        self.root.configure(bg="#ad995e")

        self.treeroot = Canvas(canvas_widget)
        self.treeroot.place(relx=0.165,rely=0.57)
        self.treeroot.configure(width=1050,height=500)
        self.treeroot.configure(bg="#ad995e")

        self.floatValidator = self.root.register(self.validateFloat)
        
        self.productDescriptionLabel = Label(self.root)
        self.productDescriptionLabel.place(relx=0.1,rely=0.02)
        self.productDescriptionLabel.configure(text="Product:")
        self.productDescriptionLabel.configure(bg="#ad995e")
        self.productDescriptionLabel.configure(font=f1)
        self.productDescription = Entry(self.root)
        self.productDescription.place(relx=0.1,rely=0.07)
        self.productDescription.configure(width=30)
        self.productDescription.configure(bg="#e5e6d5")
        self.productDescription.configure(font=f2)
        self.productDescription.configure(state='disabled', disabledforeground="#043d10")
        
        self.productNameLabel = Label(self.root)
        self.productNameLabel.place(relx=0.55,rely=0.02)
        self.productNameLabel.configure(text="Product Name:")
        self.productNameLabel.configure(bg="#ad995e")
        self.productNameLabel.configure(font=f1)
        self.productName = Entry(self.root)
        self.productName.place(relx=0.55,rely=0.07)
        self.productName.configure(width=30)
        self.productName.configure(bg="#e5e6d5")
        self.productName.configure(font=f2)

        self.manufacturerLabel = Label(self.root)
        self.manufacturerLabel.place(relx=0.1,rely=0.15)
        self.manufacturerLabel.configure(text="Manufacturer:")
        self.manufacturerLabel.configure(bg="#ad995e")
        self.manufacturerLabel.configure(font=f1)
        self.manufacturer = Entry(self.root)
        self.manufacturer.place(relx=0.1,rely=0.2)
        self.manufacturer.configure(width=30)
        self.manufacturer.configure(bg="#e5e6d5")
        self.manufacturer.configure(font=f2)
        
        self.productPackingLabel = Label(self.root)
        self.productPackingLabel.place(relx=0.55,rely=0.15)
        self.productPackingLabel.configure(text="Packing Type:")
        self.productPackingLabel.configure(bg="#ad995e")
        self.productPackingLabel.configure(font=f1)
        self.productPacking = ttk.Combobox(self.root)  
        self.productPacking.place(relx=0.55, rely=0.2) 
        self.productPacking['values'] = ('Other', 'Box', 'Bottel', 'Bag', 'Packate')
        self.productPacking.current(0)
        self.productPacking.configure(state='readonly')
        self.productPacking.configure(width=28)
        self.productPacking.configure(font=f2)

        self.productTypeLabel = Label(self.root)
        self.productTypeLabel.place(relx=0.1,rely=0.28)
        self.productTypeLabel.configure(text="Product Type:")
        self.productTypeLabel.configure(bg="#ad995e")
        self.productTypeLabel.configure(font=f1)
        self.productType = ttk.Combobox(self.root)  
        self.productType.place(relx=0.1, rely=0.33) 
        self.productType['values'] = ('Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.productType.current(0)
        self.productType.configure(state='readonly')
        self.productType.configure(width=28)
        self.productType.configure(font=f2)

        self.productWeightLabel = Label(self.root)
        self.productWeightLabel.place(relx=0.55,rely=0.28)
        self.productWeightLabel.configure(text="Weight:")
        self.productWeightLabel.configure(bg="#ad995e")
        self.productWeightLabel.configure(font=f1)
        self.productWeight = Entry(self.root)
        self.productWeight.place(relx=0.55,rely=0.33)
        self.productWeight.configure(width=15)
        self.productWeight.configure(bg="#e5e6d5")
        self.productWeight.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        self.productWeight.configure(font=f2)

        self.productWeightUnitLabel = Label(self.root)
        self.productWeightUnitLabel.place(relx=0.775,rely=0.28)
        self.productWeightUnitLabel.configure(text="Unit:")
        self.productWeightUnitLabel.configure(bg="#ad995e")
        self.productWeightUnitLabel.configure(font=f1)
        self.productWeightUnit = ttk.Combobox(self.root)  
        self.productWeightUnit.place(relx=0.775, rely=0.33) 
        self.productWeightUnit['values'] = ('kg', 'gm', 'lit', 'ml')
        self.productWeightUnit.current(0)
        self.productWeightUnit.configure(width=10)
        self.productWeightUnit.configure(font=f2)
        

        self.productgstLabel = Label(self.root)
        self.productgstLabel.place(relx=0.1,rely=0.41)
        self.productgstLabel.configure(text="GST in %:")
        self.productgstLabel.configure(bg="#ad995e")
        self.productgstLabel.configure(font=f1)
        self.productgst = Entry(self.root)
        self.productgst.place(relx=0.1,rely=0.46)
        self.productgst.configure(width=12)
        self.productgst.configure(bg="#e5e6d5")
        self.productgst.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        self.productgst.configure(font=f2)
        
        self.sellingpriceLabel = Label(self.root)
        self.sellingpriceLabel.place(relx=0.32,rely=0.41)
        self.sellingpriceLabel.configure(text="Selling Price:")
        self.sellingpriceLabel.configure(bg="#ad995e")
        self.sellingpriceLabel.configure(font=f1)
        self.sellingprice = Entry(self.root)
        self.sellingprice.place(relx=0.32,rely=0.46)
        self.sellingprice.configure(width=12)
        self.sellingprice.configure(bg="#e5e6d5")
        self.sellingprice.configure(validate="key", validatecommand=(self.floatValidator, "%P", "%d"))
        self.sellingprice.configure(font=f2)
        

        self.scrollbarx = Scrollbar(self.treeroot, orient=HORIZONTAL)
        self.scrollbarx.place(relx=0.01, rely=0.01, width=1000, height=15)

        self.scrollbary = Scrollbar(self.treeroot, orient=VERTICAL)
        self.scrollbary.place(relx=0.968, rely=0.01, width=18, height=260)

        self.tree = ttk.Treeview(self.treeroot)
        self.tree.place(relx=0.01, rely=0.05, width=1000, height=250)
        self.tree.configure(yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbary.configure(command=self.tree.yview)
        
        self.tree.configure(
            columns=(
                "Item ID",
                "Product Name",
                "Manufacturer",
                "Weight",
                "Unit",
                "GST in %",
                "SL Price",
                "Category",
                "Packing",
                "Description"
            )
        )

        self.tree.heading("Item ID", text="Item ID", anchor=W)
        self.tree.heading("Product Name", text="Product Name", anchor=W)
        self.tree.heading("Manufacturer", text="Manufacturer", anchor=W)
        self.tree.heading("Weight", text="Weight", anchor=W)
        self.tree.heading("Unit", text="Unit", anchor=W)
        self.tree.heading("GST in %", text="GST in %", anchor=W)
        self.tree.heading("SL Price", text="SL Price", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Packing", text="Packing", anchor=W)
        self.tree.heading("Description", text="Description", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=80)
        self.tree.column("#2", stretch=NO, minwidth=0, width=150)
        self.tree.column("#3", stretch=NO, minwidth=0, width=110)
        self.tree.column("#4", stretch=NO, minwidth=0, width=110)
        self.tree.column("#5", stretch=NO, minwidth=0, width=110)
        self.tree.column("#6", stretch=NO, minwidth=0, width=110)
        self.tree.column("#7", stretch=NO, minwidth=0, width=110)
        self.tree.column("#8", stretch=NO, minwidth=0, width=110)
        self.tree.column("#9", stretch=NO, minwidth=0, width=110)
        self.tree.column("#10", stretch=NO, minwidth=0, width=160)
        self.tree.configure(selectmode="extended")
        self.tree.tag_configure("item", background="#fce89d", foreground="black")
        self.tree.bind("<<TreeviewSelect>>", self.onTreeSelect)
        self.addTreeData()
        
        self.addProducdButton = Button(self.root, height=1)
        self.addProducdButton.place(relx=0.1,rely=0.56)
        self.addProducdButton.configure(text="Add")
        self.addProducdButton.configure(font=f1)
        self.addProducdButton.configure(width=12)
        self.addProducdButton.configure(activebackground="#ad995e")
        self.addProducdButton.configure(bg="#e0cb8d")
        self.addProducdButton.configure(command=self.addToDatabase)

        self.modifyButton = Button(self.root, height=1)
        self.modifyButton.place(relx=0.35,rely=0.56)
        self.modifyButton.configure(text="Modify")
        self.modifyButton.configure(font=f1)
        self.modifyButton.configure(width=12)
        self.modifyButton.configure(activebackground="#ad995e")
        self.modifyButton.configure(bg="#e0cb8d")
        self.modifyButton.configure(command=self.modifyTreeData)

        self.updateButton = Button(self.root)
        self.updateButton.place(relx=0.55,rely=0.56)
        self.updateButton.configure(text="Update")
        self.updateButton.configure(font=f1)
        self.updateButton.configure(width=12)
        self.updateButton.configure(activebackground="#ad995e")
        self.updateButton.configure(bg="#e0cb8d")
        self.updateButton.configure(command=self.updatedata)
        

        self.clearButton = Button(self.root)
        self.clearButton.place(relx=0.785,rely=0.56)
        self.clearButton.configure(text="New")
        self.clearButton.configure(font=f1)
        self.clearButton.configure(width=12)
        self.clearButton.configure(activebackground="#ad995e")
        self.clearButton.configure(bg="#e0cb8d")
        self.clearButton.configure(command=self.clearall)

    def updatedata(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        
        pName = self.productName.get()
        manufact = self.manufacturer.get()
        pType = self.productType.get()
        # pGst = self.productgst.get()
        sprice = self.sellingprice.get()
        pDescription = self.productDescription.get()
        query = ("update product set selling_price = %s where product_name = %s and manufacturer = %s and product_category = %s")
        cur.execute(query,[sprice,pName,manufact,pType])
        query2 = "update purchase set sellingprice = %s where productname = %s"
        cur.execute(query2,[sprice,pDescription])
        mydb.commit()  
        self.productDescription.configure(state='normal')
        self.productDescription.delete(0,END)
        self.productDescription.insert(0,pDescription)
        self.productDescription.configure(state='disabled')
        self.productName.configure(state='disabled')
        self.manufacturer.configure(state='disabled')
        self.productPacking.configure(state='disabled')
        self.productType.configure(state='disabled')
        self.productWeight.configure(state='disabled')
        self.productWeightUnit.configure(state='disabled')
        self.productgst.configure(state='disabled')
        self.sellingprice.configure(state='disabled')                      
        self.addTreeData()    
        messagebox.showinfo("Success!!", "Product successfully Updated.", parent=self.root)

    def modifyTreeData(self):
        selected_item = self.tree.focus()
        if selected_item:
            self.sellingprice.configure(state='normal')

    def addTreeData(self):
        self.tree.delete(*self.tree.get_children())
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cursor = mydb.cursor()
        query = "select product_id,product_name,manufacturer,product_weight,weight_unit,product_gst,selling_price,product_category,product_packing,product_description from product where status = %s"
        cursor.execute(query,["active"])
        data = cursor.fetchall()
        for item in data:
            row = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9])
            self.tree.insert("", "end", values=row,tags=("item",))
        mydb.commit()

    def validateFloat(self, value, action_type):
        if action_type == '1':
            try:
                float(value)
                return True
            except ValueError:
                return False
        return True
       
    def addToDatabase(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        
        self.pName = self.productName.get()
        self.manufact = self.manufacturer.get()
        self.pType = self.productType.get()
        self.pWeight = self.productWeight.get()
        self.pWeightUnit = self.productWeightUnit.get()
        self.pPacking = self.productPacking.get()
        self.pGst = self.productgst.get()
        sprice = self.sellingprice.get()

        if self.pName.strip():
            if self.manufact.strip():
                if self.pType.strip():
                    if self.pWeight.strip():
                        if self.pWeightUnit.strip():
                            if self.pPacking.strip():
                                self.weightUnit = self.pWeight + self.pWeightUnit
                                self.pDescription = self.pName+" "+self.weightUnit+" "+self.manufact
                                query = ("INSERT INTO product(product_id, product_name, manufacturer, product_weight_unit, product_category, product_packing, product_gst, product_weight, weight_unit, product_description,selling_price,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                                cur.execute(query,[None, self.pName, self.manufact, self.weightUnit, self.pType, self.pPacking, self.pGst, self.pWeight,self.pWeightUnit,self.pDescription,sprice,"active"])
                                # self.clearall()
                                mydb.commit()  
                                self.productDescription.configure(state='normal')
                                self.productDescription.delete(0,END)
                                self.productDescription.insert(0,self.pDescription)
                                self.productDescription.configure(state='disabled')
                                self.productName.configure(state='disabled')
                                self.manufacturer.configure(state='disabled')
                                self.productPacking.configure(state='disabled')
                                self.productType.configure(state='disabled')
                                self.productWeight.configure(state='disabled')
                                self.productWeightUnit.configure(state='disabled')
                                self.productgst.configure(state='disabled')
                                self.sellingprice.configure(state='disabled')                          
                                messagebox.showinfo("Success!!", "Product successfully added.", parent=self.root)
                                self.addTreeData()

                            else:
                                messagebox.showerror("Oops!", "Please select product Packing.", parent=self.root)
                        else:
                            messagebox.showerror("Oops!", "Please select product Weight Unit.", parent=self.root)
                    else:
                        messagebox.showerror("Oops!", "Please enter product Weight.", parent=self.root)
                else:
                    messagebox.showerror("Oops!", "Please select product category.", parent=self.root)
            else:
                messagebox.showerror("Oops!", "Please enter product manufacturer.", parent=self.root)
        else:
            messagebox.showerror("Oops!", "Please enter product name.", parent=self.root) 

    def onTreeSelect(self,event):
        selected_item = self.tree.focus()
        if selected_item:
            self.clearall()
            self.addProducdButton.configure(state='disabled')
            data = self.tree.item(selected_item, "values")
            self.productDescription.configure(state='normal')
            self.productDescription.delete(0,END)
            self.productDescription.insert(0,data[9])
            self.productDescription.configure(state='disabled')
            self.productType.configure(state='normal')
            self.productPacking.configure(state='normal')
            self.productType.delete(0, END)
            self.productPacking.delete(0, END)
            self.productWeightUnit.configure(state='normal')
            self.productWeightUnit.delete(0, END)
            self.productName.insert(0, data[1])
            self.manufacturer.insert(0, data[2])
            self.productType.insert(0, data[7])
            self.productWeight.insert(0, data[3])
            self.productWeightUnit.insert(0, data[4])
            self.productPacking.insert(0, data[8])
            self.productgst.insert(0, data[5])
            self.sellingprice.insert(0, data[6])
            self.productType.configure(state='disabled')
            self.productPacking.configure(state='disabled')
            self.productWeightUnit.configure(state='disabled')
            self.productName.configure(state='disabled')
            self.sellingprice.configure(state='disabled')
            self.productgst.configure(state='disabled')
            self.manufacturer.configure(state='disabled')
            self.productWeight.configure(state='disabled')

    def clearall(self):
            self.addProducdButton.configure(state='normal')
            self.productDescription.configure(state='normal')
            self.productDescription.delete(0,END)
            self.productDescription.configure(state='disabled')
            self.productName.configure(state='normal')
            self.manufacturer.configure(state='normal')
            self.productWeight.configure(state='normal')
            self.productgst.configure(state='normal')
            self.sellingprice.configure(state='normal') 
            self.productPacking.configure(state='normal')
            self.productType.configure(state='normal')
            self.productWeightUnit.configure(state='normal')
            self.productName.delete(0, END)
            self.manufacturer.delete(0, END)
            self.productType.delete(0, END)
            self.productWeight.delete(0, END)
            self.productWeightUnit.delete(0, END)
            self.productPacking.delete(0, END)
            self.productgst.delete(0, END)
            self.sellingprice.delete(0, END)
            self.productPacking.configure(state='readonly')
            self.productType.configure(state='readonly')
            self.productWeightUnit.configure(state='readonly')

class DeleteProduct:
    def __init__(self,canvas_widget):

        f1 = ("Times", 12)
        f2 = ("Courier New", 12)
        f3 = ("Arial Black", 14)
        self.rowForDelete = 0
        
        self.root = Canvas(canvas_widget)
        self.root.place(relx=0.35,rely=0.2)
        self.root.configure(width=400,height=500)
        self.root.configure(bg="#ad995e")

        self.productNameLabel = Label(self.root)
        self.productNameLabel.place(relx=0.1,rely=0.02)
        self.productNameLabel.configure(text="Product Name:")
        self.productNameLabel.configure(bg="#ad995e")
        self.productNameLabel.configure(font=f1)

        self.productName = Entry(self.root)
        self.productName.place(relx=0.1,rely=0.07)
        self.productName.configure(width=30)
        self.productName.configure(bg="#e5e6d5")
        self.productName.configure(font=f2)

        self.manufacturerLabel = Label(self.root)
        self.manufacturerLabel.place(relx=0.1,rely=0.15)
        self.manufacturerLabel.configure(text="Manufacturer:")
        self.manufacturerLabel.configure(bg="#ad995e")
        self.manufacturerLabel.configure(font=f1)

        self.manufacturer = Entry(self.root)
        self.manufacturer.place(relx=0.1,rely=0.2)
        self.manufacturer.configure(width=30)
        self.manufacturer.configure(bg="#e5e6d5")
        self.manufacturer.configure(font=f2)

        self.productTypeLabel = Label(self.root)
        self.productTypeLabel.place(relx=0.1,rely=0.28)
        self.productTypeLabel.configure(text="Product Type:")
        self.productTypeLabel.configure(bg="#ad995e")
        self.productTypeLabel.configure(font=f1)

        self.productType = ttk.Combobox(self.root)  
        self.productType.place(relx=0.1, rely=0.33) 
        self.productType['values'] = ('Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.productType.current(0)
        self.productType.configure(width=28)
        self.productType.configure(font=f2)

        self.productWeightLabel = Label(self.root)
        self.productWeightLabel.place(relx=0.1,rely=0.41)
        self.productWeightLabel.configure(text="Weight:")
        self.productWeightLabel.configure(bg="#ad995e")
        self.productWeightLabel.configure(font=f1)

        self.productWeight = Entry(self.root)
        self.productWeight.place(relx=0.1,rely=0.46)
        self.productWeight.configure(width=15)
        self.productWeight.configure(bg="#e5e6d5")
        self.productWeight.configure(font=f2)

        self.productWeightLabel = Label(self.root)
        self.productWeightLabel.place(relx=0.55,rely=0.41)
        self.productWeightLabel.configure(text="Unit:")
        self.productWeightLabel.configure(bg="#ad995e")
        self.productWeightLabel.configure(font=f1)

        self.productWeightUnit = ttk.Combobox(self.root)  
        self.productWeightUnit.place(relx=0.55, rely=0.46) 
        self.productWeightUnit['values'] = ('kg', 'gm', 'lit', 'ml')
        self.productWeightUnit.current(0)
        self.productWeightUnit.configure(width=10)
        self.productWeightUnit.configure(font=f2)
        
        self.productPackingLabel = Label(self.root)
        self.productPackingLabel.place(relx=0.1,rely=0.54)
        self.productPackingLabel.configure(text="Packing Type:")
        self.productPackingLabel.configure(bg="#ad995e")
        self.productPackingLabel.configure(font=f1)
        
        self.productPacking = ttk.Combobox(self.root)  
        self.productPacking.place(relx=0.1, rely=0.59) 
        self.productPacking['values'] = ('Other', 'Box', 'Bottel', 'Bag', 'Packate')
        self.productPacking.current(0)
        self.productPacking.configure(width=28)
        self.productPacking.configure(font=f2)

        self.productgstLabel = Label(self.root)
        self.productgstLabel.place(relx=0.1,rely=0.67)
        self.productgstLabel.configure(text="GST in %:")
        self.productgstLabel.configure(bg="#ad995e")
        self.productgstLabel.configure(font=f1)

        self.productgst = Entry(self.root)
        self.productgst.place(relx=0.1,rely=0.72)
        self.productgst.configure(width=30)
        self.productgst.configure(bg="#e5e6d5")
        self.productgst.configure(font=f2)

        self.deleteButton = Button(self.root)
        self.deleteButton.place(relx=0.1,rely=0.82)
        self.deleteButton.configure(text="Delete")
        self.deleteButton.configure(font=f3)
        self.deleteButton.configure(width=11)
        self.deleteButton.configure(bg="#e5e6d5")
        self.deleteButton.configure(fg="#6e5a20")
        self.deleteButton.configure(command=self.deleteProduct)
        
        self.cancelButton = Button(self.root)
        self.cancelButton.place(relx=0.55,rely=0.82)
        self.cancelButton.configure(text="Cancel")
        self.cancelButton.configure(font=f3)
        self.cancelButton.configure(width=11)
        self.cancelButton.configure(bg="#e5e6d5")
        self.cancelButton.configure(fg="#6e5a20")
        self.cancelButton.configure(command=self.clearall)

        self.productListLabel = Label(canvas_widget)
        self.productListLabel.place(relx=0.65,rely=0.2)
        self.productListLabel.configure(text="Product List")
        self.productListLabel.configure(bg="#e5e6d5")
        self.productListLabel.configure(fg="#6e5a20")
        self.productListLabel.configure(font=f3)

        self.productList = Listbox(canvas_widget)
        self.productList.place(relx=0.65, rely=0.24)
        self.productList.configure(bg="#e5e6d5")
        self.productList.configure(font=f2)
        self.productList.configure(height=24)
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        query = "select product_description from product where status = %s"
        cur.execute(query,["active"])
        items = cur.fetchall()
        for item in items:
            self.productList.insert(END, item[0])
        self.productList.bind("<<ListboxSelect>>", self.on_select)
        mydb.commit()
    
    def on_select(self,event):
        self.clearall()
        self.selected_index = self.productList.curselection()
        if self.selected_index:
            selected_item = self.productList.get(self.selected_index[0])
            # print(selected_item)
            mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
            cur = mydb.cursor()
            query = "SELECT * FROM product WHERE product_description = %s"
            cur.execute(query,[selected_item])
            data = cur.fetchall()
            self.rowForDelete = data[0][0]
            self.productName.insert(0, data[0][1])
            self.manufacturer.insert(0, data[0][2])
            self.productType.insert(0, data[0][4])
            self.productWeight.insert(0, data[0][7])
            self.productWeightUnit.insert(0, data[0][8])
            self.productPacking.insert(0, data[0][5])
            self.productgst.insert(0, data[0][6])
            mydb.commit()

    def clearall(self):
        self.productName.delete(0, END)
        self.manufacturer.delete(0, END)
        self.productType.delete(0, END)
        self.productWeight.delete(0, END)
        self.productWeightUnit.delete(0, END)
        self.productPacking.delete(0, END)
        self.productgst.delete(0, END)
    
    def deleteProduct(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
        cur = mydb.cursor()
        # print(responce)
        if self.rowForDelete > 0:
            responce = messagebox.askokcancel("Responce","You want to delete product.", parent=self.root)
            if responce:
                query = "update product set status = %s WHERE product_id = %s"
                cur.execute(query,["del",self.rowForDelete])
                self.clearall()
                messagebox.showinfo("Success!!", "Product delete successfully.", parent=self.root)
        else:
            messagebox.showwarning("Warning","Select product from list to delete", parent=self.root)
        mydb.commit()