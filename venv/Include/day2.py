"""
将华氏温度转为摄氏温度
author: Jack Lee
time: 2020/1/2 23:08

"""

f = float(input('请输入华氏摄氏度：'))
c = (f - 32) / 1.8
print('%.1f °F = %.1f °C' % (f, c))



#输入半径计算圆的周长和面积
import math

radius = float(input('input radius:'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print('perimeter of the circle : %.1f' % perimeter )
print('area of the circle : %.1f' % area)



#判断是不是闰年

year = int(input('input year: '))

is_leap = year % 400 == 0 or \
          (year % 100 != 0 and year % 4 == 0)

print('%d is leap? %s' % (year, is_leap))

