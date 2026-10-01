# open 函数最常用的三个参数如下：
#   1.file：要操作的文件路径
#   2.mode：文件的打开模式
#       r ：读取（默认值）
#       w ：写入，并先截断文件
#       x ：排它性创建，如果文件已存在，则创建失败
#       a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#       b ：二进制模式
#       t ：文本模式（默认值）
#       + ：打开用于更新（读取与写入）
#   3.encoding：字符编码
import time
from dataclasses import field

#创建文件对象
#file = open(file='a.txt', mode='rt',encoding='utf-8')

# #用循环配合多次调用read去逐步读取文件
# while True:
#     result = file.readline()
#     if result == '':
#         break
#     print(result,end='')

#如果指定了正整数 hint，则读取的总字符数（文本模式）或字节数（二进制模式）超过 hint 时停止，但会完整读取当前行
# result = file.readlines(1)
#
# print(result)

# for line in file.readlines():
#     print(line, end='')

# r1 = file.readline(5)
# r2 = file.readline(3)
# r3 = file.readline(3)
#
# print(r1)
# print(r2)
# print(r3)

#关闭文件
# file.close()


# ⭐️最佳实践：使用 with 上下文管理器，结合for循环遍历，逐行读取文件。
with open(file='a.txt', mode='rt', encoding='utf-8') as file:
    print(repr(file.readline()))

# read() 返回整个文件内容作为一个字符串，遍历它是逐字符
# readlines() 返回所有行组成的列表，遍历它是逐行
# 因为文件对象本身也是可迭代的，直接 for line in f 也是逐行，但惰性读取、内存友好，是处理大文件的首选

file = open(file='a.txt', mode='rt', encoding='utf-8')

for line in file:
    print(line)

for line in file:
    print(line)