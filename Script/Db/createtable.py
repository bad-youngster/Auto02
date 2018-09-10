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
cursor.execute("drop table if exists WATCHDOGINFO")

sql = """CREATE TABLE TESTINFO(
        id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
        HOST_NAME CHAR(10) NOT NULL,
        HOST_IP CHAR(50),
        HOST_CREATE varchar(50),
        CREATE_USER varchar(50),
        CREATE_PATH varchar(50)
        )
"""

sql1 = """
        CREATE TABLE WATCHDOGINFO(
        ID INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
        WATCHSOURDIR VARCHAR(20) NOT NULL ,
        WATCHOBJECT varchar(20) not null ,
        WATCHIP varchar(20) not null ,
        WATCHNAME varchar(20)
        
        )

"""

# cursor.execute(sql)
cursor.execute(sql)
cursor.execute(sql1)
db.commit()
db.close()


