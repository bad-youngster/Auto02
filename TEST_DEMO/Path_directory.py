#coding:utf-8
import os
import time

from Db.insert_sql import cursor, sql1, db

nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))


# def created(self):
#     project_name = ["lypt", "agent"]
#     for project_path in project_name:
#         newfilepath = ('/tmp/%s/%s' % (project_path, nowtime))
#         if not os.path.exists(newfilepath):
#             os.makedirs(newfilepath)
#
#
# createdirectory = created(nowtime)
# print(createdirectory)
project_name = ["lypt", "agent"]
for project_path in project_name:
    newfilepath = ('/tmp/%s/%s' % (project_path, nowtime))
    if not os.path.exists(newfilepath):
        os.makedirs(newfilepath)
        try:
            # cursor.execute(sql)
            cursor.execute(sql1)
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)
db.close()