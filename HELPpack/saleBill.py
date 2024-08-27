#==================imports===================
import mysql.connector
import re
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
#============================================



root = Tk()

root.geometry("1920x1080+0+0")
root.title("Retail Manager")


user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()


cust_name = StringVar()
cust_num = StringVar()
cust_new_bill = StringVar()
cust_search_bill = StringVar()
bill_date = StringVar()

def random_bill_no():
    letters = string.ascii_uppercase
    result = ''.join(random.choice(letters) for _ in range(2))
    result0 = random.randint(1000,9999)
    bill_number = f"{result}{result0}"
    return bill_number


def valid_phone(phn):
    if re.match(r"[789]\d{9}$", phn):
        return True
    return False

def login(Event=None):
    global username
    username = user.get()
    password = passwd.get()

    if username == "Admin" and password == "123":
        messagebox.showinfo("Login Page", "The login is successful")
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)
        root.withdraw()
        global biller
        global page2
        biller = Toplevel()
        page2 = bill_window(biller)
        page2.time()
        biller.protocol("WM_DELETE_WINDOW", exitt)
        biller.mainloop()

    else:
        messagebox.showerror("Error", "Incorrect username or password.")
        page1.entry2.delete(0, END)



def logout():
    sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=biller)
    if sure == True:
        biller.destroy()
        root.deiconify()
        page1.entry1.delete(0, END)
        page1.entry2.delete(0, END)

class login_page:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Sale Bill")

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
        self.button1.configure(command=login)
        
        frame.pack(pady=100)
        frame.configure(bg="#36919c")


class Item:
    def __init__(self, id, name, sprice, qty, total):
        self.productid = id
        self.product_name = name
        self.price = sprice
        self.qty = qty
        self.total = total

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)

    def dis(self):
        for i in self.items:
            print("name- ",i.product_name," price- ",i.price," Qut- ",i.qty)

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        for i in self.items:
            total += i.price * i.qty
        return total

    def isEmpty(self):
        if len(self.items)==0:
            return True
        
    def allCart(self):
        for i in self.items:
            if (i.product_name in self.dictionary):
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name:i.qty})
    

def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=biller)
    if sure == True:
        biller.destroy()
        root.destroy()


