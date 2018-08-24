# coding:utf-8
import time
import os.path

nowtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))

# print(nowtime)
# newfilepath = nowtime
class timefile(object):
    def __init__(self,nowtime):
        self.nowtime = nowtime

    def timefilepath(self):
        newfilepath = self.nowtime

        if not os.path.exists(newfilepath):
            a = os.mkdir(newfilepath)

filepath = timefile(nowtime)

# print(filepath)

if __name__ =="__main__":
    filepath.timefilepath()