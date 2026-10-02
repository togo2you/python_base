# 队列(Queue)是：一种“先进先出”的数据结构（先放进去的数据，一定会先取出来）
import time
from multiprocessing import Queue, Process
#从multiprocessing模块导入的Queue是能够实现进程间通信的队列

#创建一个队列（不限制大小）
# q1 = Queue()

#创建一个队列（最多能保存3个元素）
# q2 = Queue(3)

#1、put方法：可以向队列里放入数据（入队）
# q1.put(10)
# q1.put(20)
# q1.put(30)

#2、get方法，可以从队列里取出数据（出队）
# print(q1.get())
# print(q1.get())
# print(q1.get())

#3、empty方法用于判断队列是否为空
# res = q1.empty()
# print(res)

#4、full判断队列是否已满
# q2.put(10)
# q2.put(20)
# q2.put(30)


# res = q2.full()
# print(res)

#5、qsize用于获取队列长度
# res = q2.qsize()
# print(res)

#6、队列具备等待模式
#（1）当队列已满，继续put，就会进入等地啊模式，等待调用get方法取走队首元素
# q2.put(400)
# print('放入完毕')
#（2）当队列已满，执行：put(元素, timeout=秒数)，就会等待指定秒数，超时后会抛出queue.Full异常
# q2.put(400,timeout=3,block=False)
# print('放入完毕')
#（3）put_nowait方法，有直接向队列中添加元素，不会进入等待模式，若队列已满则直接抛出queue.Full异常
# q2.put_nowait(400)  #put_nowait等价于put(obj,block=False)
# print('放入完毕')

#（4）当从空队列中get取元素时，也会进入等待模式
# q2.get()
# q2.get()
# q2.get()

# (1).当队列已空，继续 get，就会进入等待模式。x
# q2.get()

# (2).当队列已空，执行 get(timeout=秒数)，就会等待指定秒数,超时后会抛出queue.Empty异常
# q2.get(timeout=3)

# (3).get_nowait 方法，会直接读取队列中的元素，不会进入等待模式，若队列已空，会抛出异常
# 备注：get_nowait 等价于 get(block=False)
# q2.get_nowait()
# q2.get(block=False)

def test(q):
    time.sleep(3)
    res = q.get()
    print(f'我从队列中取出了元素：{res}')



# 通过多进程，演示一下：当队列满了以后，再次put会等待，当有人从队列中取出元素后，put会继续。
if __name__ == '__main__':
    q = Queue(2)

    q.put('尚硅谷')
    q.put('atguigu')
    print(f'队列是否已满{q.full()}')

    #开启子进程，每隔3秒从队列中取出一个元素
    p1 = Process(target=test,args=(q,))
    p1.start()

    print('即将向已满的队列中添加元素........')
    q.put('hello')
    print('目前队列中有的元素是：')
    print(q.get())
    print(q.get())







