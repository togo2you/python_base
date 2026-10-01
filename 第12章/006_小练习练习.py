import os
import time

# #练习1：将一个二进制文件复制到指定位置
# #源文件
# source = "./music.mp3"
# #目标目录
# target = "D:/media"
#
# #若目标目录不存在，则创建该目录
# if not os.path.isdir(target):
#     os.makedirs(target)
#
# with open(source, 'rb') as f1, open(target + '/' + 'music_copy.mp3', 'wb') as f2:
#     # 若二进制文件较大，内存开销较大
#     # data = f1.read()
#     # f2.write(data)
#
#     #二进制文件若已读取完，再读取返回的是空字节b''，转为布尔值是False
#     # f1.read()
#     # data = f1.read()
#     # print(data)
#
#     while True:
#         data = f1.read(1024) #每次只读取1KB的二进制内容
#         if not data: #若文件读取完毕了，则跳出循环
#             break
#         f2.write(data) #向目标文件中写入内容
#

# 练习2：日志记录
#   1.用户输入用户名和密码后，程序进行校验：
#   2.用户名不存在，提示“用户名未注册”，并记录日志。
#   3.用户名存在，但密码错误，提示“密码错误”，并记录日志。
#   4.用户名和密码均正确，提示“登录成功”，并记录日志。

users = {
    '张三': '123456',
    '李四': '456789',
    '王五': '789456'
}

while True:
    username = input('请输入用户名：')
    password = input('请输入密码：')

    # 获取当前时间并格式化
    now_time = time.strftime('%Y/%m/%d %H:%M:%S')

    if username not in users.keys():
        print('用户名未注册')

        with open('log.txt', 'at', encoding='utf-8') as log:
            log.write(f'{now_time} {username} 登录失败（用户未注册）\n')

        continue

    if users[username] != password:
        print('用户密码输入错误')

        with open('log.txt', 'at', encoding='utf-8') as log:
            log.write(f'{now_time} {username} 登录失败（用户密码输入错误）\n')

        continue

    else:
        print('用户名密码正确，登录成功！')

        with open('log.txt', 'at', encoding='utf-8') as log:
            log.write(f'{now_time} {username} 登录成功\n')

        continue

#踩git大坑恢复留念