"""

Written by: Jack Lee                                                   
Time: 2020/7/30 10:42                                                  

Function:   Python并发编程进阶

                                                           
"""

"""多线程"""
import glob
import os
import threading
import time
from PIL import Image

PREFIX = 'thumbnails'

# 生成指定图片文件的缩略图
def generate_thumbnail(infile, size, format='PNG'):
    # 将文件名和扩展名分开 text.py => text, .py
    file, ext = os.path.splitext(infile)
    # 返回字符串最后一次出现的位置
    file = file[file.rfind('\\') + 1:]
    outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
    # 打开图像
    img = Image.open(infile)
    # 图像缩放 Pillow 带ANTIALIAS滤镜缩放
    img.thumbnail(size, Image.ANTIALIAS)
    # 保存图片
    img.save(outfile, format)

# 通过类来实现多线程
class GenerateThumbnail(threading.Thread):

    def __init__(self, infile, size, format='PNG'):
        super().__init__()
        self._infile = infile
        file, ext = os.path.splitext(infile)
        self._ext = ext
        self._file = file[file.rfind('\\') + 1:]
        self._image_size = size
        self._format = format

    @property
    def file(self):
        return self._file

    @property
    def format(self):
        return self._format

    # 必须对某属性设置了property才能用xxx.setter方法
    @format.setter
    def format(self, format):
        self._format = format

    # 重写run方法
    def run(self):
        outfile = f'{PREFIX}/{self._file}_{self._image_size[0]}_{self._image_size[1]}.{self._ext}'
        img = Image.open(self._infile)
        img.thumbnail(self._image_size, Image.ANTIALIAS)
        img.save(outfile, self._format)

def main_1():
    start = time.time()
    threads = []
    if not os.path.exists(PREFIX):
        os.mkdir(PREFIX)
    #  标准库glob 不用遍历整个目录判断每个文件是否符合 匹配所有符合条件的文件，将其以list的形式返回
    for infile in glob.glob('images/*.jpg'):
        print(infile)
        for size in (32, 64, 128):
            # # 创建启动线程
            # thread = threading.Thread(
            #     target=generate_thumbnail,
            #     args=(infile, (size,size))
            # )
            # threads.append(thread)
            # thread.start()
            new_thumbnail_thread = GenerateThumbnail(infile, (size, size))
            threads.append(new_thumbnail_thread)
            new_thumbnail_thread.start()

    for thread in threads:
        thread.join()


    end = time.time()


    print(f'Total time cost: {end - start}')

# if __name__ == '__main__':
#     main()

"""多个线程竞争资源的情况"""
# 当多个线程竞争资源的时候如果缺乏必要的保护措施就会导致数据混乱
# 临界资源就是被多个线程竞争的资源

# 线程池执行器
from concurrent.futures import ThreadPoolExecutor

# 银行账户
class Account_1(object):

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.RLock()

    def deposit(self, money):
        with self.lock:
            new_balance = self.balance + money
            # time.sleep()方法会推迟线程的运行
            time.sleep(0.01)
            self.balance = new_balance
            print(self.balance)

# 自定义线程类
class AddMoneyThread(threading.Thread):

    def __init__(self, account, money):
        self.account = account
        self.money = money
        # 自定义线程的初始方法中必须调用父类的初始化方法
        super().__init__()

    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)

def main_2():
    account = Account_1()
    # 线程池执行器， 创建线程池
    # 池的概念主要目的是为了重用，让线程或者进程在生命周期内可以多次使用。它减少了创建线程和进程的开销，提高了程序性能
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    # threads = []
    for _ in range(100):

        # 创建线程第一种方式
        # t = threading.Thread(target = account.deposit, args=(1, ))
        # threads.append(t)
        # t.start()

        # 创建线程的第二种方式
        # t = AddMoneyThread(account, 1)
        # threads.append()
        # t.start()

        # 创建线程的第三种方式：调用线程池中的线程来执行特定的任务
        # 任务通过executor.submit()提交executor的任务队列，返回一个future对象。
        # 任务被调度到worker中执行。一个任务一旦执行，在执行完毕前，会一直占用该worker，
        # 如果worker不够用，其他的任务会一直等待
        future = pool.submit(account.deposit, 1)
        futures.append(future)
        # print(account.balance)
    # 等待线程执行结束
    # for t in threads:
    #     t.join()

    #关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()

    print(account.balance)

# if __name__ == '__main__':
#     main_2()


"""修改上面的程序，启动5个线程向账户中存钱，5个线程从账户中取钱，取钱时如果余额不足就暂停线程进行等待。
为了达到上述目标，需要对存钱取钱线程进行调度，在余额不足时取钱的线程暂停并释放锁，而存钱的线程将钱存入后要通知
取钱的线程，使其从暂停状态被唤醒，可以使用threading模块的Condition来实现线程调度，该对象也是基于锁来创建的。
"""

from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading


class Account_2():
    """银行账户"""

    def __init__(self, balance=0):
        self.balance = balance
        lock = threading.Lock()
        self.condition = threading.Condition(lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                # 调用conditon.wait()方法让当前线程挂起， 等待被唤醒
                self.condition.wait()
            new_balance = self.balance - money
            sleep(0.001)
            self.balance = new_balance

    def deposit(self, money):
        """存钱"""
        with self.condition:
            new_balance = self.balance + money
            sleep(0.001)
            self.balance = new_balance
            # 唤醒所有等待条件变量的线程
            self.condition.notify_all()


def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, ':', money, '=====>', account.balance)
        sleep(1)

def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, ':', money, '<=====', account.balance)
        sleep(1)


def main_3():
    account = Account_2()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money, account)
            pool.submit(sub_money, account)


if __name__ == '__main__':
    main_3()