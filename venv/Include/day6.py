"""
Python调用函数若是没有参数则会使用默认参数
"""
def add(n1=0, n2=0, n3=0):
    total = n1 + n2 + n3
    return total

result = add(1,2)
print(result)



"""
Python语言不支持函数的重载，但有别的方式实现类似的重载,上面例子是一种，另外还有一种使用可变参数的方法。
"""
def multi_add(*args):
    total = 0
    for val in args:
        total += val

    return total

print(multi_add(2,3,4,5,6))



"""
Python 全局变量声明
"""

def foo():
    # a = 200
    global a
    a = 200
    print(a)

# if __name__ == '__main__':
#     a = 500
#     foo()
#     print(a)



"""
Practice1: 实现计算最大公约数和最小公倍数的函数
"""
# greatest common divisorgcd
def gcd(x, y):
    """实现最大公约数"""

    """利用这种方式实现三目运算符"""
    (x, y) = (y, x) if x > y else (x, y) #可用元组方式赋值，位置数量匹配即可赋值成功
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)


if __name__ == '__main__':
    print(gcd(12,6))
    print(lcm(12,6))
    (m, n) = 1,2
    print(m, n)
    print((m, n))
    c = (m, n)
    print(c)
    print(type(c))