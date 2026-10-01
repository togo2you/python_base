# 文件操作的核心 ———— open函数：它可以打开或创建文件，且支持多种操作模式，返回值是『文件对象』。
# open 函数最常用的三个参数如下：
#   1.file：要操作的文件路径
#   2.mode：文件的打开模式
#       主模式，主模式间是互斥的
#       r ：读取（默认值）
#       w ：写入，并先截断文件
#       x ：排它性创建，如果文件已存在，则创建失败
#       a ：打开文件用于写入，如果文件存在，则在文件末尾追加内容
#       打开方式的修饰符
#       b ：二进制模式
#       t ：文本模式（默认值）
#       + ：打开用于更新（读取与写入）
#   3.encoding：字符编码
import time

#测试w模式
# with open('c.txt','wt',encoding='utf-8') as file:
#     file.write('你好')

#测试x模式
# with open('d.txt','xt',encoding='utf-8') as file:
#     file.write('你好')

#测试a模式
# with open('demo.txt','at',encoding='utf-8') as file:
#     file.write('你好1')
#     file.write('你好2')
#     file.write('你好3')
#     file.flush() # 文件对象的 flush 方法：把缓冲区中的数据，立刻写入到文件中。
#     time.sleep(10000)
#     file.write('你好4')
#     file.write('你好5')

# 在 Python 中文件写入时，并不是每写一次就立刻落盘，而是：先写到“缓冲区”里。
#真正写入磁盘一般有2中情况：1、缓冲区满；2、文件对象调用了close方法

#测试rt+
# with open('a.txt','rt+',encoding='utf-8') as file:
#     file.seek(3,0)
#         # seek(offset, whence)方法：用于改变文件对象指针的位置，参数说明如下：
#         #   offset：偏移量，要移动多少距离，是字节的偏移量，不是字符的偏移量
#         #   whence：参考点，从哪里开始计算偏移，有三种取值：
#         #       0：从文件开头计算（默认值）
#         #       1：从当前位置计算
#         #       2：从文件末尾计算
#     #对于文件指针后面的原有字符，write() 不会自动删除或移动它们，而是直接覆盖从指针位置开始的字节
#     file.write('你你你你你你你你')

#测试wt+
# with open('a.txt','wt+',encoding='utf-8') as file:
#     file.write('你好') #文件指针在头，覆盖写完成后在文件末尾
#     file.seek(0,0)
#     result = file.read()
#     print(result)

#测试xt+
# with open('demo2.txt','xt+',encoding='utf-8') as file:
#     file.write('你好') #文件指针在头，覆盖写完成后在文件末尾
#     file.seek(0, 0)
#     result = file.read()
#     print(result)

#测试at+
with open('demo2.txt','at+',encoding='utf-8') as file:
    file.write('你好') #文件指针在头，覆盖写完成后在文件末尾
    file.seek(0, 0)
    result = file.read()
    print(result)