class bill_window:
    def __init__(self, top=None):
        top.geometry("1920x1080+0+0")
        top.title("Billing System")

        cfont1 = font.Font(family="Helvetica", size=14)
        cfont2 = font.Font(family="Helvetica", size=14, weight="bold")
        but_font = font.Font(family="Helvetica", size=12, weight="bold")
        but_font1 = font.Font(family="Helvetica", size=14, weight="bold")
        but_font2 = font.Font(family="Helvetica", size=17, weight="bold")
        but_font3 = font.Font(family="Helvetica", size=11, weight="bold")
        
        canvas_widget = Canvas(biller, width=800, height=500)
        canvas_widget.pack(fill="both", expand=True)
        canvas_widget.configure(bg='#97dbd6')

        self.clock = Label(biller)
        self.clock.place(relx=0.870, rely=0.330, width=165, height=45) 
        self.clock.configure(font=but_font2)
        self.clock.configure(foreground="#ffffff")
        self.clock.configure(background="#033145")

        frame = Frame(canvas_widget, width=1800, height=100)
        self.message = Label(biller)
        self.message.place(relx=0.038, rely=0.055, width=136, height=30)
        self.message.configure(font= cfont2)
        self.message.configure(foreground="#000000")
        self.message.configure(background="#97dbd6")
        self.message.configure(text="Admin")
        self.message.configure(anchor="w")

        self.labet1 = Label(biller)
        self.labet1.place(relx=0.402, rely=0.20, width=240, height=28)
        self.labet1.configure(font="-family {Poppins} -size 10")
        self.labet1.configure(foreground="#063c42")
        self.labet1.configure(background="#36919c")
        self.labet1.configure(text="Customer Name: ")
        self.labet1.configure(font=cfont2)
        self.labet1.configure(anchor="w")
        self.entry1 = Entry(biller)
        self.entry1.place(relx=0.402, rely=0.23, width=240, height=28)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(relief="flat")
        self.entry1.configure(textvariable=cust_name)

        self.labet2 = Label(biller)
        self.labet2.place(relx=0.684, rely=0.20, width=240, height=28)
        self.labet2.configure(font="-family {Poppins} -size 10")
        self.labet2.configure(foreground="#063c42")
        self.labet2.configure(background="#36919c")
        self.labet2.configure(text="Customer Number: ")
        self.labet2.configure(font=cfont2)
        self.labet2.configure(anchor="w")
        self.entry2 = Entry(biller)
        self.entry2.place(relx=0.684, rely=0.23, width=240, height=28)
        self.entry2.configure(font="-family {Poppins} -size 12")
        self.entry2.configure(relief="flat")
        self.entry2.configure(textvariable=cust_num)

        self.entry3 = Entry(biller)
        self.entry3.place(relx=0.102, rely=0.23, width=240, height=28)
        self.entry3.configure(font="-family {Poppins} -size 12")
        self.entry3.configure(relief="flat")
        self.entry3.configure(textvariable=cust_search_bill)

        self.button2 = Button(biller)
        self.button2.place(relx=0.280, rely=0.234, width=76, height=23)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#CF1E14")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#033145")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Search""")       
        self.button2.configure(command=self.search_bill)

        frame.place(relx=0, rely=0.185)
        frame.configure(bg="#36919c")
        
        frame1 = Frame(canvas_widget, width=600, height=370)
        
        self.button7 = Button(biller)
        self.button7.place(relx=0.058, rely=0.676, width=110, height=30)
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#CF1E14")
        self.button7.configure(cursor="hand2")
        self.button7.configure(foreground="#ffffff")
        self.button7.configure(background="#033145")
        self.button7.configure(font= but_font)
        self.button7.configure(borderwidth="0")
        self.button7.configure(text="""Add To Cart""")
        self.button7.configure(command=self.add_to_cart)

        self.button8 = Button(biller)
        self.button8.place(relx=0.250, rely=0.676, width=110, height=30)
        self.button8.configure(relief="flat")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#CF1E14")
        self.button8.configure(cursor="hand2")
        self.button8.configure(foreground="#ffffff")
        self.button8.configure(background="#033145")
        self.button8.configure(font= but_font)
        self.button8.configure(borderwidth="0")
        self.button8.configure(text="""Clear""")
        self.button8.configure(command=self.clear_selection)

        self.button9 = Button(biller)
        self.button9.place(relx=0.154, rely=0.676, width=110, height=30)
        self.button9.configure(relief="flat")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#CF1E14")
        self.button9.configure(cursor="hand2")
        self.button9.configure(foreground="#ffffff")
        self.button9.configure(background="#033145")
        self.button9.configure(font= but_font)
        self.button9.configure(borderwidth="0")
        self.button9.configure(text="""Remove""")
        self.button9.configure(command=self.remove_product)

        frame1.place(relx=0, rely=0.300)
        frame1.configure(bg="#36919c")

        self.button3 = Button(biller)
        self.button3.place(relx=0.870, rely=0.535, width=165, height=45)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#CF1E14")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#97dbd6")
        self.button3.configure(background="#033145")
        self.button3.configure(font=but_font1)
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Total""")
        self.button3.configure(command=self.total_bill)

        self.button4 = Button(biller)
        self.button4.place(relx=0.870, rely=0.655, width=165, height=60)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#CF1E14")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#97dbd6")
        self.button4.configure(background="#033145")
        self.button4.configure(font=but_font1)
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Generate\nBill""")
        self.button4.configure(command=self.gen_bill)

        self.button5 = Button(biller)
        self.button5.place(relx=0.870, rely=0.420, width=165, height=45)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#CF1E14")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#97dbd6")
        self.button5.configure(background="#033145")
        self.button5.configure(font=but_font1)
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Clear Bill""")
        self.button5.configure(command=self.clear_bill)

        self.button6 = Button(biller)
        self.button6.place(relx=0.031, rely=0.104, width=76, height=23)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#CF1E14")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#CF1E14")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.button6.configure(borderwidth="3")
        self.button6.configure(text="""Logout""")
        self.button6.configure(text="""Logout""")
        self.button6.configure(command=exitt)


        text_font = ("Poppins", "10")
        self.combo1_lab = Label(biller)
        self.combo1_lab.place(relx=0.035, rely=0.320, width=477, height=26)
        self.combo1_lab.configure(text="Product Category:")
        self.combo1_lab.configure(bg="#36919c")
        self.combo1_lab.configure(font=but_font)
        self.combo1_lab.configure(anchor=W)
        self.combo1 = ttk.Combobox(biller)
        self.combo1.place(relx=0.035, rely=0.350, width=477, height=26)
        self.combo1['values'] = ('Solid', 'Liquid', 'Powder', 'Paste', 'Gas')
        self.combo1.configure(state="readonly")
        self.combo1.configure(font="-family {Poppins} -size 10")
        self.combo1.option_add("*TCombobox*Listbox.font", text_font)
        self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#06495c")

    
        self.combo2_lab = Label(biller)
        self.combo2_lab.place(relx=0.035, rely=0.391, width=477, height=26)
        self.combo2_lab.configure(text="Product Name:")
        self.combo2_lab.configure(bg="#36919c")
        self.combo2_lab.configure(font=but_font)
        self.combo2_lab.configure(anchor=W)
        self.combo2 = ttk.Combobox(biller)
        self.combo2.place(relx=0.035, rely=0.421, width=477, height=26)
        self.combo2.configure(font="-family {Poppins} -size 10")
        self.combo2.option_add("*TCombobox*Listbox.font", text_font) 
        self.combo2.configure(state="disabled")


        self.combo3_lab = Label(biller)
        self.combo3_lab.place(relx=0.035, rely=0.463, width=477, height=26)
        self.combo3_lab.configure(text="Product Lot:")
        self.combo3_lab.configure(bg="#36919c")
        self.combo3_lab.configure(font=but_font)
        self.combo3_lab.configure(anchor=W)
        self.combo3 = ttk.Combobox(biller)
        self.combo3.place(relx=0.035, rely=0.493, width=477, height=26)
        self.combo3.configure(state="disabled")
        self.combo3.configure(font="-family {Poppins} -size 10")
        self.combo3.option_add("*TCombobox*Listbox.font", text_font)


        self.entry4_lab = Label(biller)
        self.entry4_lab.place(relx=0.035, rely=0.541, width=477, height=26)
        self.entry4_lab.configure(text="Product Quantity:")
        self.entry4_lab.configure(bg="#36919c")
        self.entry4_lab.configure(font=but_font)
        self.entry4_lab.configure(anchor=W)
        self.r1 = biller.register(self.testint)
        self.entry4 = ttk.Entry(biller)
        self.entry4.place(relx=0.035, rely=0.571, width=477, height=26)
        self.entry4.configure(font="-family {Poppins} -size 10")
        self.entry4.configure(validate="key", validatecommand=(self.r1, "%P"))
        self.entry4.configure(foreground="#000000")
        self.entry4.configure(state="disabled")

        self.lab = Label(biller)
        self.lab.place(relx=0.402, rely=0.389, width=695, height=26)
        self.lab.configure(text="\tProduct Name \t\t\t - Quantity\t\t              Price")
        self.lab.configure(borderwidth=2)
        self.lab.configure(anchor=W)
        self.lab.configure(foreground="#082422")
        self.lab.configure(background="#ffffff")
        self.lab.configure(font=but_font3)

        self.Scrolledtext1 = tkst.ScrolledText(top)
        self.Scrolledtext1.place(relx=0.402, rely=0.420, width=695, height=275)
        self.Scrolledtext1.configure(borderwidth=2)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 10")
        self.Scrolledtext1.configure(state="disabled")

        self.combo1.bind("<<ComboboxSelected>>", self.get_category)

    def testint(self, val):
        if val.isdigit():
            return True
        elif val == "":
            return True
        return False
        
    def get_category(self, Event):
        self.combo2.configure(state="readonly")
        self.combo2.set('')
        self.combo3.set('')
        find_product = "SELECT product_name FROM stock WHERE category = %s"
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute(find_product, [self.combo1.get()])
        result2 = cur.fetchall()
        subcat = []
        for j in range(len(result2)):       
            if(result2[j][0] not in subcat):
                subcat.append(result2[j][0])
        
        self.combo2.configure(values=subcat)
        self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
        self.combo3.configure(state="disabled")

        # print("1 -- ",self.combo2.get())

    def get_subcat(self, Event):
        self.combo3.configure(state="readonly")
        self.combo3.set('')
        find_product = "SELECT description FROM purchase WHERE product_name = %s AND available_quantity > 0"
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute(find_product, [self.combo2.get()])
        result3 = cur.fetchall()
        pro = []
        for k in range(len(result3)):
            pro.append(result3[k][0])

        self.combo3.configure(values=pro)
        self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
        self.entry4.configure(state="disabled")
        

    def show_qty(self, Event):
        cfont2 = font.Font(family="Helvetica", size=11, weight="bold")
        self.entry4.configure(state="normal")
        self.qty_label = Label(biller)
        self.qty_label.place(relx=0.033, rely=0.606, width=100, height=26)
        self.qty_label.configure(anchor="w")
        self.qty_label.configure(font=cfont2)
        self.qty_label.configure(foreground="#063c42")

        product_name = self.combo3.get()
        find_qty = "SELECT available_quantity FROM purchase WHERE description = %s"
        mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
        cur = mydb.cursor()
        cur.execute(find_qty, [product_name])
        results = cur.fetchone()
        self.qty_label.configure(text="In Stock: {}".format(results[0]))
        self.qty_label.configure(background="#36919c")
        self.qty_label.configure(foreground="#333333")
    
    cart = Cart()
    def add_to_cart(self):
        self.Scrolledtext1.configure(state="normal")
        strr = self.Scrolledtext1.get('1.0', END)
        if strr.find('Total')==-1:
            product_name = self.combo3.get()
            if(product_name!=""):
                product_qty = self.entry4.get()
                find_mrp = "SELECT product_id, selling_price, available_quantity FROM purchase WHERE description = %s"
                
                mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                cur = mydb.cursor()
                cur.execute(find_mrp, [product_name])
                results = cur.fetchall()
                stock = results[0][2]
                mrp = results[0][1]
                pid = results[0][0]
                if product_qty.isdigit()==True:
                    if (stock-int(product_qty))>=0:
                        total = mrp*int(product_qty)
                        item = Item(pid, product_name, mrp, int(product_qty), total)
                        self.cart.add_item(item)
                        
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "\t{}\t\t\t\t\t-- {}\t\t\t\t  {}\n".format(product_name, product_qty, total)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=biller)
        else:
            self.Scrolledtext1.delete('1.0', END)
            new_li = []
            li = strr.split("\n")
            for i in range(len(li)):
                if len(li[i])!=0:
                    if li[i].find('Total')==-1:
                        new_li.append(li[i])
                    else:
                        break
            for j in range(len(new_li)-1):
                self.Scrolledtext1.insert('insert', new_li[j])
                self.Scrolledtext1.insert('insert','\n')
            product_name = self.combo3.get()
            if(product_name!=""):
                product_qty = self.entry4.get()
                mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                cur = mydb.cursor()
                find_mrp = "SELECT selling_price, available_quantity, product_id FROM purchase WHERE product_name = %s"
                cur.execute(find_mrp, [product_name])
                results = cur.fetchall()
                stock = results[0][1]
                mrp = results[0][0]
                if product_qty.isdigit()==True:
                    if (stock-int(product_qty))>=0:
                        sp = results[0][0]*int(product_qty)
                        item = Item(product_name, mrp, int(product_qty))
                        self.cart.add_item(item)
                        self.Scrolledtext1.configure(state="normal")
                        bill_text = "\t{}\t\t\t\t\t-- {}\t\t\t\t  {}\n".format(product_name, product_qty, total)
                        self.Scrolledtext1.insert('insert', bill_text)
                        self.Scrolledtext1.configure(state="disabled")
                    else:
                        messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=biller)
                else:
                    messagebox.showerror("Oops!", "Invalid quantity.", parent=biller)
            else:
                messagebox.showerror("Oops!", "Choose a product.", parent=biller)

    def remove_product(self):
        if(self.cart.isEmpty()!=True):
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                    new_string = get_all_bill[:len(get_all_bill)-3]
                    self.Scrolledtext1.delete('1.0', END)
                    for i in range(len(new_string)):
                        self.Scrolledtext1.insert('insert', new_string[i])
                        self.Scrolledtext1.insert('insert','\n')
                    
                    self.Scrolledtext1.configure(state="disabled")
            else:
                try:
                    self.cart.remove_item()
                except IndexError:
                    messagebox.showerror("Oops!", "Cart is empty", parent=biller)
                else:
                    self.Scrolledtext1.delete('1.0', END)
                    new_li = []
                    li = strr.split("\n")
                    for i in range(len(li)):
                        if len(li[i])!=0:
                            if li[i].find('Total')==-1:
                                new_li.append(li[i])
                            else:
                                break
                    new_li.pop()
                    for j in range(len(new_li)-1):
                        self.Scrolledtext1.insert('insert', new_li[j])
                        self.Scrolledtext1.insert('insert','\n')
                    self.Scrolledtext1.configure(state="disabled")

        else:
            messagebox.showerror("Oops!", "Add a product.", parent=biller)

    def wel_bill(self):

        cfont1 = font.Font(family="Helvetica", size=14)
        
        self.name_messagel = Label(biller)
        self.name_messagel.place(relx=0.402, rely=0.310, width=230, height=30)
        self.name_messagel.configure(text="Customer Name:")
        self.name_messagel.configure(anchor=W)
        self.name_messagel.configure(font=cfont1)
        self.name_messagel.configure(bg="#97dbd6")
        self.name_messagel.configure(fg="#34615e")
        self.name_message = Text(biller)
        self.name_message.place(relx=0.402, rely=0.340, width=230, height=30)
        self.name_message.configure(font="-family {Podkova} -size 14")
        self.name_message.configure(borderwidth=2)
        self.name_message.configure(background="#ffffff")

        self.num_messagel = Label(biller)
        self.num_messagel.place(relx=0.562, rely=0.310, width=230, height=30)
        self.num_messagel.configure(text="Mobile No:")
        self.num_messagel.configure(anchor=W)
        self.num_messagel.configure(font=cfont1)
        self.num_messagel.configure(bg="#97dbd6")
        self.num_messagel.configure(fg="#34615e")
        self.num_message = Text(biller)
        self.num_message.place(relx=0.562, rely=0.340, width=140, height=30)
        self.num_message.configure(font="-family {Podkova} -size 14")
        self.num_message.configure(borderwidth=2)
        self.num_message.configure(background="#ffffff")

        self.bill_messagel = Label(biller)
        self.bill_messagel.place(relx=0.662, rely=0.310, width=230, height=30)
        self.bill_messagel.configure(text="Bill No:")
        self.bill_messagel.configure(anchor=W)
        self.bill_messagel.configure(font=cfont1)
        self.bill_messagel.configure(bg="#97dbd6")
        self.bill_messagel.configure(fg="#34615e")
        self.bill_message = Text(biller)
        self.bill_message.place(relx=0.662, rely=0.340, width=140, height=30)
        self.bill_message.configure(font="-family {Podkova} -size 14")
        self.bill_message.configure(borderwidth=2)
        self.bill_message.configure(background="#ffffff")

        self.bill_date_messagel = Label(biller)
        self.bill_date_messagel.place(relx=0.762, rely=0.310, width=130, height=30)
        self.bill_date_messagel.configure(text="Date:")
        self.bill_date_messagel.configure(anchor=W)
        self.bill_date_messagel.configure(font=cfont1)
        self.bill_date_messagel.configure(bg="#97dbd6")
        self.bill_date_messagel.configure(fg="#34615e")
        self.bill_date_message = Text(biller)
        self.bill_date_message.place(relx=0.762, rely=0.340, width=140, height=30)
        self.bill_date_message.configure(font="-family {Podkova} -size 14")
        self.bill_date_message.configure(borderwidth=2)
        self.bill_date_message.configure(background="#ffffff")

    
    def total_bill(self):
        if self.cart.isEmpty():
            messagebox.showerror("Oops!", "Add a product.", parent=biller)
        else:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)
            if strr.find('Total')==-1:
                self.Scrolledtext1.configure(state="normal")
                divider = "\n\n\n"+("─"*61)
                self.Scrolledtext1.insert('insert', divider)
                total = "\n\tTotal\t\t\t\t\t\t\t\t\tRs. {}".format(self.cart.total())
                self.Scrolledtext1.insert('insert', total)
                divider2 = "\n"+("─"*61)
                self.Scrolledtext1.insert('insert', divider2)
                self.Scrolledtext1.configure(state="disabled")
            else:
                return

    state = 1
    def gen_bill(self):

        if self.state == 1:
            strr = self.Scrolledtext1.get('1.0', END)
            self.wel_bill()
            if (cust_name.get()==""):
                messagebox.showerror("Oops!", "Please enter a customer name.", parent=biller)
            elif (cust_num.get()==""):
                messagebox.showerror("Oops!", "Please enter a number.", parent=biller)
            elif valid_phone(cust_num.get())==False:
                messagebox.showerror("Oops!", "Please enter a valid number.", parent=biller)
            elif (self.cart.isEmpty()):
                messagebox.showerror("Oops!", "Cart is empty.", parent=biller)
            else: 
                if strr.find('Total')==-1:
                    self.total_bill()
                    self.gen_bill()
                else:
                    self.name_message.insert(END, cust_name.get())
                    self.name_message.configure(state="disabled")
            
                    self.num_message.insert(END, cust_num.get())
                    self.num_message.configure(state="disabled")
            
                    cust_new_bill.set(random_bill_no())

                    self.bill_message.insert(END, cust_new_bill.get())
                    self.bill_message.configure(state="disabled")
                
                    bill_date.set(str(date.today()))

                    self.bill_date_message.insert(END, bill_date.get())
                    self.bill_date_message.configure(state="disabled")

                    mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimdb')
                    cur = mydb.cursor()

                    for i in self.cart.items:
                        
                        insert = "INSERT INTO invoice(invoice_id,invoice_date, bill_id, customer_name, customer_number, product_id, product_name, sale_quantity, selling_price, total, grand_total) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        cur.execute(insert, [None, bill_date.get(),cust_new_bill.get(), cust_name.get(), cust_num.get(), i.productid, i.product_name, i.qty, i.price, i.total, self.cart.total()])
                        
                        select1 = "SELECT available_quantity FROM purchase WHERE description = %s"
                        cur.execute(select1,[i.product_name])
                        quant1 = cur.fetchall()
                        new_purchase_qty = quant1[0][0] - i.qty

                        select2 = "SELECT product_quantity FROM stock WHERE product_id = %s"
                        cur.execute(select2,[i.productid])
                        quant2 = cur.fetchall()
                        new_stock_qty = quant2[0][0] - i.qty

                        update_qty1 = "UPDATE purchase SET available_quantity = %s WHERE description = %s"
                        cur.execute(update_qty1, [new_purchase_qty, i.product_name])

                        update_qty2 = "UPDATE stock SET product_quantity = %s WHERE product_id = %s"
                        cur.execute(update_qty2, [new_stock_qty, i.productid])

                    
                    insert1 = "INSERT INTO bills(srno,bill_id, bill_date, customer_name, customer_number, total_amt) VALUES(%s,%s,%s,%s,%s,%s)"
                    cur.execute(insert1, [None, cust_new_bill.get(), bill_date.get(), cust_name.get(), cust_num.get(), self.cart.total()]) 
                    mydb.commit()

                    messagebox.showinfo("Success!!", "Bill Generated", parent=biller)
                    self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.state = 0
        else:
            return
                    
    def clear_bill(self):
        self.wel_bill()
        self.entry1.configure(state="normal")
        self.entry2.configure(state="normal")
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.name_message.configure(state="normal")
        self.num_message.configure(state="normal")
        self.bill_message.configure(state="normal")
        self.bill_date_message.configure(state="normal")
        self.Scrolledtext1.configure(state="normal")
        self.name_message.delete(1.0, END)
        self.num_message.delete(1.0, END)
        self.bill_message.delete(1.0, END)
        self.bill_date_message.delete(1.0, END)
        self.Scrolledtext1.delete(1.0, END)
        self.name_message.configure(state="disabled")
        self.num_message.configure(state="disabled")
        self.bill_message.configure(state="disabled")
        self.bill_date_message.configure(state="disabled")
        self.Scrolledtext1.configure(state="disabled")
        self.cart.remove_items()
        self.state = 1

    def clear_selection(self):
        self.entry4.delete(0, END)
        self.combo1.configure(state="normal")
        self.combo2.configure(state="normal")
        self.combo3.configure(state="normal")
        self.combo1.delete(0, END)
        self.combo2.delete(0, END)
        self.combo3.delete(0, END)
        self.combo2.configure(state="disabled")
        self.combo3.configure(state="disabled")
        self.entry4.configure(state="disabled")
        try:
            self.qty_label.configure(foreground="#ffffff")
        except AttributeError:
            pass
             
    def search_bill(self):
        # find_bill = "SELECT * FROM bill WHERE bill_no = ?"
        # cur.execute(find_bill, [cust_search_bill.get().rstrip()])
        # results = cur.fetchall()
        # if results:
        #     self.clear_bill()
        #     self.wel_bill()
        #     self.name_message.insert(END, results[0][2])
        #     self.name_message.configure(state="disabled")
    
        #     self.num_message.insert(END, results[0][3])
        #     self.num_message.configure(state="disabled")
    
        #     self.bill_message.insert(END, results[0][0])
        #     self.bill_message.configure(state="disabled")

        #     self.bill_date_message.insert(END, results[0][1])
        #     self.bill_date_message.configure(state="disabled")

        #     self.Scrolledtext1.configure(state="normal")
        #     self.Scrolledtext1.insert(END, results[0][4])
        #     self.Scrolledtext1.configure(state="disabled")

        #     self.entry1.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
        #     self.entry2.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")

        #     self.state = 0
        # else:
        #     messagebox.showerror("Error!!", "Bill not found.", parent=biller)
        #     self.entry3.delete(0, END)
        pass

            
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)


page1 = login_page(root)
root.bind("<Return>", login)
root.mainloop()

