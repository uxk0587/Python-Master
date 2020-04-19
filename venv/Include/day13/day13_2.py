"""
自定义线程类
author: Jack Lee
time: 2020/4/19 13:02

"""


from random import randint
from threading import Thread
from time import time, sleep

class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('Start download %s ' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s downloaded finished! %s spended!' % (self._filename, time_to_download))

def main():
    start_time = time()
    t1 = DownloadTask(filename='PythonGuide.py')
    t1.start()
    t2 = DownloadTask(filename='PekingHot.avi')
    t2.start()
    t1.join()
    t2.join()
    end_time = time()
    print('Totally cost %.2f ' % (end_time - start_time))

if __name__ == '__main__':
    main()