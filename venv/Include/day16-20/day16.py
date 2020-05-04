"""
Python进阶
Written by: Jack Lee                                                   
Time: 2020/5/2 20:33                                                  

Function:Python重要知识点

"""

"""生成式（推到式）用法:用于生成列表、集合和字典。
"""
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.24,
    'ACN': 166.89,
    'FB': 208.89,
    'SYMC': 21.29
}
# python字典item函数以列表的形式返回可遍历的（键、值）元组数组
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)


"""嵌套列表：录入五个学生三门课的成绩
"""

names = ['Jack', 'Pony', 'Musk', 'Jobs', 'Bill']
courses = ['Chinese', 'Math', 'English']

# None是Python中一个特殊的常量，代表空值，有他自己独特的数据类型，与[]和""都不同
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        # scores[row][col] = float(input('请输入%s的%s成绩: ' %(name, course)))
        # scores[row][col] = float(input('请输入{}的{}成绩:'.format(name, course)))
        # Python3.6之后更为简洁的格式化字符串方式
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)


"""heapq模块(堆排序):从列表中找到最大的或者最小的N个元素
堆结构（大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM' , 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
# key关键字与sorted函数key关键字类似，用某个属性或则函数作为关键字 ， 该函数会作用与列表中的每一项
# lambda匿名函数的 x 是参数，
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


"""itertools模块:迭代工具模块"""

import itertools
# 产生ABCD的全排列
# 生成一个迭代器对象 元组数组
iter = itertools.permutations('ABCD')
for item in iter:
    print(item)
# 产生ABCDE的五选三组合
iter1 = itertools.combinations('ABCDE', 3)
for item in iter1:
    print(item)
# 产生ABCD和123的笛卡尔积
iter2 = itertools.product('ABCD', '123')
for item in iter2:
    print(item)

# 显示ABC无限循环序列
iter3 = itertools.cycle(('A', 'B', 'C'))


"""collection模块"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

counter = Counter(words)
print(counter.most_common(3))