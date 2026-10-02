import time
from multiprocessing import Process, Pipe


def test1(con1):
    time.sleep(2)
    con1.send(100)
    print('test1发送了100')


def test2(con2):
    data = con2.recv()
    print(f'test2接收了{data}')



if __name__ == '__main__':
    #Pipe类的实例对象是一个元组，里面有2个元素，分别表示管道的两端
    #当Pipe实例对象的属性duplex为False时，返回元组的第一个元素只能接收，第二个元素只能发送
    con1, con2 = Pipe(duplex=False)

    p1 = Process(target=test1,args=(con1,))
    p2 = Process(target=test2,args=(con2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()