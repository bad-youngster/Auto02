#coding:utf-8
import pymysql
host_name = "pymysql"
host_ip = "192.168.56.102"

db = pymysql.connect("192.168.56.102","root","123456","pymysql")
cursor = db.cursor()
# cursor.execute("select version()")
# # data = cursor.fetchone()
# # print("database version %s " % data)
# # db.close()

cursor.execute("DROP TABLE IF EXISTS TESTINFO")

sql = """CREATE TABLE TESTINFO(
        id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
        HOST_NAME CHAR(10) NOT NULL,
        HOST_IP CHAR(10)       
        )
"""

# cursor.execute(sql)



