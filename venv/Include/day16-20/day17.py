"""

Written by: Jack Lee
Time: 2020/5/6 10:39                                                  

Function:Python进阶： 函数的使用方式


                                                           
"""

"""
1.map函数: map函数会对根据提供的函数对指定序列做映射map(function函数, iterable可迭代对象),
           返回一个迭代器;
2.filter函数： filter函数用于过滤序列，filter（function函数，iterable可迭代对象），序列中的每个元素作为参数传递
            给前面参数作为判断，返回True和False，将返回True的元素放到新的迭代器对象中
"""
filter_items = filter(lambda x: x % 2, range(1, 10))
print(filter_items)
items1 = list(map(lambda x: x ** 2, filter_items))
print(items1)
print(1 is True)
a = [1, 2, 3]
b = a
b = [1, 2, 3]
print(a is b)

"""位置参数、默认参数、关键字参数**kargs 、可变参数*args,（这两个相当于包裹过程） 命名关键字参数 """


# 命名关键字参数 *右边为关键字参数否则会报错，当然也可以有默认参数
def person(name, age, *, grade='12', city):
    print(name, age, grade, city)

person('Jack', 22, city='TianJin')
person('Jack', 22, grade='13', city='Tianjin')


# 默认参数在定义时在位置参数后面,否则会报错

def person1(name, age=12):
    print(name, age)


# *args中的*表示可变参数，所有参数会被*args变量收集，形成一个元组*args，
# args是 *args 元组的拷贝
def calc(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)

calc(12, 12)


# **kwargs中的**表示关键字参数, 传入的关键字会在函数内部自动组装成一个字典**kwargs，
# kwargs是**kargs字典的一个拷贝
def person3(**kwargs):
    print(kwargs)


person3(name='Jack', age=22)
dict1 = {'name': 'Jack', 'age': 22}
# 在调用函数时使用*或**时代表解包裹， **将字典中的键值对解包裹成关键字参数传递给函数
person3(**dict1)

tuple1 = (1,2,3)
# *将元组中的元素解包裹成参数传给函数
calc(*tuple1)

"""装饰器函数、带参数的装饰器、函数中嵌套装饰器、装饰器类"""

#装饰器函数 具体内容看Python进阶书
from functools import wraps
from time import time
#输出函数执行时间的装饰器
def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}')
        return result
    return wrapper

@record_time
def func():
    a = []
    for i in range(10111000):
        a.append(i)

func()


# 带参数的装饰器, 在函数中嵌套装饰器 源自《Python进阶一书》
def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            start = time()
            log_string = 'Time: ' + str(start)
            log_string += ' ' + func.__name__ + " was called"
            spended_time = time() - start
            log_string += ', Time spended: ' + str(spended_time)
            print(log_string)
            # 执行前写入日志
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1(x):
    return x + x

print(myfunc1(2))

# 带参数的装饰器
@logit(logfile='out1.log')
def myfunc2(x):
    return x + x

print(myfunc2(2))

# 装饰器类  这样比嵌套函数使用更加简洁
class class_logit(object):
    def __init__(self, logfile = 'out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            start = time()
            log_string = 'Time: ' + str(start)
            log_string += ' ' + func.__name__ + " was called"
            spended_time = time() - start
            log_string += ', Time spended: ' + str(spended_time)
            print(log_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass

@class_logit()
def myfunc3(x):
    return x + x

print(myfunc3(2))

# 创建class_logit的子类，通过继承实现别的功能

class email_logit(class_logit):
    """
    实现在调用函数的时候，除了打印日志还发送email给管理员
    """

    def __init__(self, email='xxx@gmail.com', *args, **kwargs):
        self.email = email
        super().__init__(*args, **kwargs)

    def notify(self):
        print("Sending a email to Jack")
        pass

@email_logit()
def myfunc4(x):
    return x + x

print(myfunc4(2))


# 用装饰器来实现单例模式
# 装饰类的装饰器
def singleton(cls):

    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class President:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

president1 = President('Jack')
print(president1.name)
president2 = President('Tom')
# 返回的还是Jack， 单例模式中 单例类只能有一个实例， 单例类必须自己创建唯一的实例，单例类必须给所有其他对象提供这一实例。
# 保证一个类仅有一个实例，并提供一个访问它的全局访问点。
# 返回的还是Jack
print(president2.name)

from threading import RLock

# 线程安全的单例装饰器 避免一个实例被构建了多次
def ths_singleton(cls):
    instances = {}
    locker = RLock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        # 在wrapper函数中，我们先做了一次不带锁的检查，然后再做带锁的检查，这样做比直接加锁检查性能要更好，
        # 如果对象已经创建就没有必须再去加锁而是直接返回该对象就可以了。
        if cls not in instances:
            with locker: # 通过with方式来获取锁
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


