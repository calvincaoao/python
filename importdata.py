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

data = xlrd.open_workbook('summary.xlsx')
table = data.sheets()[0]
nrows = table.nrows

for rownum in range(1,nrows):
    str = table.row_values(rownum)[0]
    #pa1 = int(str.strip('Communication:Detail:').strip())
    pa1 = int(table.row_values(rownum)[0])
    pa2 = table.row_values(rownum)[1]
    pa3 = table.row_values(rownum)[2]
    paf = table.row_values(rownum)[3]
    #cur.execute('select * from cmlcpv')
    #results = cur.fetchall()
    names = (pa1,pa2,pa3,paf)
    stmt_insert = "INSERT INTO  pageinfo(pageid,pagetitle,bd,ed) VALUES (%s, %s, %s,%s)"
    cur.execute(stmt_insert,names)
    
cnx.commit()
cur.close()
cnx.close()

 
