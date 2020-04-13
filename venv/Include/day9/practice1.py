"""
奥特曼打小怪兽
author: Jack Lee
time: 2020/4/11 12:03

"""

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class  Ultraman(Fighter):

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15,25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False


    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '---%s Ultraman---\n' % self.name + \
                'hp: %d\n' % self._hp + \
                'mp: %d\n' % self._mp


class Monster(Fighter):

    __slots__ = ('_hp', '_name')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '---%s Monster--- \n' % self._name + \
                'hp: %d\n ' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive is True:
            return True
    return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive is True:
            return monster


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')



def main():
    tailuo = Ultraman("Tailuo", 100, 100)
    print(tailuo)
    m1 = Monster('m1', 250)
    m2 = Monster('m2', 500)
    m3 = Monster('m3', 750)
    monsters = [m1,m2,m3]
    fight_round = 1
    while tailuo.alive and is_any_alive(monsters):
        print("-----------第%02d回合-------------" % fight_round)
        m = select_alive_one(monsters)
        skill = randint(1,10)
        if skill <= 6:
            print("%s使用普通攻击打了%s" % (tailuo.name, m.name))
            tailuo.attack(m)
            print("%s的魔法值恢复了%s点." % (tailuo.name, tailuo.resume()))
        elif skill <= 9:
            if(tailuo.magic_attack(monsters)):
                print("%s使用了魔法攻击" % tailuo.name)
            else:
                print("%s使用魔法失败" % tailuo.name)
        else:
            if tailuo.huge_attack(m):
                print("%s使用究极必杀技虐杀了%s." % (tailuo.name, m.name))
            else:
                print("%s使用了普通攻击打了%s." % (tailuo.name, m.name))
                print("%s的魔法值恢复了%d点." % (tailuo.name, tailuo.resume()))

        if m.alive is True:
            print("%s回击了%s." % (m.name, tailuo.name))
            m.attack(tailuo)
        display_info(tailuo, monsters)

        fight_round += 1
    print("-----------------战斗结束---------------------")
    if tailuo.alive is True:
        print("%s 奥特曼胜利" % tailuo.name)
    else:
        print("小怪兽胜利")




if __name__ == '__main__':
    main()



