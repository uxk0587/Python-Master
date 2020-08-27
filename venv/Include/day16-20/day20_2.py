"""

Written by: Jack Lee                                                   
Time: 2020/8/21 16:12                                                  

Function:  Python进阶Day20：异步处理

"""

"""
异步处理：从调度程序任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务以某种顺序去执行，因为执行
顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序
的不确定，因此需要通过回调式函数编程或者future对象来获取任务执行的结果。Python3通过asyncio模块和await和async关键字来支持异步处理
"""

# 异步I/O - async / await
# 本节异步IO相关知识具体参考廖雪峰的网站：https://www.liaoxuefeng.com/wiki/1016959663602400/1017959540289152
import asyncio


def num_generator(m, n):
    """指定范围的数字生成器"""
    # yield from 后面加可迭代对象， yield关键字参见day19
    # 返回一个iterable可迭代对象
    yield from range(m, n+1)

# 把一个genertator标记为coroutine类型， async是@asyncio.coroutine的python3.5新语法替换
# 总的来说，可以用async来声明一个异步函数，正常函数在执行过程中是不会中断的，要写一个可以中断的函数，就要用到async关键字，
# 异步函数特点是能够在函数执行的过程中挂起，去执行其他异步函数，等到挂起条件消失后再回来接着执行
async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break

        if flag:
            print('Prime => ', i)
            primes.append(i)
        # await替换了之前的yield from,是Python3.5新语法 yield from可以方便地调用另一个coroutine
        # 由于asycnio.sleep也是coroutine，所以线程不会等待asyncio.sleep(),而是直接中断并执行下一个消息循环
        # 当asyncio.sleep()返回时，线程可以从yield from 拿到返回值（此处是None），然后接着执行下一条语句
        # 可以把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine，
        # 因此可以实现并发执行
        # 总的来说：await用来声明函数的挂起，比如异步函数声明到某一步需要等待很长的时间，就将此挂起，去执行其他的异步函数。
        # 这里await的使用讲解可以参考：https://www.cnblogs.com/xinghun85/p/9937741.html
        await asyncio.sleep(0.001)
    return tuple(primes)



async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square => ', i*i)
        squares.append(i*i)

        await asyncio.sleep(0.001)

    return squares

def main():
    """主函数"""
    # 获取EventLoop
    loop = asyncio.get_event_loop()
    # 可通过asyncio.gather(*tasks), 将不同的coroutine预先封装成future, 返回一个future对象
    future = asyncio.gather(prime_filter(2,100), square_mapper(1,100))
    # future对象实际上也是个coroutine，添加回调函数,当future运行结束后会调用这个函数
    # future.result()返回future结果
    future.add_done_callback(lambda x: print(x.result()))
    # 执行coroutine, loop对象的run_until_complete方法可以等待通过future对象获得协程执行结果
    loop.run_until_complete(future)
    loop.close()

if __name__ == '__main__':
    main()
