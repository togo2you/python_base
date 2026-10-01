# def demo():
#     print('demo函数开始执行了')
#     yield '//我是第一个yield返回的数据'
#     print(100)
#     yield '//我是第二个yield返回的数据'
#     a = 200
#     print(a)
#     yield '//我是第三个yield返回的数据'
#     b = 300
#     print(b)
#     return 'aaa'
#
# d = demo()
#
# # 验证：生成器对象d，和迭代器一样，也拥有：__iter__  和 __next__ 方法
# print(hasattr(d,'__next__'))
# print(hasattr(d,'__iter__'))
#
# #for循环遍历生成器
# # for item in d:
# #     print(item)
# # #手动实现for循环遍历生成器
# gen = iter(d)
#
# while True:
#     try:
#         value = next(gen)
#         print(value)
#     except StopIteration:
#         break

# def create_car(total):
#     for index in range(total):
#         yield f'我是第{index}台车'
#
# cars = create_car(5)
#
# for car in cars:
#     print(car)

# def demo():
#     print('demo函数开始执行了')
#     print(100)
#     a = yield '//我是第一个yield返回的数据'
#     print(a)
#     b = yield '//我是第二个yield返回的数据'
#     print(b)
#     return 'aaa'
#
# d = demo()
# print(next(d))
# print(d.send(2200))
# #print(d.send(3200))
#

#用生成器实现遍历Person类的实例对象
class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        yield self.name
        yield self.age
        yield self.gender
        yield self.address


p1 = Person('张三', 18, '男', '北京昌平区')

for attr in p1:
    print(attr)