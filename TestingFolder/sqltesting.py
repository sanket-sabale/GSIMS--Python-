import calendar
from tkinter import *
import mysql.connector
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import messagebox
mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
cursor = mydb.cursor()

fromdate = datetime.strptime(f"{2024}-{str(1)}-{1}", "%Y-%m-%d")
todate = datetime.strptime(f"{2024}-{str(1)}-{31}", "%Y-%m-%d")
# cursor.execute("select quantity,returnqty,availableqty,amount,status,productname from purchase where productno = %s and (status = %s or status = %s)",[13,"dc","inv"])
cursor.execute("select quantity,returnqty,availableqty,amount,status,productname from purchase where productno = %s and (status = %s or status = %s) and ((purchasedcdate > %s and purchasedcdate < %s) or (purchasedate > %s and purchasedate < %s))",[13,"dc","inv",fromdate,todate,fromdate,todate])

rowdata = cursor.fetchall()
print("ok")
for data in rowdata:
    print(data)