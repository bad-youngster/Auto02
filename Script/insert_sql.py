#coding:utf-8
# from Script.test import cursor,db,sql
import pymysql

host_name = "pymysql"
host_ip = "192.168.56.102"

db = pymysql.connect("192.168.56.102","root","123456","pymysql")
cursor = db.cursor()

sql1 = "INSERT INTO TESTINFO(HOST_NAME,HOST_IP) VALUES ('%s','%s')" % (host_name,host_ip)
print(sql1)
try:
    # cursor.execute(sql)
    cursor.execute(sql1)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)


db.close()


