# ==================( IMPORT )==================
from tkinter import *
from docx import Document
import win32print
from docx2pdf import convert
from docxtpl import DocxTemplate
import os
import webbrowser
# import re
# import string
import mysql.connector
# import random
# import psutil
# from datetime import date
# from tkinter import ttk
# from GSIMSPac import fun
# from GSIMSPac import Product
# from GSIMSPac import Partys
# from GSIMSPac import PurchaseDC
# from GSIMSPac import PurchaseInvoice
# from datetime import datetime
# from tkcalendar import DateEntry
# from tkinter import messagebox
# ===============================================

class Headder:
    def __init__(self,canvas_widget,subTitlename):
        title = Label(canvas_widget)
        title.place(relx=0.08,rely=0.003)
        title.configure(text="Grocery Shop Inventory Management System")
        title.configure(font=("Times", 50))
        title.configure(bg="#e5e6d5")
        title.configure(fg="#6e5a20")

        self.c1 = Canvas(canvas_widget)
        self.c1.place(relx=0.9,rely=0.035)
        self.c1.configure(width=60,height=10)
        self.c1.configure(bg='#6e5a20')
        self.c2 = Canvas(canvas_widget)
        self.c2.place(relx=0.9,rely=0.055)
        self.c2.configure(width=60,height=10)
        self.c2.configure(bg='#6e5a20')
        self.c3 = Canvas(canvas_widget)
        self.c3.place(relx=0.9,rely=0.075)
        self.c3.configure(width=60,height=10)
        self.c3.configure(bg='#6e5a20')

        self.subTitle = Label(canvas_widget)
        self.subTitle.place(relx=0.0,rely=0.11)
        self.subTitle.configure(text=subTitlename)
        self.subTitle.configure(bg="#ad995e")
        self.subTitle.configure(font=("Arial Black", 15))
        self.subTitle.configure(width=110)
        
def shortKeys(canvas_widget):  

    ShortCutPanel = Canvas(canvas_widget)
    ShortCutPanel.place(relx=0.38,rely=0.3)
    ShortCutPanel.configure(width=400,height=350)
    ShortCutPanel.configure(bg='#c4b076')

    lab1 = Label(ShortCutPanel)
    lab1.place(relx=0.1,rely=0.1)
    lab1.configure(text="Ctrl+S+B       Sale Inv Bill")
    lab1.configure(font=("Times", 20))
    lab1.configure(bg="#c4b076")
    lab1.configure(fg="#544312")
    
    lab2 = Label(ShortCutPanel)
    lab2.place(relx=0.1,rely=0.2)
    lab2.configure(text="Ctrl+S+R    Sale Return Bill")
    lab2.configure(font=("Times", 20))
    lab2.configure(bg="#c4b076")
    lab2.configure(fg="#544312")
    
    lab3 = Label(ShortCutPanel)
    lab3.place(relx=0.1,rely=0.3)
    lab3.configure(text="Ctrl+D+C   Purchase DC")
    lab3.configure(font=("Times", 20))
    lab3.configure(bg="#c4b076")
    lab3.configure(fg="#544312")
    
    lab4 = Label(ShortCutPanel)
    lab4.place(relx=0.1,rely=0.4)
    lab4.configure(text="Ctrl+P+I     Purchase Inv Bill")
    lab4.configure(font=("Times", 20))
    lab4.configure(bg="#c4b076")
    lab4.configure(fg="#544312")
    
    lab5 = Label(ShortCutPanel)
    lab5.place(relx=0.1,rely=0.5)
    lab5.configure(text="Ctrl+P+A   Party Add")
    lab5.configure(font=("Times", 20))
    lab5.configure(bg="#c4b076")
    lab5.configure(fg="#544312")
    
    lab6 = Label(ShortCutPanel)
    lab6.place(relx=0.1,rely=0.6)
    lab6.configure(text="Ctrl+P+R   Product Add")
    lab6.configure(font=("Times", 20))
    lab6.configure(bg="#c4b076")
    lab6.configure(fg="#544312")
    
    lab7 = Label(ShortCutPanel)
    lab7.place(relx=0.1,rely=0.8)
    lab7.configure(text="Ctrl+X       EXIT")
    lab7.configure(font=("Times", 20))
    lab7.configure(bg="#c4b076")
    lab7.configure(fg="#544312")
    
    lab8 = Label(ShortCutPanel)
    lab8.place(relx=0.1,rely=0.7)
    lab8.configure(text="Ctrl+H       Home")
    lab8.configure(font=("Times", 20))
    lab8.configure(bg="#c4b076")
    lab8.configure(fg="#544312")

def callme():
    print("test is ok...")

def clearall(canvas_widget):
    for widget in canvas_widget.winfo_children():
        widget.destroy()

def print_docx(file_path, printer_name): # check this function using printer name
    # Load the DOCX file
    doc = Document(file_path)

    # Concatenate all paragraphs into a single string
    content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

    # Specify the printer name
    printer = win32print.OpenPrinter(printer_name)

    # Create a printer job
    job = win32print.StartDocPrinter(printer, 1, ("My Document", None, "RAW"))

    # Start a new page
    win32print.StartPagePrinter(printer)

    # Send the content to the printer
    win32print.WritePrinter(printer, content.encode('utf-8'))

    # End the page and the print job
    win32print.EndPagePrinter(printer)
    win32print.EndDocPrinter(printer)
    win32print.ClosePrinter(printer)

def generate_invoice(invoiceid):
    invoice_list = []
    doc = DocxTemplate("invoice_template.docx")
    mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
    cur = mydb.cursor()
    cur.execute("select * from sale where entryno = %s",[invoiceid])
    data = cur.fetchall()
    mydb.commit()
    for item in data:
        product = [item[10],item[11],item[12],item[13],item[14],item[15],item[16],item[17],item[18]]
        invoice_list.append(product)

    doc.render({"billtype":data[0][8], 
            "customername":data[0][3],
            "address":data[0][6],
            "mobileno":data[0][5],
            "adharno":data[0][7],
            "invoiceno":data[0][1],
            "invoicedate":data[0][2],
            "invoice_list":invoice_list,
            "totalqty":data[0][23],
            "note":data[0][9],
            "roundoff":data[0][26],
            "total":data[0][27],
            "discount":data[0][24],
            "charge":data[0][25],
            "nettotal":data[0][28]})
    
    docx_file_path = data[0][1] + "new_invoice" + ".docx"
    pdf_file_path = data[0][1] + "new_invoice" + ".pdf"
    doc.save(docx_file_path)
    try:
        convert(docx_file_path, pdf_file_path)
    except Exception as e:
        print(f"During conversion: {e}")
    try:
        os.remove(docx_file_path)
        # os.remove(pdf_file_path)
    except FileNotFoundError:
        pass
    except Exception as e:
        pass
    webbrowser.open(pdf_file_path)