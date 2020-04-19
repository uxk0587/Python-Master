"""
Python进程与线程
author: Jack Lee
time: 2020/4/19 10:07

"""
# Python中的多进程

from random import randint
from time import time, sleep # time.time()获得当前时间戳
# 通过multiprocessing模块的Process类来创建进程
from multiprocessing import Process

# 没有用线程方式模拟下载文件例子
def download_task(filename):
    print('Start downloading: %s' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s Download finished! %s seconds spended" % (filename, time_to_download))

# 不用多进程下载
def download_task_without_multiprocess():
    start = time()
    download_task('PythonGuide.pdf')
    download_task('PekingHot.avi')
    end = time()
    print('Totally cost %.2f' % (end - start))


# 使用多进程下载
def download_task_with_multiprocess():
    start_time = time()
    # target参数传入一个函数表示进程启动后要执行的代码， argss是一个元组代表传递给函数的参数
    p1 = Process(target=download_task, args=('PythonGuide.pdf',))
    # 启动进程
    p1.start()
    p2 = Process(target=download_task, args=('PekingHot.avi',))
    p2.start()
    # 等待进程执行结束
    p1.join()
    p2.join()
    end_time = time()
    print('Totally cost %.2f' % (end_time - start_time))


if __name__ == '__main__':
    # download_task_without_multiprocess()
    download_task_with_multiprocess()


