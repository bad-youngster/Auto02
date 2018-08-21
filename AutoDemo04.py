import datetime
import os

#获取路径，为上传路径
locallistfilepath = os.getcwd()
#print(locallistfilepath)
#获取路径下是否有目录
files = os.path.exists(locallistfilepath)

# print(files)

if files == True:
    print("文件存在")
else:
    print("文件不存在")

#列出路径下文件和文件夹
filelist = os.listdir(locallistfilepath)

# print(filelist)
#输出远程拷贝路径文件和创建时间

def filelists(file_dir):
    for root,dirs,files in os.walk(file_dir):
        print(root)



        # 处理时间戳，转化成时间格式
        # filetime = os.path.getctime(filename)
        #
        # data = datetime.datetime.fromtimestamp(filetime)
        #
        # print(filename, data.strftime('%Y-%m-%d %H:%M:%S'))
        #





