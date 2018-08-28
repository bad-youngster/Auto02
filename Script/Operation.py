#coding:utf-8
import paramiko
from Script.SshServer import host,port,user,password
from scp import SCPClient


user = "root"

class ScpConnt(object):
    #初始化连接
    def __init__(self,host,user,password,port):

        self.host = host
        self.port = port
        self.user = user
        self.password = password
    #ssh连接
    def ssh_connection(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(host,port,user,password)
            print("连接成功！")
        except Exception as e:
            print("连接失败!")

    #定义执行命令
    def command(self):
        try:
            cmd = input("输入你要执行的命令:>>")
            (stdin,stdout,stderr) = self.ssh.exec_command(cmd)
            st = stdout.readlines()
            for index,tt in enumerate(st):
                print(index,tt)
        except Exception as e:
            print("输入命令不存在!")
    #定义上传路径和下载路径
    def putfilepath(self):
        try:
            self.put_remote_file_path = input("输入远程绝对上传路径:>>")
            self.put_local_file_path = input("输入本地文件绝对路径:>>")
            # self.remote1_file_path = input("输入远程下载文件绝对路径:>>")
            print("路径存在")
        except Exception as e:
            print("路径不存在")
    def getfilepath(self):
        try:
            self.get_remote_file_path = input("输入远程绝对下载路径:>>")
            self.get_local_file_path = input("输入本地绝对下载路径:>>")
            print("路径存在")
        except Exception as e:
            print("路径不存在")
    #上传文件
    def put(self):
        try:
            #定义连接的socket时间
            scpsocket = SCPClient(self.ssh.get_transport(),socket_timeout=30.0)
            #定义远程目录
            # remotfile = "/root/"
            #定义本地路径
            # localfile = "a1.txt"
            # scpsocket.put(localfile,remotfile)
            self.putfilepath()
            scpsocket.put(self.put_local_file_path,self.put_remote_file_path)
            print("上传成功")

        except Exception as e:
            print("上传失败，请检查目录是否有权限!")

    def get(self):
        try:
            scpsocket = SCPClient(self.ssh.get_transport(),socket_timeout=30.0)
            self.getfilepath()
            scpsocket.get(self.get_remote_file_path,self.get_local_file_path)
            print("下载成功")
        except Exception as e:
            print("下载失败,请检查目录是否有权限!")

    #结束进程
    def close(self):
        self.ssh.close()
        print("结束连接!")
#调用class的连接
connection = ScpConnt(host,port,user,password)