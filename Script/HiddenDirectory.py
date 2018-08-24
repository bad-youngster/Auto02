#coding:utf-8
import os

dirlist = []
filelist = []
filepath = "C:\\Data\\Project\\Auto02"
files = os.listdir(filepath)
'''
通过列表输出文件夹和文件
忽略隐藏文件
'''

for f in files:
    #忽略隐藏文件
    if (os.path.isdir(filepath + '/' + f)):

        if (f[0] == '.'):
            pass
        else:
            dirlist.append(f)

    if (os.path.isfile(filepath + '/' + f)):

        filelist.append(f)

print(dirlist,filelist)