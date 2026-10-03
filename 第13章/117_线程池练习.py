import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id, RLock

# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     time.sleep(1)
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     executor.submit(work, 1, lock)
#     executor.submit(work, 2, lock)
#     executor.submit(work, 3, lock)
#     executor.submit(work, 4, lock)
#     executor.submit(work, 5, lock)
#     executor.submit(work, 6, lock)
#     executor.submit(work, 7, lock)
#     # shutdown 的作用：不再接收新的任务。
#     # wait=True 的作用：阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#     print('---------end-------------')


#2、获取子线程执行后的返回结果，submit返回的实例对象+result方法
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#     # 使用 submit 方法提交任务（submit 只负责“提交任务”，不会阻塞主线程）
#     # executor.submit(work, 1, lock)
#     # executor.submit(work, 2, lock)
#     # executor.submit(work, 3, lock)
#     # executor.submit(work, 4, lock)
#     # executor.submit(work, 5, lock)
#     # executor.submit(work, 6, lock)
#     # executor.submit(work, 7, lock)
#
#     futures = [executor.submit(work, n, lock) for n in range(1, 8)]
#
#     #阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     for future in futures:
#         print(future.result())
#
#     print('---------end-------------')

#3、使用as_completed获取执行结果
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     futures = [executor.submit(work, n, lock) for n in range(1, 8)]
#     #收集每个线程返回的结果
#     result_list = []
#     #将每个线程执行的结果，存入result_list
#     for future in as_completed(futures):
#         result_list.append(future.result())
#
#     #阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     print(result_list)
#
#
#     print('---------end-------------')


#4、使用add_done_callback方法，为任务添加完成时的回调函数
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start-------------')
#
#     def done_func(f):
#         result_list.append(f.result())
#
#     # 创建一个线程池执行器
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     #收集每个线程的执行结果
#     result_list = []
#
#     #使用submit提交任务，并指定回调函数
#     for index in range(1, 8):
#         f = executor.submit(work, index, lock)
#         f.add_done_callback(done_func)
#
#
#
#     #阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     print(result_list)
#
#
#     print('---------end-------------')


#5、使用map方法批量提交任务
# def work(n, lock):
#     with lock:
#         print(f'work正在执行任务{n}.........{get_native_id()}')
#     if n == 1:
#         time.sleep(15)
#     elif n == 2:
#         time.sleep(10)
#     else:
#         time.sleep(1)
#     return f'任务{n}的结果'
#
# if __name__ == '__main__':
#     print('---------start主线程启动-------------')
#
#     executor = ThreadPoolExecutor(3)
#     # 创建线程锁
#     lock = RLock()
#
#     #使用map方法批量提交任务，其返回是一个生成器，获取其结果时会阻塞
#     result = executor.map(work, [1,2,3,4,5,6,7], [lock]*7)
#     print(list(result))
#
#     #阻塞主线程，等待线程池中所有任务执行完毕。
#     executor.shutdown(wait=True)
#
#     print('---------end主线程结束-------------')
#


#6、使用 with：线程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
def work(n, lock):
    with lock:
        print(f'work正在执行任务{n}.........{get_native_id()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)
    return f'任务{n}的结果'

if __name__ == '__main__':
    print('---------start主线程启动-------------')

    with ThreadPoolExecutor(3) as executor:
        # 创建线程锁
        lock = RLock()

        #使用map方法批量提交任务，其返回是一个生成器，获取其结果时会阻塞
        result = executor.map(work, [1,2,3,4,5,6,7], [lock]*7)
        print(list(result))

    print('---------end主线程结束-------------')




