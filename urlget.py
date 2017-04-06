import urllib.request
import pathlib
import os
import pyquery
from pyquery import PyQuery as pq
import re
import mysql.connector
import sys
import time


config={
        'host': 'localhost',
        'port': 3306,
        'database': 'housedata',
        'user': 'root',
        'password': '1234',
       }

response = urllib.request.urlopen('http://sh.lianjia.com/ershoufang/q5011000015938')

# p= pathlib.path('d:/project/python/lianjiacontent')
# print(content.read().decode('utf-8'))
# fp = open('lianjiacontent.txt','bw')
# fp.write(content.read())
# fp.close()

content = response.read().decode('utf-8')
pattern = re.compile(r'<div.*?where">.*?<span.*?>(.*?)</span>.*?<span.*?</span>.*?<span>(.*?)平.*?</span>.*?<div.*?price-pre">(.*?)元/平</div>',re.S)
# pattern = re.compile(r'where')
items = re.findall(pattern,content)

cnx = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='housedata')
cur = cnx.cursor()
date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
for item in items:
    data = (item[0], item[1],int(item[2]),date)
    stmt_insert = "INSERT INTO  houseprice(description,acreage,unitprice,insertdate) VALUES (%s, %s, %s,%s)"
    cur.execute(stmt_insert, data)

cnx.commit()
cur.close()
cnx.close()

# doc = pq(filename='lianjiacontent.txt')

# print(doc('head').text())