"""
Python多线程
author: Jack Lee
time: 2020/4/19 11:52

"""

from random import randint
from time import time, sleep
from threading import Thread

def download(filename):
    print('%s Start downloading' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s download finished! %s second spended' % (filename, time_to_download))

def download_file_with_thread():
    start_time = time()
    t1 = Thread(target=download, args=('PythonGuide.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('PekingHot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end_time = time()
    print('Total time cost: %.3f' % (end_time - start_time))


if __name__ == '__main__':
    download_file_with_thread()