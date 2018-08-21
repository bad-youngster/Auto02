# coding:utf-8
import paramiko
import getpass

print("\033[32;1m****开始配置机器*****\033[0m")

host_ip = '172.16.31.200'      #input("目标主机IP:")
user = "root"     #input("主机用户名：")
password = "CentOS@123"      #getpass.getpass("主机密码:")
port = 22   #input("目标端口：")

class Tools(object):
    def __init__(self,host_ip,port,user,password):
        self.user = user
        self.password = password
        self.port = port
        self.host_ip = host_ip

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host_ip,self.port,self.user,self.password)
            print("连接已建立")

        except Exception as e:
            print("未连接到目标主机")

    def cmd(self):
        try:
            cmd = input("请输入执行命令:>>")
            (stdout,stdin,stderr) = self.ssh.exec_command(cmd)
            st = stdout.readlines()

            for index,aa in enumerate(st):
                print(index,aa)


        except Exception as e:
            print("输入的命令有误！")

    def input(self):
        self.local_file_abs = input("本地文件地址:>>")
        self.remote_file_abs = input("远程文件地址:>>")

    def put(self):

        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        self.input()
        sftp.put(self.local_file_abs,self.remote_file_abs)
    def get(self):
        sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
        sftp = self.ssh.open_sftp()
        self.input()
        sftp.get(self.remote_file_abs,self.local_file_abs)

    def close(self):
        self.ssh.close()
        print("关闭连接")


connpool = Tools(host_ip,port,user,password)

if __name__ == "__main__":
    massge = '''
    \033[31;1m
    执行命令 >> 输入cmd
    上传文件 >> 输入put
    下载文件 >> 输入get
    退出 >> 输入q\033[0m
    '''
    getattr(connpool,"connect")()
    while True:
        print(massge)
        inp = input("action:>>")

        if hasattr(connpool, inp):
            getattr(connpool, inp)()

        if inp == "q":
            getattr(connpool,"close")()
            exit()
        else:
            print("输入参数没有选项，重新输入:>>")


