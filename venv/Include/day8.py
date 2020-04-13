"""
Python面向对象编程基础
author: Jack Lee
time: 2020/3/31 11:41

"""


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s is studing %s." % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s only can see Bear Is Coming" % self.name)
        else:
            print("%s can see Action Movies" % self.name)


class Test(object):

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    student1 = Student('Jack', 17)
    student1.study("Python Object Programming")
    student1.watch_movie()

    student2 = Student("Pony", 40)
    student2.study("Tencent Busiess")
    student2.watch_movie()

    test = Test("Programming")
    """双下划线设为私有属性，外界不能访问。
    test.__foo()
    test.__bar()
    """
    # 但是还是可以通过这种方式访问到, 建议
    print(test._Test__foo)
    test._Test__bar()


from time import sleep


class Clock(object):

    def __init__(self, hour, min, sec):
        self._hour = hour
        self._min = min
        self._sec = sec

    def run(self):
        self._sec += 1
        if self._sec == 60:
            self._min += 1
            self._sec = 0
            if self._min == 60:
                self._hour += 1
                self._min = 0
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return "%3d:%03d:%03d" % (self._hour, self._min, self._sec)


def clock_main():
    clock = Clock(12, 12, 12)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
        f()


from math import sqrt


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)



def point_main():
    p1 = Point(1,1)
    p2 = Point(2,2)
    print(p1)
    print(p2)

    p2.move_by(1,1)
    print(p2)

    print(p1.distance_to(p2))



if __name__ == '__main__':
    point_main()
"""
    a = ""
    print(type(a))
    a = 1
    print(a)
    print(type(a))
    
"""
