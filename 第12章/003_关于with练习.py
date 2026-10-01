#   with 能得到一个上下文管理器的表达式 as 变量:
#       具体的事1
#       具体的事2
#       具体的事3

# 4.上下文管理器协议：
#    (1). __enter__ 方法：with 中的代码执行【之前】调用，其返回值会赋值给 as 后的变量。
#    (2). __exit__  方法：with 中的代码执行【结束后】调用（无论是 with 中否出现异常都会调用）。

# 定义一个 Person 类，让其实例对象遵循：上下文管理器协议
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'我叫{self.name}，年龄是{self.age}')

    def __enter__(self):
        print(f'_______我是{self.name}进入的逻辑_______')
        return self

    # 当 with 中的代码发生异常时，__exit__ 方法的返回值规则如下：
    #   🔸返回“真”：表示异常【已经】被处理，异常【不会】被继续抛出。
    #   🔸返回“假”：表示异常【没有】被处理，异常【会】被继续抛出。
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'_______我是{self.name}退出的逻辑_______')
        if exc_type:
            print(f"{self.name}的异常类型是{exc_type}")  # 异常类型
            print(f"{self.name}的异常对象是{exc_val}")  # 异常对象
            print(f"{self.name}的异常追踪信息是{exc_tb}")  # 异常追踪信息

        return True

# 1.计算 with 后面的表达式，得到一个『上下文管理器』。
# 2.调用『上下文管理器』的 __enter__() 方法，并将其返回值赋给 as 后面的变量。
# 3.执行 with 所管理的代码。
# 4.无论代 with 中的代码，是正常结束，还是发生异常，都会自动调用『上下文管理器』的 __exit__ 方法。
with Person('张三', 18) as p1, Person('李四', 21) as p2:
    p1.speak()
    # p1.study()
    print('666')

    p2.study()
