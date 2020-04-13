"""
@classmethod
author: Jack Lee
time: 2020/4/10 12:10

"""

from time import time, localtime, sleep

class Clock(object):

    def __init__(self, hour = 0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second


    @classmethod
    def now(cls):
        # time()返回到当前秒数
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)


    def run(self):
        self._second += 1
        if self._second == 60:
            self._minute += 1
            self._second = 0
            if self._minute == 60:
                self._hour += 1
                self._minute = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%0d' % (self._hour, self._minute, self._second)


def main():
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()