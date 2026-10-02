# 进程之间不共享内存，因此也就不共享任何变量。
#特殊的比如 锁Lock是跨进程的
from multiprocessing import Process

#创建一个全局变量num
# num = 100 #不可变对象
# names = [] #可变对象

def test1(num,names):
    # global num,names
    # num += 10
    names.append('张三')
    print(f'我是 test1 进程，操作之后的num是{num}，names是{names}')

def test2(num,names):
    # global num,names
    # num -= 10
    names.append('李四')
    print(f'我是 test2 进程，操作之后的num是{num}，names是{names}')

if __name__ == "__main__":
    num = 100  # 不可变对象
    names = []  # 可变对象

    print('主进程中的【第一行】代码')
    p1 = Process(target=test1,args=(num,names))
    p2 = Process(target=test2,args=(num,names))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('主进程中的【最后一行】代码', num,names)