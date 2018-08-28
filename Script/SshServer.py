# coding:utf-8

from Script.Operation import user

print(user)


host = '172.16.31.200'
user = "root"
password = "CentOS@123"
port = 22


#
# if __name__ == "__main__":
#     massge = '''
#     \033[31;1m
#     执行命令 >> 输入command
#     上传文件 >> 输入put
#     下载文件 >> 输入get
#     退出 >> 输入quit\033[0m
#     '''
#     getattr(connection,"ssh_connection")()
#     while True:
#         print(massge)
#         inp = input("action:>> ")
#
#         if hasattr(connection, inp):
#             getattr(connection, inp)()
#             print("执行成功")
#
#         elif inp == "quit":
#             getattr(connection,"close")()
#             exit()
