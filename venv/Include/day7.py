
import sys
"""
Python string和常用数据结构部分

"""
string = "Jack Lee is so fucking cooool!"
print(string)

str1 = string[0]
print(str1)

"""判断是否一个字符串是否包含另一个字符串"""
check = "J" in string
off_check = "J" not in string
print(check)
print(off_check)

print(len(string))


"""切片中后面的索引取不到"""
string3_5 = string[3:5]
print(string3_5)
string3_30 = string[3:]
print(string3_30)
string_all_to_5 = string[:5]
""" ::5 加步长; 2::5 从index为2开始步长5取  -为倒序取"""
string_allreverse_to_5 = string[::-1]
print(string[::-5])
print(string_allreverse_to_5)
print(string_all_to_5)
"""逆序切片"""
string_back1_back3 = string[-3:-1]
print(string_back1_back3)



print(len(string))

newstring = "jack is so facking coool"
print(newstring.capitalize())

print(newstring.title())

print(newstring.upper())

print(newstring.find("so"))

print(newstring.find("shit"))

print(newstring.index("so"))

print(newstring.startswith('jack'))
print(newstring.startswith('j'))
print(newstring.startswith('ja'))

print(newstring.endswith('l'))
print(newstring.endswith('coool'))

print(newstring.center(50, '-'))
print(newstring.center(50, '*'))
print(newstring.rjust(50, ' '))


string2 = '123asd'
# if it consists of digit
print(string2.isdigit())

# if it consists of alpha

print(string2.isdigit())

# if it both contain alpha and digit

print(string2.isalnum())


string3 = "   jsfgj@126.com   "
print(string3.strip())

a, b = 1, 3
print('method1: %d * %d = %d' % (a, b, a*b))
print('method2: {} * {} = {}'.format(a, b, a*b))
"""python3.6的新格式化字符串的方法"""
print(f'method3: {a} * {b} = {a * b}')



list = [1,2,3,4,5]

print(list)

print(len(list))

print(list[1])
print(list[-1])
list[2] = 500
print(list)

for i in range(len(list)):
    print(list[i])

for elem in list:
    print(elem)

for index, elem in enumerate(list):
    print(index, elem)

list.append(11)

print(list)

list.insert(1,400)
print(list)

list1 = ['a', 'b']
list.extend(list1)
print(list)

list += ['c', 'd']
print(list)

if 'a' in list:
    list.remove('a')
    print(list)

print(list.pop(6))
print(list)
# clear the element in the list
# print(list)
# list.clear()

print(list[1:3])
print(list[1::2])
print(list)


print(list[::-1])
print(list[::-2])
print(list)
"""从index为5开始倒着取步长为2"""
print(list[5::-2])
"""从index为-1开始倒着取步长为5"""
print(list[-1::-5])

print(list[:5])
print(list[:])
print(list[::])
list = list[0:6]
print(list)
print(sorted(list))

print(sorted(list, reverse=True))



list.sort(reverse=True)
print(list)


newlist = [x for x in range(10)]
print(newlist)

f = [x + y for x in 'abcdef' for y in '12345']
print(f)

# 生成式语法
list3 = [x ** 2 for x in range(10)]
print(sys.getsizeof(list3))
print(list3)

# 创造一个生成器对象
fgenerator = (x for x in range(1,1000))
print(sys.getsizeof(fgenerator))
print(fgenerator)

# 获取生成器内部数据
# for key in fgenerator:
#     print(key)


"""python中另一种使用生成器的方法"""
def fib(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
        # 通过yield字段将普通fib函数改造成生成器函数
        yield a

def main():
    for key in fib(20):
        print(key)
main()



"""元组"""
t = (1, 2, 'Jack', True)
print(t[1])
print(type(t))

# 遍历元组中的值
for member in t:
    print(member)

t = ('Jack', 'sooooo', 'fucking', 'coool')
print(t)

list_to_tuple = tuple(list)
print(list_to_tuple)
print(len(list_to_tuple))
print(list3)
print(sys.getsizeof(list3))
print(sys.getsizeof(tuple(list3)))


"""集合"""

set0 = {1,2,3,4,5}
print(set0)
print('length of the set: ',  len(set0))


set1 = {x for x in range(10)}
print(set1)

set2 = set(range(1,12))
print(set2)

set3 = set((1,2,3,4))
print(set3)

set3.add(5)
print(set3)

set3.update([10,11])
print(set3)

set3.discard(3)
print(set3)
set3.remove(10)
print(set3)
# 集合默认弹出第一个
print(set3.pop())
print(list)
# 列表默认弹出最后一个
print(list.pop())

"""字典"""
scores = {'Jack': 22, 'Tony': 23, 'Tom': 24}
print(scores)
print(type(scores))

item1 = dict(one='1', two='2', three='3', four='4')
print(item1)

item2 = {'{}'.format(num): num**2 for num in range(10)}
print(item2)
# 通过zip函数将两个序列压成字典
item3 = dict(zip([1,2,3], 'abc'))
print(item3)

print(scores['Jack'])

for key in scores:
    print("{}: ".format(key), scores[key])
    # print(f"")打印可以执行的表达式，会对表达式先进行运算然后打印
    print(f"{key} is : {scores[key]}")
    print(key)
scores.update(newton=22, tomas=32)
print(scores)

scores['wade'] = 12
print(scores)

if 'Jack' in scores:
    print(scores['Jack'])


print(scores.get('Jack'))
# 字典默认pop出最后一个
print(scores.popitem())

print(scores.pop('Jack', 22))
print(scores)


scores.clear()
print(scores)

testlist = [1,2,'2']
print(testlist)