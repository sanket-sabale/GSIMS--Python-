# ==================imports===================
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
import mysql.connector
# ============================================

root = Tk()
root.geometry("1920x1080+0+0")
root.title("Retail Manager(ADMIN)")

user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()

def random_emp_id(stringLength):
    Digits = string.digits
    strr=''.join(random.choice(Digits) for i in range(stringLength-3))
    return ('EMP'+strr)

def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def valid_aadhar(aad):
    if aad.isdigit() and len(aad)==12:
        return True
    return False

class login_page:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Retail Manager(ADMIN)")

        canvas_widget = Canvas(root, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')

        frame = Frame(canvas_widget, width=400, height=300)
        
        self.labal1 = Label(frame)
        self.labal1.pack()
        self.labal1.configure(text="User name")
        self.labal1.configure(bg="#36919c")

        self.entry1 = Entry(frame)
        self.entry1.pack(pady=15, padx=30)
        self.entry1.configure(width=25)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#b6dde3")
        self.entry1.configure(textvariable=user)

        self.labal2 = Label(frame)  
        self.labal2.pack()
        self.labal2.configure(text="password")
        self.labal2.configure(bg="#36919c")

        self.entry2 = Entry(frame)
        self.entry2.pack(pady=15, padx=30)
        self.entry2.configure(width=25)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        self.entry2.configure(bg="#b6dde3")
        self.entry2.configure(textvariable=passwd)
        
        self.button1 = Button(frame)
        self.button1.pack(padx=150, pady=70)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#D2463E")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#dbe7ff")
        self.button1.configure(background="#285269")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="1")
        self.button1.configure(text="""LOGIN""")
        self.button1.configure(width=11, height=1)
        self.button1.configure(command=self.login)
        
        frame.pack(pady=100)
        frame.configure(bg="#36919c")

    def login(self, Event=None):
        # messagebox.showinfo("Login Page", "The login is successful.")
        # page1.entry1.delete(0, END)
        # page1.entry2.delete(0, END)
        # root.withdraw()
        # global adm
        # global page2
        # adm = Toplevel()
        # page2 = Inventory_Page(adm)
        # adm.protocol("WM_DELETE_WINDOW", exitt)
        # adm.mainloop()
        username = user.get()
        password = passwd.get()
        if username and password:
            if username == "Admin" and password == "123":
                messagebox.showinfo("Login Page", "The login is successful.")
                page1.entry1.delete(0, END)
                page1.entry2.delete(0, END)

                root.withdraw()
                global adm
                global page2
                adm = Toplevel()
                page2 = Inventory_Page(adm)
                adm.protocol("WM_DELETE_WINDOW", exitt)
                adm.mainloop()
            else:
                messagebox.showerror("Oops!!", "You are not an admin.")

        else:
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)
   
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        adm.destroy()
        root.destroy()

def stockInventory():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = Stock(inv)
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()

def puchaseInventory():
    adm.withdraw()
    global purchas
    global page5
    purchas = Toplevel()
    page5 = Purchase(purchas)
    purchas.protocol("WM_DELETE_WINDOW", exitt)
    purchas.mainloop()

def invoices():
    adm.withdraw()
    global invoice
    invoice = Toplevel()
    page7 = Invoice(invoice)
    invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def about():
    pass


