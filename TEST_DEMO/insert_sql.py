#coding:utf-8
import datetime
import time
import pwd,os
import pymysql
# from TEST_DEMO.Path_directory import newfilepath
# print(newfilepath)

nowtime1 = time.strftime('%Y-%m-%d',time.localtime(time.time()))

host_name = "pymysql"
host_ip = "192.168.56.102"
nowtime = datetime.datetime.now()
create_user = pwd.getpwuid(os.getegid())[0]
# project_name = ["lypt", "agent"]
# for project_path in project_name:
#     newfilepath = ('/tmp/%s/%s' % (project_path, nowtime))
#     if not os.path.exists(newfilepath):
#         os.makedirs(newfilepath)



db = pymysql.connect("192.168.56.102","root","123456","pymysql")
cursor = db.cursor()

project_name = ["lypt", "agent"]
for project_path in project_name:
    newfilepath = ('/tmp/%s/%s' % (project_path, nowtime1))
    if not os.path.exists(newfilepath):
        os.makedirs(newfilepath)

sql1 = "INSERT INTO TESTINFO(HOST_NAME,HOST_IP,\
        HOST_CREATE,CREATE_USER,CREATE_PATH)\
         VALUES ('%s','%s','%s','%s','%s')"\
       % (host_name,host_ip,nowtime,create_user,newfilepath)
print(sql1)
try:

    # cursor.execute(sql)
    cursor.execute(sql1)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

db.close()

