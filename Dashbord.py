# ==================( IMPORT )==================
import os
from tkinter import *
import re
import string
from PIL import Image, ImageTk
import mysql.connector
import random
import psutil
from datetime import date
from tkinter import ttk
from GSIMSPac import fun
from GSIMSPac import Product
from GSIMSPac import Partys
from GSIMSPac import PartyReports
from GSIMSPac import PurchaseDC
from GSIMSPac import PurchaseInvoice
from GSIMSPac import Reports
from GSIMSPac import SaleBill
from GSIMSPac import SaleReport
from GSIMSPac import PurchaseDCReport
from GSIMSPac import PurchaseInvoiceReport
from GSIMSPac import SaleReturn
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
# ===============================================

def home():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget,"-----------------------------------| HOME |-----------------------------------")
    fun.shortKeys(canvas_widget)
    
def itemWiseStockReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Item Wise Stock Report )")
    Reports.ItemWiseReport(canvas_widget)
    
def expWiseStockReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Expiry Wise Stock Report )")
    Reports.ExpWiseReport(canvas_widget)
    
def purchaseReturn():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Return Entry )")
    PurchaseInvoice.PurchaseReturn(canvas_widget)
        
def saleBilling():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Billing )")
    SaleBill.SaleBill(canvas_widget)

def saleReturn():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Return )")
    SaleReturn.SaleReturn(canvas_widget)

def newParty():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Add New Party )")
    Partys.NewParty(canvas_widget)
    
def partyReports():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Party Reports )")
    PartyReports.partyReports(canvas_widget)
    
def deleteparty():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Delete Party )")
    Partys.deleteParty(canvas_widget)

def purchaseDcEntry():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase D/C Entry )")
    PurchaseDC.PurchaseDc(canvas_widget)

def purchaseInvoiceEntry():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Invoice Entry )")
    PurchaseInvoice.PurchaseInvoice(canvas_widget)

def deleteProduct():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Delete Product )")
    Product.DeleteProduct(canvas_widget)
    
def saleReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Report )")
    SaleReport.SaleReport(canvas_widget)

def saleReturnReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Return Report )")
    SaleReport.SaleReturnReport(canvas_widget)
    
def saleDailyRoport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Daily Report )")
    SaleReport.SaleDailyReport(canvas_widget)

def saleMonthlyRoport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Monthly Report )")
    SaleReport.SaleMonthlyReport(canvas_widget)

def purchaseMonthlyRoport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Monthly Report )")
    PurchaseDCReport.PurchaseMonthlyReport(canvas_widget)
    
def saleReturnDailyRoport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Sale Return Daily Report )")
    SaleReport.SaleReturnDailyReport(canvas_widget)
    
def purchaseReturnDailyRoport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Return Daily Report )")
    PurchaseInvoiceReport.PurchaseReturnDailyReport(canvas_widget)
    
def purchaseDcReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( DC Report )")
    PurchaseDCReport.PurchaseDCReport(canvas_widget)
    
def purchaseInvoiceReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Invoice Report )")
    PurchaseInvoiceReport.PurchaseInvoiceReport(canvas_widget)

def purchaseReturnInvoiceReport():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Return Report )")
    PurchaseInvoiceReport.PurchaseReturnInvoiceReport(canvas_widget)
    
def purchaseDailyReporte():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Purchase Daily Report )")
    PurchaseDCReport.PurchaseDailyReport(canvas_widget)
                
def newProduct():
    fun.clearall(canvas_widget)
    fun.Headder(canvas_widget, "( Add New Product )")
    Product.AddProduct(canvas_widget)



root = Tk()
root.title("Dashbord")
root.geometry("1800x850+0+0")

canvas_widget = Canvas(root, width=800, height=500)
canvas_widget.pack(fill="both", expand=True)
canvas_widget.configure(bg='#e5e6d5')

fun.Headder(canvas_widget,"-----------------------------------| HOME |-----------------------------------")
fun.shortKeys(canvas_widget)

main_menu = Menu(root)
main_menu.configure(bg="#d5d99a")

product_menu = Menu(main_menu,tearoff=0)
product_menu.add_command(label="New Product",command=newProduct)
product_menu.add_command(label="Product Delete",command=deleteProduct)
product_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))

