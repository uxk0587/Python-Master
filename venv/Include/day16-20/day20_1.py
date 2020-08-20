"""

Written by: Jack Lee                                                   
Time: 2020/8/19 9:30                                                  

Function: Python进阶 Day20 多进程编程进阶

                                                           
"""

"""多进程可以有效的解决GIL问题，实现多进程主要的类是Process，其他辅助的类跟threading模块中的类似，
进程间共享数据可以使用管道，套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁机制提供了多个进程共享的队列。
下面是官方文档中关于多进程和进程池的一个实例"""


"""多进程和进程池的使用
多进程因为GIL锁的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑使用多进程

time python3 example22.py
real    0m11.512s
user    0m39.319s
sys     0m0.169s
使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU"""


import concurrent.futures
import math
from time import time

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5


def is_prime(n):
    """判断素数"""
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main_1():
    """主函数1: 使用多进程"""
    start_time = time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # zip函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些组成的列表
        # ProcessPoolExecutor.map()方法类似全局函数map(func, iterable),全局函数map会根据提供的函数对指定序列做映射
        # 但是该map函数会启动多个进程，以异步的方式对iterable执行map处理
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    end_time = time()
    print(f'----------------Total time cost: { end_time - start_time}-----------------')
    
def main_2():
    """主函数2: 不使用多进程"""
    start_time = time()
    for number, prime in zip(PRIMES, map(is_prime, PRIMES)):
        print(f'{number} is prime: {prime}')
    end_time = time()
    print(f'--------------Total time cost: {end_time - start_time}----------------')

if __name__ == '__main__':
    main_1()
    main_2()




"""多线程和多进程比较
以下情况使用多线程：
1.程序需要维护多个共享的状态，Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态
的代价相对较小
2.程序会花费大量时间在I/O操作上,没有太多并行计算的需求且不需占有太多内存

以下情况使用多进程：
1.执行计算密集型任务（如字节码操作、数据处理、科学计算）
2.程序在内存使用方面没有任何限制且不强依赖于I/O操作（如读写文件、套接字）
"""
