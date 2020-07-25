"""

Written by: Jack Lee                                                   
Time: 2020/7/25 13:28                                                  

Function:   Python迭代器和生成器

                                                           
"""

"""迭代器：Python中迭代器是实现了迭代器协议的对象"""
# 参考Python yield浅析：https://www.runoob.com/w3cnote/python-yield-used-analysis.html
# Python中没有protocol和interface这样的定义协议的关键字
# Python中用魔法方法表示协议
# __iter__和__next__魔法方法就是迭代器协议


class Fib(object):
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    # 该魔术方法可以让对象可以用for ... in循环遍历，在使用for ... in循环的时候触发。
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

print(Fib(12))
# 实现迭代器后Fib实际上就成了支持Iterable的class，可直接在循环中用
for i in Fib(12):
    print(i)

# 生成器是语法简化版的迭代器
def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a+b
        # yield的作用是把函数变成一个generator生成器，带有yield的函数不再是一个普通函数，Python解释器会将其视为一个generator
        # 调用fib(12)不会执行fib函数，而是返回一个iterable对象
        yield a

print(fib(12))
for i in fib(12):
    print(i)

# 生成器进化为协程： 协程部分具体参见张雪峰教程：https://www.liaoxuefeng.com/wiki/1016959663602400/1017968846697824
def calc_avg():
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter

gen = calc_avg()
# 调用next()第一次调用，相当于启动生成器，从gen函数头开始调用，一直到yield停止
next(gen)
# send()方法可以发送数据，发送的数据会成为生成器函数中通过yield表达式获得的值。
print(gen.send(10))
print(gen.send(20))