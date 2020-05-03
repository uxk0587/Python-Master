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

