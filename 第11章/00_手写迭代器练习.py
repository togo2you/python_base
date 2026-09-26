# 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）。
names = ['张三', '李四', '王五']

# it1 = iter(names)
# print(next(it1))
# print(next(it1))
# print(next(it1))

# for item in names:
#     print(item)

# for循环遍历可迭代对象的实现
it = iter(names)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break

print('-' * 8 + '前置练习' + '-' * 8)


# 手写迭代器实现需求：让for循环可以比遍历Person类的实例对象
# -------------------------------实现方式1-------------------------------
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)  # 返回的迭代器也是实例对象
#
#
# class PersonIterator:
#     def __init__(self, p):
#         # 保存外部传入的数据
#         self.p = p
#         # 设置迭代器指针的初始化状态
#         self.index = 0
#         #设置传入对象要遍历的数据
#         self.attrs = [p.name, p.age, p.gender, p.address]
#
#     #迭代器的iter()方法会返回迭代器自身
#     def __iter__(self):
#         return self
#
#     #迭代器每次调用__next__方法，会根据当前状态，返回下一个元素
#     def __next__(self):
#         #若指针超出范围，抛出StopIteration异常
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         #若指针index为超出范围，获取要返回的内容
#         value = self.attrs[self.index]
#         #更新迭代器index的位置
#         self.index += 1
#
#         return value
#

# -------------------------------实现方式2-------------------------------

class Person:
    def __init__(self, name, age, gender, address):
        # 对象的属性
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

        # 迭代器的属性，设置迭代器指针的初始位置
        self.__index = 0
        # 迭代器的属性，设置要迭代的内容
        self.__attrs = [self.name, self.age, self.gender, self.address]

    #方式2实现的Person类的实例对象即是迭代器又是可迭代对象
    def __iter__(self):  # 迭代器对象调用返回自身，可迭代对象调用返回迭代器
        self.__index = 0 #保证调用返回迭代器后，迭代器初始化；但传入的是迭代器时，会异常初始化
        return self

    def __next__(self):
        if self.__index >= len(self.__attrs):
            raise StopIteration
        value = self.__attrs[self.__index]
        self.__index += 1

        return value

p1 = Person('张三', 18, '男', '北京昌平区')

# 目标：将Person类的实例对象变为可迭代对象
# 要求1：可迭代对象要能调用到__iter__方法，调用后返回的是迭代器；迭代器调用__iter__方法返回自身
# 要求2：迭代器协议：1.能被 iter() 接收；2.能被 next() 一步一步取值

for item in p1:
    print(item)


# 进阶：迭代器玩的就是__next__
from cn2an import an2cn
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化状态（指针位置）
        self.__index = 0
        # 配置好要遍历的内容
        self.__attrs = [name, age, gender, address]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        # 如果指针的位置超出范围，那就抛出StopIteration异常
        if self.__index >= len(self.__attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attrs[self.__index]
        # 将字符串转为大写
        if isinstance(value, str):
            value = value.upper()
        # 将数字转为汉语形式
        if isinstance(value, int):
            value = an2cn(value)
        # 更新迭代器状态（指针位置）
        self.__index += 1
        # 返回value
        return value
