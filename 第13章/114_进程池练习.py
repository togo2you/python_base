from concurrent.futures import ProcessPoolExecutor, as_completed
import os,time

#1 创建进程池执行器，使用submit方法提交任务，使用shutdown方法等待任务完成
#2 获取子进程执行后返回的结果，Future类的实例对象+result方法

def work(n):
    print(f'work正在执行任务{n}.............{os.getpid()}')
    if n == 1:
        time.sleep(15)
    elif n == 2:
        time.sleep(10)
    else:
        time.sleep(1)

    return f'我是任务{n}的执行结果'

def done_func(future):
    print('任务已完成', future.result())

if __name__ == '__main__':
    print('-------------------start主进程-------------------')
    #创建一个进程池执行器
    #executor = ProcessPoolExecutor(max_workers=3)

    #使用submit提交任务，只负责提交任务，不会阻塞主进程
    # future1 = executor.submit(work, 1)
    # future2 = executor.submit(work, 2)
    # future3 = executor.submit(work, 3)
    # future4 = executor.submit(work, 4)
    # future5 = executor.submit(work, 5)
    # future6 = executor.submit(work, 6)
    # future7 = executor.submit(work, 7)
    #列表推导式写法：futures = [executor.submit(work, index) ]
    # futures = [executor.submit(work, index) for index in range(1,8)]


    #若要按“完成顺序”获取执行结果，需要调用as_completed方法，但需要放到executor.shutdown(wait=True)前
    # results = [future.result() for future in as_completed(futures)]

    #shutdown的作用：使进程池不再接收新的任务
    #wait=True的租用：阻塞主进程，等待进程池中所有任务执行完毕
    # executor.shutdown(wait=True)


    #调用result方法时会阻塞当前进程等待执行结果
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    # print(future4.result())
    # print(future5.result())
    # print(future6.result())
    # print(future7.result())
    #遍历future实例对象，打印每个任务的结果
    # print(results)


    #使用add_done_callback方法，为任务添加完成时的回调函数
    #回调函数：作为参数传递、在特定时机被调用的函数，
    # future1 = executor.submit(work, 1)
    # future2 = executor.submit(work, 2)
    # future3 = executor.submit(work, 3)
    # future1.add_done_callback(done_func)
    # future2.add_done_callback(done_func)
    # future3.add_done_callback(done_func)
    #
    # executor.shutdown(wait=True)

    #使用map方法批量提交任务（注意：map方法是阻塞的，且得到结果的顺序和提交的顺序一致）
    #map方法的第一个参数是要执行的任务，第二个参数是一个可迭代对象，返回的是一个生成器
    # results = executor.map(work, [1,2,3,4,5,6,7])
    #获取results生成器中的内容，会阻塞主进程，按提交顺序得到执行结果
    # print(list(results))
    #
    # executor.shutdown(wait=True)

    #使用with：进程池的“自动回收”写法，离开 with 代码块时自动执行 shutdown(wait=True)
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(work, [1, 2, 3, 4, 5, 6, 7])
        print(list(results))




    print('-------------------end主进程-------------------')















