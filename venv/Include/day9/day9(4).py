"""

author: Jack Lee
time: 2020/4/11 11:07

"""
"""多态"""
from abc import ABCMeta, abstractmethod


# 通过ABCMeta元类来达到定义抽象类效果
class Pet(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    # 通过abstractmethod包装器来实现抽象方法
    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):

    def make_voice(self):
        print("%s : WangWangWang" % self._name)

class Cat(Pet):

    def make_voice(self):
        print("%s : MiaoMiaoMiao" % self._name)

# def main():
#     pets = [Dog('Wangcai'), Cat('Timmy'), Dog('DaHuang')]
#
#     for pet in pets:
#         pet.make_voice()

class Hero(object):

    def __init__(self, name, hp = 100):
        self._name = name
        self._hp = hp

    def useItem(self, item):
        item.effect()


class Item(object):

    def effect(self):
        print("Item has worked")

class LifePotion(Item):

    def effect(self):
        print("LifePotion is being used, It has worked")

class MagicPotion(Item):

    def effect(self):
        print("MagicPotion is being used, It has worked")

def main():
    gareen = Hero('gareen')
    lp = LifePotion()
    mp = MagicPotion()
    gareen.useItem(lp)
    gareen.useItem(mp)


if __name__ == '__main__':
    main()
