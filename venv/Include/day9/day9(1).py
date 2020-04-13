"""

author: Jack Lee
time: 2020/4/10 11:25

"""

"""静态方法"""
from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c


    @staticmethod
    def is_valid(a, b, c):
        # if a + b > c and b + c > a and a + c > b:
        #     return True
        # else:
        #     return False
        return a + b > c and b + c > a and a + c > b


    def perimeter(self):
        return self._a + self._b + self._c


    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))



def main():
    a, b, c = 4, 3, 5

    if Triangle.is_valid(a,b,c):
        t = Triangle(a, b, c)
        # print(t.perimeter())
        print(Triangle.perimeter(t))
        print(Triangle.area(t))
        # print(t.area())
    else:
        print("Can't construct to a Triangle")


if __name__ == '__main__':
    main()



