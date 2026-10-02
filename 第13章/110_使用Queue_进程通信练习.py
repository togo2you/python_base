import time
from multiprocessing import Process, Queue


#子进程1：向队列中添加数据
def test1(q):
    for index in range(5):
        print(f'【test1】放入数据：{index}')
        q.put(index)
        time.sleep(0.5)

#子进程2：从队列中取出数据
def test2(q):
    for index in range(5):
        res = q.get()
        print(f'【test2】取出数据：{res}')
        time.sleep(0.5)


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=test1, args=(q,))
    p2 = Process(target=test2, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()