"""

author: Jack Lee
time: 2020/1/31 21:40

"""

"""
输入一个判断是不是素数
素数：只能被1和自身整除的大于1的整数
"""

from math import sqrt


n = int(input('input the number:'))
is_prime = True

if n==1:
    print('1 is prime')
else:
    for i in range(2,n+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print('%d is prime' % n)
    else:
        print('%d is not prime' % n)

"""
method2:利用开平方，一个数要是有有素因子p，则必存在另一个因数n/p
"""
number = int(input('input the number:'))
is_prime = True
end = int(sqrt(number))
for i in range(2, end+1):
    if number % i == 0:
        is_prime = False
        break
if is_prime and number != 1:
    print('%d is prime' % number)
else:
    print('%d is not prime' % number)


"""
输入两个正整数计算他们的最大公约数和最小公倍数
"""



"""
输出三角形图案
*
**
***
****
*****
"""
for i in range(5):
    for j in range(i+1):
        print("*", end='')
    print('')

"""
输出三角形图案
    *
   **
  ***
 ****
*****
"""
for i in range(5):
    for j in range(5-i-1):
        print(' ', end='')
    for j in range(i+1):
        print("*", end='')
    print()

"""
输出三角形图案
    *
   ***
  *****
 *******
*********
"""

for i in range(5):
    for j in range(5-i-1):
        print(' ', end='')
    for j in range(2*(i+1)-1):
        print('*', end='')
    for j in range(5-i-1):
        print(' ', end='')
    print()
