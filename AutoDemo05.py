#coding:utf-8
import datetime
import os
file_dir = os.getcwd()
# # print(file_dir)

a = ['q','']

for aa in a:
    if aa is not None:
        print (aa)





def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        # if dirs is not None:
        #     print(dirs)

        # print(root)
        print(dirs)


file_name(file_dir)
# print(a)
