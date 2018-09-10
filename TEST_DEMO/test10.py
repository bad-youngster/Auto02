#coding:utf-8
import datetime
import os
import pwd
import time

import pymysql

host_name = "pymysql"
host_ip = "192.168.56.102"
nowtime = datetime.datetime.now()
create_user = pwd.getpwuid(os.getegid())[0]

nowtime1 = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
# print(nowtime1)
project_name = ["lypt", "agent"]


db = pymysql.connect("192.168.56.102","root","123456","pymysql")
cursor = db.cursor()
for project_path in project_name:
    newfilepath = ('/tmp/%s/%s' % (project_path, nowtime1))
    # if not os.path.exists(newfilepath):
    #     os.makedirs(newfilepath)
    sql1 = "INSERT INTO TESTINFO(HOST_NAME,HOST_IP,\
        HOST_CREATE,CREATE_USER,CREATE_PATH)\
        VALUES ('%s','%s','%s','%s','%s')"\
        % (host_name,host_ip,nowtime,create_user,newfilepath)
    print(sql1)

    # cursor.execute(sql1)
    if not os.path.exists(newfilepath):
        cursor.execute(sql1)
        os.makedirs(newfilepath)
        db.commit()
db.close()



