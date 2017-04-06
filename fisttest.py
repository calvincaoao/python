import xlrd
import mysql.connector
import sys 


config={
        'host': 'localhost',
        'port': 3306,
        'database': 'omniturereport',
        'user': 'root',
        'password': '1234',
       }

cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='omniturereport')
cur = cnx.cursor()

data = xlrd.open_workbook('reportdata.xls')
table = data.sheets()[0]
nrows = table.nrows

for rownum in range(1,nrows):
    str = table.row_values(rownum)[0]
    pa1 = int(str.strip('Communication:Detail:').strip())
    pa2 = int(table.row_values(rownum)[1])
    pa3 = int(table.row_values(rownum)[2])
    #cur.execute('select * from cmlcpv')
    #results = cur.fetchall()
    names = (pa1,pa2,pa3,'20170322')
    stmt_insert = "INSERT INTO  cmlcpv(pageid, levelcode, pageviews, packageid) VALUES (%s, %s, %s,%s)"
    cur.execute(stmt_insert,names)
    
cnx.commit()
cur.close()
cnx.close()

 