purchase_menu = Menu(main_menu,tearoff=0)
invoice_menu = Menu(purchase_menu,tearoff=0)
invoice_menu.add_command(label="Purchase D/C",command=purchaseDcEntry)
invoice_menu.add_command(label="Purchase Invoice",command=purchaseInvoiceEntry)
invoice_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
purchase_menu.add_cascade(label="Purchase",menu=invoice_menu)
perchasereport_menu = Menu(purchase_menu,tearoff=0)
perchasereport_menu.add_command(label="Purchase D/C Reports",command=purchaseDcReport)
perchasereport_menu.add_command(label="Purchase Invoice Reports",command=purchaseInvoiceReport)
perchasereport_menu.add_command(label="Purchase Return Reports",command=purchaseReturnInvoiceReport)
perchasereport_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
purchase_menu.add_cascade(label="Reports",menu=perchasereport_menu)
purchase_menu.add_separator()
purchase_menu.add_command(label="Purchase Return",command=purchaseReturn)
purchase_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))

sale_manu = Menu(main_menu,tearoff=0)
sale_manu.add_command(label="Sale Bill",command=saleBilling)
sale_ReportMenu = Menu(sale_manu,tearoff=0)
sale_ReportMenu.add_command(label="Sale Report",command=saleReport)
sale_ReportMenu.add_command(label="Sale Return Report",command=saleReturnReport)
sale_ReportMenu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
sale_manu.add_cascade(label="Reports",menu=sale_ReportMenu)
sale_manu.add_separator()
sale_manu.add_command(label="Sale Return",command=saleReturn)
sale_manu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))

party_manu = Menu(main_menu,tearoff=0)
party_manu.add_command(label="New Party",command=newParty)
party_manu.add_command(label="Party Reports",command=partyReports)
party_manu.add_command(label="Party Delete",command=deleteparty)
party_manu.add_separator()
party_manu.add_command(label="Customer")
party_manu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))

report_manu = Menu(main_menu,tearoff=0)
report_manu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))

stockRep_menu = Menu(report_manu,tearoff=0)
stockRep_menu.add_command(label="Item Wise Stock Report",command=itemWiseStockReport)
stockRep_menu.add_command(label="Exp. Date Wise Stock",command=expWiseStockReport)
stockRep_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
report_manu.add_cascade(label="Stock Report",menu=stockRep_menu)

dailyRegis_menu = Menu(report_manu,tearoff=0)
dailyRegis_menu.add_command(label="Sale",command=saleDailyRoport)
dailyRegis_menu.add_command(label="Purchase", command= purchaseDailyReporte)
dailyRegis_menu.add_command(label="Sale Return",command=saleReturnDailyRoport)
dailyRegis_menu.add_command(label="Purchase Return",command=purchaseReturnDailyRoport)
dailyRegis_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
report_manu.add_cascade(label="Daily Register",menu=dailyRegis_menu)

monthlyRegis_menu = Menu(report_manu,tearoff=0)
monthlyRegis_menu.add_command(label="Sale", command=saleMonthlyRoport)
monthlyRegis_menu.add_command(label="Purchase",command=purchaseMonthlyRoport)
monthlyRegis_menu.add_command(label="Sale Return")
monthlyRegis_menu.add_command(label="Purchase Return")
monthlyRegis_menu.configure(bg="#e5e6d5", fg="black", activebackground="#ad995e", activeforeground="#e5e6d5", font=("Times", 10))
report_manu.add_cascade(label="Monthly Register",menu=monthlyRegis_menu)

main_menu.add_cascade(label="Home",command=home)
main_menu.add_cascade(label="Sale",menu=sale_manu)
main_menu.add_cascade(label="Purchase",menu=purchase_menu)
main_menu.add_cascade(label="Product",menu=product_menu)
main_menu.add_cascade(label="Party",menu=party_manu)
main_menu.add_cascade(label="Report", menu=report_manu)
# main_menu.add_cascade(label="Help",command=help)
main_menu.add_cascade(label="Help")

root.bind_all("<Control-h>", lambda event: home())
root.bind_all("<Control-s>b", lambda event: saleBilling()) 
root.bind_all("<Control-d>c", lambda event: purchaseDcEntry())
root.bind_all("<Control-p>i", lambda event: purchaseInvoiceEntry()) 
root.bind_all("<Control-s>r", lambda event: saleReturn()) 
root.bind_all("<Control-p>a", lambda event: newParty())
root.bind_all("<Control-p>r", lambda event: newProduct()) 
root.bind_all("<Control-x>", lambda event: root.destroy()) 
root.bind_all("<Control-c>", lambda event: itemWiseStockReport()) 
root.bind_all("<Control-e>", lambda event: purchaseMonthlyRoport()) 

root.configure(menu=main_menu)
root.mainloop()

