# coding:utf-8
import paramiko
from Script.Operation import ScpConnt
from Script.Operation import *


host = '172.16.31.200'
user = "root"
password = "CentOS@123"
port = 22

# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect(host,port,user,password)
#
# cmd = input("输入你要执行的命令:>>")
#
# (stdin,stdout,stderr) = ssh.exec_command(cmd)
#
# st = stdout.readlines()



if __name__ == "__main__":
    massge = '''
    \033[31;1m
    执行命令 >> 输入command
    上传文件 >> 输入put
    下载文件 >> 输入get
    退出 >> 输入quit\033[0m
    '''
    getattr(connection,"ssh_connection")()
    while True:
        print(massge)
        inp = input("action:>>")

        if hasattr(connection, inp):
            getattr(connection, inp)()
            print("执行成功")

        elif inp == "quit":
            getattr(connection,"close")()
            exit()
