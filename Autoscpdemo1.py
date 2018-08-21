import paramiko
from scp import SCPClient

host = '172.16.31.200'
user = "root"
password = "CentOS@123"
port = 22

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host,port,user,password)

cmd = input("输入你要执行的命令:>>")

(stdin,stdout,stderr) = ssh.exec_command(cmd)

st = stdout.readlines()

scpclient = SCPClient(ssh.get_transport(),socket_timeout=30.0)

remotepath = '/root/a.txt'

# localpath = 'a.txt'
#
# scpclient.put(localpath,remotepath)

localpath1 = 'c:\\Data\\Project\\Auto02'

scpclient.get(remotepath,localpath1)

ssh.close()

for index,tt in enumerate(st):
    print(index,tt)