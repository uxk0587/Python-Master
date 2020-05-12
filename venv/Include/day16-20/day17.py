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


# 命名关键字参数
def person(name, age, *, grade='12', city):
    print(name, age, grade, city)


person('Jack', 22, city='Tianjin')


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

