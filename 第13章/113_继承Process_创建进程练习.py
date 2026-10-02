from multiprocessing import Process
import time,os

# Process.run() 是子进程的“入口函数”，start() 负责启动新进程并让新进程去执行 run()。
# 默认 run() 会调用你传入的 target；你也可以继承 Process 重写 run() 来自定义子进程要做什么。
# 直接调用 run() 不会创建新进程，必须用 start()

class SpeakProcess(Process):
    #自定义类实现进程，必须包含run方法
    def run(self):
        for index in range(10):
            print(f'我在说话{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)


class StudayProcess(Process):
    #自定义类实现进程，必须包含run方法
    def run(self):
        for index in range(15):
            print(f'我在学习{index}, 进程pid是:{os.getpid()}, 我的父进程是:{os.getppid()}')
            time.sleep(1)


if __name__ == '__main__':
    print('我是主进程中的【第一行】打印')

    p1 = SpeakProcess()
    p2 = StudayProcess()

    #进程Process实例对象的start方法会先去向OS申请进程，然后执行run方法
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('我是主进程中的【最后一行】打印')












