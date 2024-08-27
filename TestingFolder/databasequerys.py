import mysql.connector


mydb = mysql.connector.connect(host='localhost', user='root', password='myPluto@18021930', database= 'gsimsdb')
cur = mydb.cursor()

# query ="delete from purchase where returnqty = %s"
# cur.execute(query,[0])

# query = "update purchase set salereturnqty = %s where status = %s"
# cur.execute(query,[0,"inv"])

# query = "update partys set debit = %s, credit = %s"
# cur.execute(query,[0,0])

mydb.commit()