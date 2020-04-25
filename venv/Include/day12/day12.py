"""
使用正则表达式
author: Jack Lee
time: 2020/4/14 10:26

"""

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

# Python提供re模块来支持正则表达式相关操作
import re


# 例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息

def check_username_qq():
    username = input("Username: ")
    qq = input("Input the qq number: ")

    # re.match 用正则表达式匹配字符串 成功返回匹配对象，失败返回None
    # 字符串前加r表示使用原始字符串，即字符串中没有所谓的转义字符。
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Please input the valid username')
    else:
        print("This username is valid")
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Please input the valid qq')
    else:
        print("This qq number is valid")


# 例子2：从一段文字中提取出国内手机号码。

def find_all_number():
    # 编译正则表达式返回正则表达式对象
    # 实际开发中若如果一个正则表达式需要重复的使用, 那么先通过compile函数编译正则表达式并创建出正则表达式对象无疑是更为明智的选择。
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''

    # re.findall查找字符串所有与正则表达式匹配的模式 返回字符串列表
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print("---------------------------------------")

    # re.finditer 查找字符串与正则表达式匹配的模式，返回一个迭代器
    # 通过迭代器取出匹配对象并获得匹配内容
    # （实际开发中也可以用正则表达式对象的方法pattern.finditer替代re.finditer
    for temp in re.finditer(pattern, sentence):
        # temp是一个匹配对象， 通过匹配对象temp.group()函数来得到整个该匹配对象中匹配的字符串
        print(temp.group())


# 例子3：替换字符串中的不良内容
def replace_main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    # pattern = re.compile("[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔|fuck you") 注意编译后不在re.xxx()函数中不用用flags参数，会报错
    # re.sub()用于替换字符串中的匹配项，第一个参数是正则表达式匹配模式
    # 第二个参数是替换的字符，第三个参数是要被查找替换的原始字符串，第四个参数是模式匹配后替换的最大次数默认为0替换所有匹配
    # re模块中都有一个flags参数，用来指定匹配时是否忽略大小写、多行匹配等等。
    purified = re.sub("[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔|fuck you", '*', sentence, flags=re.I)
    print(purified)


if __name__ == '__main__':
    check_username_qq()
    find_all_number()
    replace_main()
