# 1.迭代器是惰性计算，不会一次性生成所有结果，所以能显著降低内存占用。
# 2.当数据量很大，不确定要用多少结果时，推荐使用迭代器。

import tracemalloc

# 目标：实现一个斐波那契数列的迭代器，迭代到目标次数后停止
class Fibo:
    def __init__(self, total):
        self.pre = 1
        self.cur = 1
        self.total = total  # 总共要生成多少个数
        self.index = 0  # 当前生成数的计数

    def __iter__(self):
        return self

    def __next__(self):
        # 当生成足够数量的数后，抛出异常停止迭代
        if self.index >= self.total:
            raise StopIteration
        # 斐波那契数列前2项为1
        if self.index < 2:
            value = 1
        # 数列新的结果等于前两项之和
        else:
            value = self.pre + self.cur
            self.pre = self.cur
            self.cur = value

        self.index += 1  # 计数器加1

        return value


# 目标：实现一个斐波那契数列的函数，迭代到目标次数后停止
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]

    fibo_list = [1, 1]
    for i in range(2, total):
        fibo_list.append(fibo_list[-1] + fibo_list[-2])

    return fibo_list

tracemalloc.start()
fibo1_iterator = Fibo(10000)
m1 = tracemalloc.get_traced_memory()[1]
print(f'迭代器对象的内存占用是：{m1/1024/1024}MB')

tracemalloc.start()
fibo1_list = fibo(10000)
m2 = tracemalloc.get_traced_memory()[1]
print(f'函数生成的斐波那契数字列表的内存占用是：{m2/1024/1024}MB')
