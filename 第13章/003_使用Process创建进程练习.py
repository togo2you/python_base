import os
import time
from multiprocessing import Process,current_process
print(__name__)

# 定义一个 speak 函数，功能是：每隔一秒说话一次（一共说话10次）
def speak(a,b,msg):
    for index in range(10):
        print(f'{current_process().name}--我在说话{index}，进程pid是：:{os.getpid()}，父进程pid是：:{os.getppid()}')
        print(a,b)
        print(msg)
        time.sleep(1)

# 定义一个 study 函数，功能是：每隔一秒学习一次（一共学习15次）
def studay():
    for index in range(15):
        print(f'{current_process().name}--我在学习{index}，进程pid是：:{os.getpid()}，父进程pid是：:{os.getppid()}')
        time.sleep(1)

# 注意：一定要写 if __name__ == '__main__' 这个判断，原因如下：
#   1.当创建子进程时，Python 并不会把父进程内存里的 speak 函数直接交给子进程。
#   2.Python会启动一个全新的 Python 解释器进程，重新执行当前的 .py 文件（作为模块）。
#   3.在执行过程中，重新定义出一个 speak 函数，交给子进程。

if __name__ == '__main__':
    #创建两个Process类的实例对象（进程），分别是p1和p2
    # 注意点1：p1 和 p2 就对应着以后的两个子进程，在创建它们的时候，就要指定好他们要执行的任务。
    # 注意点2：此时的 p1 和 p2 只是代码层面的两个进程对象，操作系统还没有真的创建 p1 和 p2 两个进程。

    # Process的参数：
    #   🔸group： 默认值为None（应当始终为None）。
    #   🔸target：子进程要执行的可调用对象，默认值为 None。
    #   🔸name：  进程名称，默认为 None ，如果设置为 None，Python 会自动分配名字。
    #   🔸args：  给 target 传的位置参数（元组）
    #   🔸kwargs：给 target 传的关键字参数（字典）。
    #   🔸daemon：标记进程是否为守护进程，取值为布尔值（默认为 None，表示从创建方进程继承）。

    print(os.getpid())#打印主进程的pid

    p1 = Process(target=speak,name='speak_process',args=(1,12),kwargs={'msg':'hello'})
    p2 = Process(target=studay,name='studay_process')

    # 调用进程对象的 start 方法，会立刻向操作系统申请一个进程，并且会将该进程交由操作系统进行调度。
    p1.start()
    p2.start()









