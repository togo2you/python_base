import os
import time
from multiprocessing import Process
from threading import get_native_id, Thread, RLock

class SpeakThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在说话{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
            time.sleep(1)

class StudyThread(Thread):
    def __init__(self, lock, **kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(5):
            with self.lock:
                print(f'我在学习{index}, 进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')
            time.sleep(1)

if __name__ == '__main__':
    print(f'-------------start主进程-------------进程pid是:{os.getpid()}, 线程编号:{get_native_id()}')

    lock = RLock()

    #继承Thread类，创建2个线程
    t1 = SpeakThread(lock)
    t2 = StudyThread(lock)

    #调用线程对象的start方法，会立刻将该线程交给OS进行调度
    t1.start()
    t2.start()
    #阻塞主线程，等待其他线程执行完毕
    t1.join()
    t2.join()

    print('-------------end主进程-------------')