"""
线程之间的通信， 加锁
author: Jack Lee
time: 2020/4/19 16:52

"""

from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            # 计算存款后的余额
            newBalance = self._balance + money;
            # 模拟受理款项业务需要0.01s的时间
            sleep(0.1)
        finally:
            self._lock.release()
            self._balance = newBalance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money


    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for i in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()

    print('The Account Balance is  %s' % account.balance)

if __name__ == '__main__':
    main()


