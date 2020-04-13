"""
写文件：
如何将1-9999之间的素数分别写入三个文件中
（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
author: Jack Lee
time: 2020/4/13 12:22

"""

from math import sqrt

def is_prime(n):
    """Check if is prime number"""
    # assert断言 在表达式为false时触发异常
    assert n > 0, 'n can\'t be negative '
    for factor in range(2,int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fi_list = []
    try:
        for filename in filenames:
            fi_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fi_list[0].write(str(number)+ '\n')
                elif number < 1000:
                    fi_list[1].write(str(number) + '\n')
                else:
                    fi_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('Find an Error when writing a file')

    finally:
        for fi in fi_list:
            fi.close()
    print("Operation Down!")

if __name__ == '__main__':
    main()