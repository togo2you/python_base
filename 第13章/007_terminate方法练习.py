import os
import time
from multiprocessing import Process
def speak():
    try:
        for index in range(10):
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)
    # 注意：使用 terminate 终止进程，不会引起 finally 执行！
    finally:
        print('我是finally里的逻辑')

def study():
    for index in range(15):
        print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
        time.sleep(1)

if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')
    p1 = Process(target=speak)
    p2 = Process(target=study)

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()

    time.sleep(3)
    print('我是主进程，我准备强制终止p1进程')
    p1.terminate() #进程的terminate终止操作是异步执行的，是一种暴力终止进程的操作
    p1.join() #阻塞当前进程，待p1进程执行完毕后再继续执行
    print(p1.is_alive())

    print('我是主进程中的【最后一行】打印')