class Inventory_Page:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("INVENTORY Mode")

        canvas_widget = Canvas(adm, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')

        
        f2=("Arial Black", 15)
        f3=("Times", 20)
                
        self.message = Label(adm)
        self.message.place(relx=0.046, rely=0.056, width=100, height=30)
        self.message.configure(font=f3)
        self.message.configure(foreground="#112240")
        self.message.configure(background="#97dbd6")
        self.message.configure(text="ADMIN")
        self.message.configure(anchor="center")

        self.button1 = Button(adm)
        self.button1.place(relx=0.046, rely=0.106, width=100, height=30)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#CF1E14")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)
        self.button2.place(relx=0.14, rely=0.480, width=146, height=63)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(bg='#112240')
        self.button2.configure(fg='#97dbd6')
        self.button2.configure(font= f2)
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Stock Book""")
        self.button2.configure(command=stockInventory)

        self.button3 = Button(adm)
        self.button3.place(relx=0.338, rely=0.480, width=170, height=63)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(bg='#112240')
        self.button3.configure(fg='#97dbd6')
        self.button3.configure(font= f2)
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Purchase Book""")
        self.button3.configure(command=puchaseInventory)


        self.button4 = Button(adm)
        self.button4.place(relx=0.536, rely=0.480, width=146, height=63)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(bg='#112240')
        self.button4.configure(fg='#97dbd6')
        self.button4.configure(font= f2)
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Sale Book""")
        self.button4.configure(command=invoices)


        self.button5 = Button(adm)
        self.button5.place(relx=0.732, rely=0.480, width=146, height=63)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(bg='#112240')
        self.button5.configure(fg='#97dbd6')
        self.button5.configure(font= f2)
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""EXP Product""")
        self.button5.configure(command=about)
        
        # two lines
        # self.message1 = Label(adm)
        # self.message1.place(rely=0.490, width=1700, height=10)
        # self.message1.configure(bg='#112240')
        # self.message2 = Label(adm)
        # self.message2.place(rely=0.539, width=1700, height=10)
        # self.message2.configure(bg='#112240')

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=adm)
        if sure == True:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class Stock:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Stock Book")
             
        canvas_widget = Canvas(inv, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')

        frame = Frame(canvas_widget, width=550, height=550)
        frame.place(relx=0.013, rely=0.203)
        frame.configure(bg="#36919c")

        self.entry1 = Entry(inv)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#d5dbdb")

        self.button1 = Button(inv)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_product)

        self.button6 = Button(inv)
        self.button6.place(relx=0.900, rely=0.106, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#990f0f")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.button3 = Button(inv)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#033145")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""ADD PRODUCT""")
        self.button3.configure(command=self.add_product)

        self.button5 = Button(inv)
        self.button5.place(relx=0.052, rely=0.57, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#033145")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE PRODUCT""")
        self.button5.configure(command=self.delete_product)


        self.scrollbarx = Scrollbar(inv, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(inv, orient=VERTICAL)
        self.tree = ttk.Treeview(inv)
        self.tree.place(relx=0.320, rely=0.203, width=950, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.940, rely=0.203, width=15, height=548)
        self.scrollbarx.place(relx=0.325, rely=0.181, width=940, height=15)

        self.tree.configure(
            columns=(
                "Id",
                "Name",
                "Quantity",
                "Manufacturer",
                "Weight",
                "Exp Date",
                "Category",
                "Discription"
            )
        )

        self.tree.heading("Id", text="Id", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Manufacturer", text="Manufacturer", anchor=W)
        self.tree.heading("Weight", text="Weight", anchor=W)
        self.tree.heading("Exp Date", text="Exp Date", anchor=W)
        self.tree.heading("Category", text="Category", anchor=W)
        self.tree.heading("Discription", text="Discription", anchor=W)


        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=60)
        self.tree.column("#2", stretch=NO, minwidth=0, width=180)
        self.tree.column("#3", stretch=NO, minwidth=0, width=100)
        self.tree.column("#4", stretch=NO, minwidth=0, width=120)
        self.tree.column("#5", stretch=NO, minwidth=0, width=80)
        self.tree.column("#6", stretch=NO, minwidth=0, width=80)
        self.tree.column("#7", stretch=NO, minwidth=0, width=110)
        self.tree.column("#8", stretch=NO, minwidth=0, width=300)


        self.DisplayData()

    def DisplayData(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute("SELECT * FROM stock")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))

    def search_product(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        try:
            to_search = int(self.entry1.get())
        except ValueError:
            messagebox.showerror("Oops!!", "Invalid Product Id.", parent=inv)
        else:
            for search in val:
                if search==to_search:
                    self.tree.selection_set(val[val.index(search)-1])
                    self.tree.focus(val[val.index(search)-1])
                    break
            else: 
                messagebox.showerror("Oops!!", "Product ID: {} not found.".format(self.entry1.get()), parent=inv)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)
        # print(self.sel)

    def delete_product(self):
        val = []
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected products?", parent=inv)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                                
                # print("val[0] TYPE = ",type(val[0]))   
                # print("val TYPE = ",type(val))
                       
                print("val[0]  = '",val[0],"'")   
                # print("val  = ",val)
                delete = f"DELETE FROM stock WHERE product_id = {val[0]}"
                cur.execute(delete)
                mydb.commit()

                messagebox.showinfo("Success!!", "Products deleted from database.", parent=inv)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select a product.", parent=inv)
        
    def add_product(self):
        global p_add
        global page4
        p_add = Toplevel()
        page4 = add_product(p_add)
        p_add.mainloop()

    def Exit(self):
            inv.destroy()
            adm.deiconify()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class add_product:
    def __init__(self, top=None):
        top.geometry("434x610+550+120")
        top.resizable(0, 0)
        top.title("Add Product")

        canvas_widget = Canvas(p_add, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg="#36919c")
        
        self.entry1 = Entry(p_add) # product_name
        self.entry1.place(relx=0.07, rely=0.14, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#edfbff")

        self.label1 = Label(p_add)
        self.label1.place(relx=0.07, rely=0.08)
        self.label1.configure(text="Product Name: ")
        self.label1.configure(bg="#36919c")

        self.entry2 = Entry(p_add) # Manufacturer
        self.entry2.place(relx=0.07, rely=0.285, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(bg="#edfbff")

        self.label2 = Label(p_add)
        self.label2.place(relx=0.07, rely=0.235)
        self.label2.configure(text="Manufacturer: ")
        self.label2.configure(bg="#36919c")

        self.r2 = p_add.register(self.testint)

        self.entry3 = Entry(p_add) # Product Weight
        self.entry3.place(relx=0.07, rely=0.421, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(bg="#edfbff")

        self.label3 = Label(p_add)
        self.label3.place(relx=0.07, rely=0.370)
        self.label3.configure(text="Product Weight: ")
        self.label3.configure(bg="#36919c") 

        self.entry4 = ttk.Combobox(p_add)  
        self.entry4.place(relx=0.07, rely=0.555, width=374, height=30) 
        self.entry4['values'] = ('Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.entry4.current(1)
        
        self.label4 = Label(p_add)
        self.label4.place(relx=0.07, rely=0.505)
        self.label4.configure(text="Categeory: ")
        self.label4.configure(bg="#36919c")

        self.button1 = Button(p_add)
        self.button1.place(relx=0.2, rely=0.786, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(relx=0.526, rely=0.786, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#033145")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def add(self):
        pname = self.entry1.get()
        manufacturer = self.entry2.get()
        weight = self.entry3.get() 
        pcategeory = self.entry4.get()        

        if pname.strip():
            if manufacturer.strip():
                if weight:
                    disc = f"{pname}_{weight}_{manufacturer}"
                    mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                    cur = mydb.cursor()
                    insert = (
                                "INSERT INTO stock(product_id, product_name, product_quantity,manufacturer,product_weight,product_expdate, category, description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                            )
                    cur.execute(insert, [None, pname, 0, manufacturer, weight, None, pcategeory, disc])
                    mydb.commit()
                    messagebox.showinfo("Success!!", "Product successfully added in inventory.", parent=p_add)
                    p_add.destroy()
                    page3.tree.delete(*page3.tree.get_children())
                    page3.DisplayData()
                    p_add.destroy()

                    print(pname, " ", manufacturer, " ", weight, " ", pcategeory )
                                   
                else:
                    messagebox.showerror("Oops!", "Please enter product quantity.", parent=p_add)    
            else:
                messagebox.showerror("Oops!", "Please enter product category.", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Please enter product name", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry4.delete(0, END)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


class Purchase:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Purchase Book")

        canvas_widget = Canvas(purchas, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')
        
        frame = Frame(canvas_widget, width=600, height=550)
        frame.place(relx=0.01, rely=0.203)
        frame.configure(bg="#36919c")
        
        self.entry1 = Entry(purchas)
        self.entry1.place(relx=0.040, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(bg="#d5dbdb")

        self.button1 = Button(purchas)
        self.button1.place(relx=0.229, rely=0.289, width=76, height=23)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 10")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_purchase)

        self.button3 = Button(purchas)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=28)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#033145")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""PURCHASE ENTRY""")
        self.button3.configure(command=self.purchase_entry)

        self.button4 = Button(purchas)
        self.button4.place(relx=0.052, rely=0.51, width=306, height=28)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#033145")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE ENTRY""")
        self.button4.configure(command=self.update_purchase)

        self.button5 = Button(purchas)
        self.button5.place(relx=0.052, rely=0.59, width=306, height=28)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#033145")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""DELETE ENTRY""")
        self.button5.configure(command=self.delete_purchase)

        self.button6 = Button(purchas)
        self.button6.place(relx=0.900, rely=0.106, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#990f0f")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(purchas, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(purchas, orient=VERTICAL)

        self.tree = ttk.Treeview(purchas)
        self.tree.place(relx=0.320, rely=0.203, width=965, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=548)
        self.scrollbarx.place(relx=0.325, rely=0.181, width=960, height=15)

        self.tree.configure(
            columns=(
                "Id",
                "Bill_no",
                "Supplier",
                "Product ID",
                "Product name",
                "Quantity",
                "Cost price",
                "Selling price",
                "Purchase Date",
                "Exp Date",
                "Avl Quantity"
            )
        )

        self.tree.heading("Id", text="Id", anchor=W)
        self.tree.heading("Bill_no", text="Bill_no", anchor=W)
        self.tree.heading("Supplier", text="Supplier", anchor=W)
        self.tree.heading("Product ID", text="Product ID", anchor=W)
        self.tree.heading("Product name", text="Product name", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Cost price", text="Cost price", anchor=W)
        self.tree.heading("Selling price", text="Selling price", anchor=W)
        self.tree.heading("Purchase Date", text="Purchase Date", anchor=W)
        self.tree.heading("Exp Date", text="Exp Date", anchor=W)
        self.tree.heading("Avl Quantity", text="Avl Quantity", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=70)
        self.tree.column("#2", stretch=NO, minwidth=0, width=80)
        self.tree.column("#3", stretch=NO, minwidth=0, width=130)
        self.tree.column("#4", stretch=NO, minwidth=0, width=100)
        self.tree.column("#5", stretch=NO, minwidth=0, width=160)
        self.tree.column("#6", stretch=NO, minwidth=0, width=100)
        self.tree.column("#7", stretch=NO, minwidth=0, width=100)
        self.tree.column("#8", stretch=NO, minwidth=0, width=110)
        self.tree.column("#9", stretch=NO, minwidth=0, width=120)
        self.tree.column("#10", stretch=NO, minwidth=0, width=120)
        self.tree.column("#11", stretch=NO, minwidth=0, width=120)

        self.DisplayData()

    def DisplayData(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute("SELECT * FROM purchase")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))
        

    def search_purchase(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            if search==int(to_search):
                self.tree.selection_set(val[val.index(search)-1])
                self.tree.focus(val[val.index(search)-1])
                messagebox.showinfo("Success!!", "Purchase ID: {} found.".format(self.entry1.get()), parent=purchas)
                break
        else: 
            messagebox.showerror("Oops!!", "Purchase ID: {} not found.".format(self.entry1.get()), parent=purchas)
    
    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def delete_purchase(self):
        val = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected entry?", parent=purchas)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                cur = mydb.cursor()

                productid = val[3]
                purchasid = val[0]
                quant = val[5]

                select = "SELECT product_quantity FROM stock WHERE product_id = %s"
                cur.execute(select,[productid])
                result1 = cur.fetchall()
                stockquantity = result1[0][0]
                stockquantity = stockquantity - quant
                if stockquantity < 0:
                    stockquantity = 0
                stockupdate = "UPDATE stock SET product_quantity = %s WHERE product_id = %s"
                cur.execute(stockupdate,[stockquantity, productid])

                delet = "DELETE FROM purchase WHERE purchase_id = %s"
                cur.execute(delet,[purchasid])
                
                mydb.commit()
                messagebox.showinfo("Success!!", "Entry deleted from database.", parent=purchas)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())
                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select an Entry.", parent=purchas)

    def update_purchase(self):
        
        if len(self.sel)==1:
            global p_update
            p_update = Toplevel()
            page8 = Update_Purchase(p_update)
            p_update.protocol("WM_DELETE_WINDOW", self.ex2)
            global vall
            vall = []
            for i in self.sel:
                for j in self.tree.item(i)["values"]:
                    vall.append(j)
            
            page8.entry1.insert(0, vall[1])
            page8.entry2.insert(0, vall[6])
            page8.entry3.insert(0, vall[8])
            page8.entry4.insert(0, vall[5])
            page8.entry5.insert(0, vall[2])
            page8.entry6.insert(0, vall[7])
            page8.entry7.insert(0, vall[9])
            page8.entry8.insert(0, vall[10])
            p_update.mainloop()
        elif len(self.sel)==0:
            messagebox.showerror("Error","Please select an purchase-entry to update.")
        else:
            messagebox.showerror("Error","Can only update one purchase-entry at a time.")

    def purchase_entry(self):
        global p_add
        p_add = Toplevel()
        page6 = Purchase_entry(p_add)
        p_add.protocol("WM_DELETE_WINDOW", self.ex)
        p_add.mainloop()


    def ex(self):
        p_add.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()   

    def ex2(self):
        p_update.destroy()
        self.tree.delete(*self.tree.get_children())
        self.DisplayData()  



    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
            purchas.destroy()
            adm.deiconify()


    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            purchas.destroy()
            root.deiconify()
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)


class Purchase_entry:
    def __init__(self, top=None):
        top.geometry("900x500+350+100")
        top.resizable(0, 0)
        top.title("Purchase Entry")

        canvas_widget = Canvas(p_add, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg="#36919c")

        self.p_id = 0
        self.p_name =""
        self.squantity = 0

        self.r1 = p_add.register(self.testint)
        self.r2 = p_add.register(self.testchar)

        self.label1 = Label(p_add)
        self.label1.place(relx=0.05, rely=0.09)
        self.label1.configure(text="Bill No: ")
        self.label1.configure(bg="#36919c")
        self.entry1 = Entry(p_add)
        self.entry1.place(relx=0.05, rely=0.150, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        

        self.label2 = Label(p_add)
        self.label2.place(relx=0.05, rely=0.246)
        self.label2.configure(text="Product Name: ")
        self.label2.configure(bg="#36919c")
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        self.cursor = self.mydb.cursor()
        self.cursor.execute("SELECT description FROM stock")
        self.items = self.cursor.fetchall()
        self.combo = ttk.Combobox(p_add, values=[item[0] for item in self.items])
        self.combo.place(relx=0.05, rely=0.306, width=374, height=30)
        
        def on_select(event):
            selected_item = self.combo.get()
            self.cursor.execute(f"SELECT product_id,product_name,product_quantity FROM stock WHERE description='{selected_item}'")
            result = self.cursor.fetchall()
            self.p_id = result[0][0]
            self.squantity = result[0][2]
            self.p_name = result[0][1]
            print(self.p_name)
        self.combo.bind("<<ComboboxSelected>>", on_select)

        self.label3 = Label(p_add)
        self.label3.place(relx=0.05, rely=0.402)
        self.label3.configure(text="Cost Price: ")
        self.label3.configure(bg="#36919c")
        self.entry3 = Entry(p_add)
        self.entry3.place(relx=0.05, rely=0.462, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(validate="key", validatecommand=(self.r1, "%P"))


        self.label4 = Label(p_add)
        self.label4.place(relx=0.05, rely=0.558)
        self.label4.configure(text="Purchase Date: (yyyy-mm-dd)")
        self.label4.configure(bg="#36919c")
        self.entry4 = Entry(p_add)
        self.entry4.place(relx=0.05, rely=0.618, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")


        self.label5 = Label(p_add)
        self.label5.place(relx=0.530, rely=0.090)
        self.label5.configure(text="Supplier name: ")
        self.label5.configure(bg="#36919c")
        self.entry5 = Entry(p_add)
        self.entry5.place(relx=0.530, rely=0.150, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")


        self.label6 = Label(p_add)
        self.label6.place(relx=0.530, rely=0.246)
        self.label6.configure(text="Quantity: ")
        self.label6.configure(bg="#36919c")
        self.entry6 = Entry(p_add)
        self.entry6.place(relx=0.530, rely=0.306, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")
        self.entry6.configure(validate="key", validatecommand=(self.r1, "%P"))


        self.label7 = Label(p_add)
        self.label7.place(relx=0.530, rely=0.402)
        self.label7.configure(text="Selling Price: ")
        self.label7.configure(bg="#36919c")
        self.entry7 = Entry(p_add)
        self.entry7.place(relx=0.530, rely=0.462, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")
        self.entry7.configure(validate="key", validatecommand=(self.r1, "%P"))


        self.label8 = Label(p_add)
        self.label8.place(relx=0.530, rely=0.558)
        self.label8.configure(text="Product ExpDate: (yyyy-mm-dd)")
        self.label8.configure(bg="#36919c")
        self.entry8 = None
        self.entry8 = Entry(p_add)
        self.entry8.place(relx=0.530, rely=0.618, width=374, height=30)
        self.entry8.configure(font="-family {Poppins} -size 12")
        self.entry8.configure(relief="flat")

        self.button1 = Button(p_add)
        self.button1.place(relx=0.30, rely=0.80, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""ADD""")
        self.button1.configure(command=self.add)

        self.button2 = Button(p_add)
        self.button2.place(relx=0.60, rely=0.80, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#033145")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def add(self):
        bill_no = self.entry1.get()
        proname = self.combo.get()
        pid = self.p_id
        cost = self.entry3.get()
        pdate = self.entry4.get()
        supplier = self.entry5.get()
        quantity = self.entry6.get()
        selling = self.entry7.get()
        expdate = self.entry8.get()
        sqty = self.squantity + int(quantity)
        p_n = self.p_name
        rannumber = random.randint(10,99)

        if bill_no:
            if proname:
                if cost and selling:
                    if pdate:
                        if supplier:
                            if quantity:
                                if expdate == "":
                                    expdate = "0000-00-00"
                                
                                pname = f"{proname}- UN{rannumber}"
                                
                                insert1 = (
                                            "INSERT INTO purchase(purchase_id, bill_no, supplier, product_id, product_name, quantity, cost_price, selling_price, purchase_date, expdate, available_quantity, description) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                        )
                                mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                                cur = mydb.cursor()
                                cur.execute(insert1, [None, bill_no, supplier, pid, p_n, quantity, cost, selling, pdate, expdate, quantity, pname])

                                cur.execute(f"UPDATE stock SET product_quantity = {sqty} WHERE product_id = {pid}")

                                mydb.commit()
                                messagebox.showinfo("Success!!", "Purchase data added in database.", parent=p_add)
                                self.clearr()
                            else:
                                messagebox.showerror("Oops!", "Please enter a password.", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter address.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Please enter designation.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Invalid Aadhar number.", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Invalid phone number.", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Please enter employee name.", parent=p_add)

    def clearr(self):
        self.entry1.delete(0, END)
        self.combo.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)


class Update_Purchase:
    def __init__(self, top=None):
        top.geometry("900x500+350+100")
        top.resizable(0, 0)
        top.title("Update Purchase")

        canvas_widget = Canvas(p_update, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg="#36919c")

        self.r1 = p_update.register(self.testint)
        self.r2 = p_update.register(self.testchar)

        self.label1 = Label(p_update)
        self.label1.place(relx=0.05, rely=0.09)
        self.label1.configure(text="Bill No: ")
        self.label1.configure(bg="#36919c")
        self.entry1 = Entry(p_update)
        self.entry1.place(relx=0.05, rely=0.150, width=374, height=30)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        
        self.label2 = Label(p_update)
        self.label2.place(relx=0.05, rely=0.246)
        self.label2.configure(text="Bill No: ")
        self.label2.configure(bg="#36919c")
        self.entry2 = Entry(p_update)
        self.entry2.place(relx=0.05, rely=0.306, width=374, height=30)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")

        self.label3 = Label(p_update)
        self.label3.place(relx=0.05, rely=0.402)
        self.label3.configure(text="Bill No: ")
        self.label3.configure(bg="#36919c")
        self.entry3 = Entry(p_update)
        self.entry3.place(relx=0.05, rely=0.462, width=374, height=30)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")

        self.label4 = Label(p_update)
        self.label4.place(relx=0.05, rely=0.558)
        self.label4.configure(text="Bill No: ")
        self.label4.configure(bg="#36919c")
        self.entry4 = Entry(p_update)
        self.entry4.place(relx=0.05, rely=0.618, width=374, height=30)
        self.entry4.configure(font="-family {Poppins} -size 12")
        self.entry4.configure(relief="flat")

        self.label5 = Label(p_update)
        self.label5.place(relx=0.530, rely=0.090)
        self.label5.configure(text="Bill No: ")
        self.label5.configure(bg="#36919c")
        self.entry5 = Entry(p_update)
        self.entry5.place(relx=0.530, rely=0.150, width=374, height=30)
        self.entry5.configure(font="-family {Poppins} -size 12")
        self.entry5.configure(relief="flat")

        self.label6 = Label(p_update)
        self.label6.place(relx=0.530, rely=0.246)
        self.label6.configure(text="Bill No: ")
        self.label6.configure(bg="#36919c")
        self.entry6 = Entry(p_update)
        self.entry6.place(relx=0.530, rely=0.306, width=374, height=30)
        self.entry6.configure(font="-family {Poppins} -size 12")
        self.entry6.configure(relief="flat")

        self.label7 = Label(p_update)
        self.label7.place(relx=0.530, rely=0.402)
        self.label7.configure(text="Bill No: ")
        self.label7.configure(bg="#36919c")
        self.entry7 = Entry(p_update)
        self.entry7.place(relx=0.530, rely=0.462, width=374, height=30)
        self.entry7.configure(font="-family {Poppins} -size 12")
        self.entry7.configure(relief="flat")

        self.label8 = Label(p_update)
        self.label8.place(relx=0.530, rely=0.558)
        self.label8.configure(text="Bill No: ")
        self.label8.configure(bg="#36919c")
        self.entry8 = Entry(p_update)
        self.entry8.place(relx=0.530, rely=0.618, width=374, height=30)
        self.entry8.configure(font="-family {Poppins} -size 12")
        self.entry8.configure(relief="flat")


        self.button1 = Button(p_update)
        self.button1.place(relx=0.30, rely=0.80, width=96, height=34)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""UPDATE""")
        self.button1.configure(command=self.update)

        self.button2 = Button(p_update)
        self.button2.place(relx=0.60, rely=0.80, width=86, height=34)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#033145")
        self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""CLEAR""")
        self.button2.configure(command=self.clearr)
        
        # top.geometry("1920x1080+0+0")
        # top.title("Update Purchase")

        

        # canvas_widget = Canvas(p_update, width=800, height=500)
        # canvas_widget.pack(fill="both", expand=True)

        # self.entry1 = Entry(p_update)
        # self.entry1.place(relx=0.132, rely=0.280, width=374, height=30)
        # self.entry1.configure(font="-family {Poppins} -size 12")
        # self.entry1.configure(relief="flat")
        
        # self.entry2 = Entry(p_update)
        # self.entry2.place(relx=0.132, rely=0.397, width=374, height=30)
        # self.entry2.configure(font="-family {Poppins} -size 12")
        # self.entry2.configure(relief="flat")

        # self.entry3 = Entry(p_update)
        # self.entry3.place(relx=0.132, rely=0.513, width=374, height=30)
        # self.entry3.configure(font="-family {Poppins} -size 12")
        # self.entry3.configure(relief="flat")

        # self.entry4 = Entry(p_update)
        # self.entry4.place(relx=0.132, rely=0.629, width=374, height=30)
        # self.entry4.configure(font="-family {Poppins} -size 12")
        # self.entry4.configure(relief="flat")

        # self.entry5 = Entry(p_update)
        # self.entry5.place(relx=0.527, rely=0.280, width=374, height=30)
        # self.entry5.configure(font="-family {Poppins} -size 12")
        # self.entry5.configure(relief="flat")

        # self.entry6 = Entry(p_update)
        # self.entry6.place(relx=0.527, rely=0.397, width=374, height=30)
        # self.entry6.configure(font="-family {Poppins} -size 12")
        # self.entry6.configure(relief="flat")

        # self.entry7 = Entry(p_update)
        # self.entry7.place(relx=0.527, rely=0.513, width=374, height=30)
        # self.entry7.configure(font="-family {Poppins} -size 12")
        # self.entry7.configure(relief="flat")

        # self.entry8 = Entry(p_update)
        # self.entry8.place(relx=0.527, rely=0.629, width=374, height=30)
        # self.entry8.configure(font="-family {Poppins} -size 12")
        # self.entry8.configure(relief="flat")


        # self.button1 = Button(p_update)
        # self.button1.place(relx=0.408, rely=0.836, width=96, height=34)
        # self.button1.configure(relief="flat")
        # self.button1.configure(overrelief="flat")
        # self.button1.configure(activebackground="#CF1E14")
        # self.button1.configure(cursor="hand2")
        # self.button1.configure(foreground="#ffffff")
        # self.button1.configure(background="#CF1E14")
        # self.button1.configure(font="-family {Poppins SemiBold} -size 14")
        # self.button1.configure(borderwidth="0")
        # self.button1.configure(text="""UPDATE""")
        # self.button1.configure(command=self.update)

        # self.button2 = Button(p_update)
        # self.button2.place(relx=0.526, rely=0.836, width=86, height=34)
        # self.button2.configure(relief="flat")
        # self.button2.configure(overrelief="flat")
        # self.button2.configure(activebackground="#CF1E14")
        # self.button2.configure(cursor="hand2")
        # self.button2.configure(foreground="#ffffff")
        # self.button2.configure(background="#CF1E14")
        # self.button2.configure(font="-family {Poppins SemiBold} -size 14")
        # self.button2.configure(borderwidth="0")
        # self.button2.configure(text="""CLEAR""")
        # self.button2.configure(command=self.clearr)

    def update(self):
        bill = self.entry1.get()
        cprice = self.entry2.get()
        pdate = self.entry3.get()
        qty = self.entry4.get()
        supl = self.entry5.get()
        sprice = self.entry6.get()
        expdate = self.entry7.get()
        newavqty = self.entry8.get()

        productname = vall[4]

        if bill:
            if cprice:
                if pdate:
                    if qty and newavqty:
                        if supl:
                            if sprice:
                                old_qty = vall[5]
                                p_id= vall[0]

                                mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                                cur = mydb.cursor()

                                select_query1 = "SELECT product_quantity FROM stock WHERE product_name = %s "
                                cur.execute(select_query1, [productname])
                                rows1 = cur.fetchall()
                                stockavquantity = rows1[0][0]
                                
                                select_query2 = "SELECT available_quantity FROM purchase WHERE purchase_id = %s "
                                cur.execute(select_query2, [p_id])
                                rows2 = cur.fetchall()
                                purchasavquantity = rows2[0][0]

                                
                                sure = messagebox.askyesno("Exit","Are you sure you want to UPDATE...?", parent=purchas)
                                if sure == True:
                                    if int(qty) > old_qty:
                                        diff = int(qty) - old_qty
                                        pavqty = purchasavquantity + diff
                                        savqty = stockavquantity + diff
                                        update1 = (
                                                    "UPDATE purchase SET bill_no = %s, supplier = %s, quantity = %s, cost_price = %s, selling_price = %s, purchase_date = %s, expdate = %s, available_quantity = %s WHERE purchase_id = %s"
                                                )
                                        cur.execute(update1, [bill, supl, qty, cprice, sprice, pdate, expdate, pavqty, p_id])
                                        update2 = (
                                                    "UPDATE stock SET product_quantity = %s WHERE product_name = %s"
                                                )
                                        cur.execute(update2, [savqty, productname])
                                        print("if is called")
                                        vall.clear()
                                        page5.tree.delete(*page5.tree.get_children())
                                        page5.DisplayData()
                                        Purchase.sel.clear()
                                        p_update.destroy()
                                    elif int(qty) < old_qty:
                                        diff = old_qty - int(qty)
                                        pavqty = purchasavquantity - diff
                                        savqty = stockavquantity - diff
                                        update1 = (
                                                    "UPDATE purchase SET bill_no = %s, supplier = %s, quantity = %s, cost_price = %s, selling_price = %s, purchase_date = %s, expdate = %s, available_quantity = %s WHERE purchase_id = %s"
                                                )
                                        cur.execute(update1, [bill, supl, qty, cprice, sprice, pdate, expdate, pavqty, p_id])
                                        update2 = (
                                                    "UPDATE stock SET product_quantity = %s WHERE product_name = %s"
                                                )
                                        cur.execute(update2, [savqty, productname])
                                        print("elif is called")
                                        vall.clear()
                                        page5.tree.delete(*page5.tree.get_children())
                                        page5.DisplayData()
                                        Purchase.sel.clear()
                                        p_update.destroy()
                                    else:
                                        oldavqty = vall[10]
                                        if int(newavqty) > oldavqty:
                                            diff = int(newavqty) - oldavqty
                                            savqty = stockavquantity + diff
                                            update1 = (
                                                        "UPDATE purchase SET bill_no = %s, supplier = %s, quantity = %s, cost_price = %s, selling_price = %s, purchase_date = %s, expdate = %s, available_quantity = %s WHERE purchase_id = %s"
                                                    )
                                            cur.execute(update1, [bill, supl, qty, cprice, sprice, pdate, expdate, newavqty, p_id])
                                            update2 = (
                                                        "UPDATE stock SET product_quantity = %s WHERE product_name = %s"
                                                    )
                                            cur.execute(update2, [savqty, productname])
                                            print("else---if")
                                            vall.clear()
                                            page5.tree.delete(*page5.tree.get_children())
                                            page5.DisplayData()
                                            Purchase.sel.clear()
                                            p_update.destroy()

                                        elif int(newavqty) < oldavqty:
                                            diff = oldavqty - int(newavqty)
                                            savqty = stockavquantity - diff
                                            update1 = (
                                                        "UPDATE purchase SET bill_no = %s, supplier = %s, quantity = %s, cost_price = %s, selling_price = %s, purchase_date = %s, expdate = %s, available_quantity = %s WHERE purchase_id = %s"
                                                    )
                                            cur.execute(update1, [bill, supl, qty, cprice, sprice, pdate, expdate, newavqty, p_id])
                                            update2 = (
                                                        "UPDATE stock SET product_quantity = %s WHERE product_name = %s"
                                                    )
                                            cur.execute(update2, [savqty, productname])
                                            print("else---elif")
                                            vall.clear()
                                            page5.tree.delete(*page5.tree.get_children())
                                            page5.DisplayData()
                                            Purchase.sel.clear()
                                            p_update.destroy()

                                        else:
                                            update1 = (
                                                        "UPDATE purchase SET bill_no = %s, supplier = %s, quantity = %s, cost_price = %s, selling_price = %s, purchase_date = %s, expdate = %s, available_quantity = %s WHERE purchase_id = %s"
                                                    )
                                            cur.execute(update1, [bill, supl, qty, cprice, sprice, pdate, expdate, newavqty, p_id])
                                            print("else is called")
                                            vall.clear()
                                            page5.tree.delete(*page5.tree.get_children())
                                            page5.DisplayData()
                                            Purchase.sel.clear()
                                            p_update.destroy()
                                mydb.commit()
                            else:
                                messagebox.showerror("Oops!", "Please enter a Selling price.", parent=p_add)
                        else:
                            messagebox.showerror("Oops!", "Please enter Supplier.", parent=p_add)
                    else:
                        messagebox.showerror("Oops!", "Please check both quantity are filled or Not.", parent=p_add)
                else:
                    messagebox.showerror("Oops!", "Please enter purchase date", parent=p_add)
            else:
                messagebox.showerror("Oops!", "Please enter cost price", parent=p_add)
        else:
            messagebox.showerror("Oops!", "Please enter bill number", parent=p_add)


    def clearr(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.entry6.delete(0, END)
        self.entry7.delete(0, END)
        self.entry8.delete(0, END)


    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False

    def testchar(self, val):
        if val.isalpha():
            return True
        elif val == "":
            return True
        return False


class Invoice:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Invoices")

        canvas_widget = Canvas(invoice, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')

        frame = Frame(canvas_widget, width=600, height=550)
        frame.place(relx=0.01, rely=0.203)
        frame.configure(bg="#36919c")
        
        self.entry1 = Entry(invoice)
        self.entry1.place(relx=0.052, rely=0.286, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(background="#c9f5f0")

        self.button1 = Button(invoice)
        self.button1.place(relx=0.216, rely=0.289, width=76, height=25)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#CF1E14")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Search""")
        self.button1.configure(command=self.search_inv)

        self.button3 = Button(invoice)
        self.button3.place(relx=0.052, rely=0.432, width=306, height=30)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#ffffff")
        self.button3.configure(background="#033145")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""DELETE INVOICE""")
        self.button3.configure(command=self.delete_invoice)

        self.button4 = Button(invoice)
        self.button4.place(relx=0.052, rely=0.500, width=306, height=30)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#ffffff")
        self.button4.configure(background="#033145")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""UPDATE INVOICE""")
        self.button4.configure(command=self.delete_invoice)

        self.button5 = Button(invoice)
        self.button5.place(relx=0.900, rely=0.106, width=76, height=23)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#ffffff")
        self.button5.configure(background="#CF1E14")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""EXIT""")
        self.button5.configure(command=self.Exit)

        self.scrollbarx = Scrollbar(invoice, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(invoice, orient=VERTICAL)
        self.tree = ttk.Treeview(invoice)
        self.tree.place(relx=0.320, rely=0.203, width=950, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.tree.bind("<Double-1>", self.double_tap)

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.940, rely=0.203, width=15, height=548)
        self.scrollbarx.place(relx=0.325, rely=0.181, width=940, height=15)

        self.tree.configure(
            columns=(
                "Sr No",
                "Bill Number",
                "Date",
                "Customer Name",
                "Customer Phone No.",
                "Total Amount",
            )
        )

        self.tree.heading("Sr No", text="Sr No", anchor=W)
        self.tree.heading("Bill Number", text="Bill Number", anchor=W)
        self.tree.heading("Date", text="Date", anchor=W)
        self.tree.heading("Customer Name", text="Customer Name", anchor=W)
        self.tree.heading("Customer Phone No.", text="Customer Phone No.", anchor=W)
        self.tree.heading("Total Amount", text="Total Amount", anchor=W)
        

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=60)
        self.tree.column("#2", stretch=NO, minwidth=0, width=120)
        self.tree.column("#3", stretch=NO, minwidth=0, width=130)
        self.tree.column("#4", stretch=NO, minwidth=0, width=222)
        self.tree.column("#5", stretch=NO, minwidth=0, width=180)
        self.tree.column("#6", stretch=NO, minwidth=0, width=200)
        

        self.DisplayData()


    def DisplayData(self):
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute("SELECT * FROM bills")
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))
        mydb.commit()


    sel = []
    def on_tree_select(self, Event):
        self.sel.clear()
        for i in self.tree.selection():
            if i not in self.sel:
                self.sel.append(i)

    def double_tap(self, Event):
        item = self.tree.identify('item', Event.x, Event.y)
        global bill_num
        bill_num = self.tree.item(item)['values'][1]
        print(bill_num)

        global bill
        bill = Toplevel()
        pg = open_bill(bill)
        # bill.protocol("WM_DELETE_WINDOW", exitt)
        bill.mainloop()

    def delete_invoice(self):
        val = []
        to_delete = []

        if len(self.sel)!=0:
            sure = messagebox.askyesno("Confirm", "Are you sure you want to delete selected invoice(s)?", parent=invoice)
            if sure == True:
                for i in self.sel:
                    for j in self.tree.item(i)["values"]:
                        val.append(j)
                
                for j in range(len(val)):
                    if j%5==0:
                        to_delete.append(val[j])
                
                for k in to_delete:
                    # delete = "DELETE FROM bill WHERE bill_no = ?"
                    # cur.execute(delete, [k])
                    # db.commit()
                    pass

                messagebox.showinfo("Success!!", "Invoice(s) deleted from database.", parent=invoice)
                self.sel.clear()
                self.tree.delete(*self.tree.get_children())

                self.DisplayData()
        else:
            messagebox.showerror("Error!!","Please select an invoice", parent=invoice)

    def search_inv(self):
        val = []
        for i in self.tree.get_children():
            val.append(i)
            for j in self.tree.item(i)["values"]:
                val.append(j)

        to_search = self.entry1.get()
        for search in val:
            # print(search)
            if search==to_search:
                print(search)
                self.tree.selection_set(val[val.index(search)-2])
                self.tree.focus(val[val.index(search)-2])
                messagebox.showinfo("Success!!", "Bill Number: {} found.".format(self.entry1.get()), parent=invoice)
                break
        else: 
            messagebox.showerror("Oops!!", "Bill Number: {} not found.".format(self.entry1.get()), parent=invoice)

    def Exit(self):
            invoice.destroy()
            adm.deiconify()


class open_bill:
    def __init__(self, top=None):
        
        top.geometry("900x600+350+100")
        top.resizable(0, 0)
        top.title("Bill")

        f1=("Times", 18)
        f2=("Courier New", 18)

        canvas_widget = Canvas(bill, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg="#36919c")

        self.label_1 = Label(bill)
        self.label_1.place(relx=0.100, rely=0.100, width=100, height=30)
        self.label_1.configure(text="Bill No:")
        self.label_1.configure(font=f1)
        self.label_1.configure(anchor=W)
        self.label_1.configure(bg="#36919c")
        self.label_1.configure(foreground="#022120")
        self.label1 = Text(bill)
        self.label1.place(relx=0.200, rely=0.100, width=100, height=30)
        self.label1.configure(font="-family {Podkova} -size 10")
        self.label1.configure(borderwidth=0)
        self.label1.configure(relief="flat")
        self.label1.configure(font=f2)
        self.label1.configure(background="#36919c")
        self.label1.configure(foreground='#ffffff')

        self.label_2 = Label(bill)
        self.label_2.place(relx=0.520, rely=0.100, width=100, height=30)
        self.label_2.configure(text="Bill Date:")
        self.label_2.configure(font=f1)
        self.label_2.configure(anchor=W)
        self.label_2.configure(bg="#36919c")
        self.label_2.configure(foreground="#022120")
        self.label2 = Text(bill)
        self.label2.place(relx=0.630, rely=0.100, width=200, height=30)
        self.label2.configure(font="-family {Podkova} -size 10")
        self.label2.configure(borderwidth=1)
        self.label2.configure(relief="flat")
        self.label2.configure(font=f2)
        self.label2.configure(background="#36919c")
        self.label2.configure(foreground='#ffffff')
        
        self.label_3 = Label(bill)
        self.label_3.place(relx=0.100, rely=0.150, width=200, height=30)
        self.label_3.configure(text="Customer Name:")
        self.label_3.configure(font=f1)
        self.label_3.configure(anchor=W)
        self.label_3.configure(bg="#36919c")
        self.label_3.configure(foreground="#022120")
        self.label3 = Text(bill)
        self.label3.place(relx=0.310, rely=0.150, width=250, height=30)
        self.label3.configure(font="-family {Podkova} -size 10")
        self.label3.configure(borderwidth=1)
        self.label3.configure(relief="flat")
        self.label3.configure(font=f2)
        self.label3.configure(background="#36919c")
        self.label3.configure(foreground='#ffffff')

        self.label_4 = Label(bill)
        self.label_4.place(relx=0.100, rely=0.200, width=200, height=30)
        self.label_4.configure(text="Customer MoNo:")
        self.label_4.configure(font=f1)
        self.label_4.configure(anchor=W)
        self.label_4.configure(bg="#36919c")
        self.label_4.configure(foreground="#022120")
        self.label4 = Text(bill)
        self.label4.place(relx=0.310, rely=0.200, width=250, height=30)
        self.label4.configure(font="-family {Podkova} -size 10")
        self.label4.configure(borderwidth=1)
        self.label4.configure(relief="flat")
        self.label4.configure(font=f2)
        self.label4.configure(background="#36919c")
        self.label4.configure(foreground='#ffffff')

        self.label_5 = Label(bill)
        self.label_5.place(relx=0.700, rely=0.300, width=130, height=30)
        self.label_5.configure(text="Tax Amt:")
        self.label_5.configure(font=f1)
        self.label_5.configure(anchor=W)
        self.label_5.configure(bg="#36919c")
        self.label_5.configure(foreground="#022120")
        self.label5 = Text(bill)
        self.label5.place(relx=0.820, rely=0.300, width=100, height=30)
        self.label5.configure(font="-family {Podkova} -size 10")
        self.label5.configure(borderwidth=1)
        self.label5.configure(relief="flat")
        self.label5.configure(font=f2)
        self.label5.insert(END, "00.0")
        self.label5.configure(state="disabled")
        self.label5.configure(background="#36919c")
        self.label5.configure(foreground='#ffffff')

        self.label_6 = Label(bill)
        self.label_6.place(relx=0.700, rely=0.365, width=130, height=30)
        self.label_6.configure(text="Discount:")
        self.label_6.configure(font=f1)
        self.label_6.configure(anchor=W)
        self.label_6.configure(bg="#36919c")
        self.label_6.configure(foreground="#022120")
        self.label6 = Text(bill)
        self.label6.place(relx=0.820, rely=0.365, width=100, height=30)
        self.label6.configure(borderwidth=1)
        self.label6.configure(relief="flat")
        self.label6.configure(font=f2)
        self.label6.insert(END, "00.0")
        self.label6.configure(state="disabled")
        self.label6.configure(background="#36919c")
        self.label6.configure(foreground='#ffffff')

        self.label_7 = Label(bill)
        self.label_7.place(relx=0.700, rely=0.430, width=130, height=30)
        self.label_7.configure(text="Total Amt:")
        self.label_7.configure(font=f1)
        self.label_7.configure(anchor=W)
        self.label_7.configure(bg="#36919c")
        self.label_7.configure(foreground="#022120")
        self.label7 = Text(bill)
        self.label7.place(relx=0.820, rely=0.430, width=100, height=30)
        self.label7.configure(borderwidth=1)
        self.label7.configure(relief="flat")
        self.label7.configure(font=f2)
        self.label7.configure(background="#36919c")
        self.label7.configure(foreground='#ffffff')

        self.button1 = Button(bill)
        self.button1.place(relx=0.700, rely=0.560, width=200, height=40)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#50ab93")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#033145")
        self.button1.configure(font=f1)
        self.button1.configure(text="Delete")

        self.button2 = Button(bill)
        self.button2.place(relx=0.700, rely=0.650, width=200, height=40)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#50ab93")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#033145")
        self.button2.configure(font=f1)
        self.button2.configure(text="Print")

        self.scrollbary = Scrollbar(bill, orient=VERTICAL)

        self.tree = ttk.Treeview(bill)
        self.tree.place(relx=0.100, rely=0.300, width=500, height=400)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set
        )
        self.tree.configure(selectmode="extended")

        # self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.scrollbary.configure(command=self.tree.yview)

        self.scrollbary.place(relx=0.655, rely=0.300, width=15, height=400)

        self.tree.configure(
            columns=(
                "Products",
                "Quantity",
                "Price",
                "Total",
            )
        )

        self.tree.heading("Products", text="Products", anchor=W)
        self.tree.heading("Quantity", text="Quantity", anchor=W)
        self.tree.heading("Price", text="Price", anchor=W)
        self.tree.heading("Total", text="Total", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=260)
        self.tree.column("#2", stretch=NO, minwidth=0, width=80)
        self.tree.column("#3", stretch=NO, minwidth=0, width=80)
        self.tree.column("#4", stretch=NO, minwidth=0, width=80)


        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        find_bill = "SELECT * FROM bills WHERE bill_id = %s"
        cur.execute(find_bill, [bill_num])
        results = cur.fetchall()
        if results:
            self.label1.insert(END, results[0][1])
            self.label1.configure(state="disabled")

            self.label2.insert(END, results[0][2])
            self.label2.configure(state="disabled")

            self.label3.insert(END, results[0][3])
            self.label3.configure(state="disabled")
    
            self.label4.insert(END, results[0][4])
            self.label4.configure(state="disabled")

            self.label7.insert(END, results[0][5])
            self.label7.configure(state="disabled")

        
        select = "SELECT product_name, sale_quantity, selling_price, total FROM invoice WHERE bill_id = %s"
        cur.execute(select, [bill_num])
        fetch = cur.fetchall()
        for data in fetch:
            self.tree.insert("", "end", values=(data))
        
        mydb.commit()


page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()