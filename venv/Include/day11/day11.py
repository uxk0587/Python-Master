"""
read file
author: Jack Lee
time: 2020/4/13 11:06

"""
import time
def main():
    # f = open('day11.txt', 'r')
    # print(f.read())
    # f.close()
    f = None

    try:
        # Get the file object
        # f = open('day111.txt', 'r')
        # print(f.read())
        with open('day11.txt', 'r') as f:
            print(f.read())
            print()
        with open('day11.txt', 'r') as f:
            lines = f.readlines()
        print(lines)
        """
        with open('day11.txt', 'r') as f:
            # 使用for循环对对象file进行迭代时，每次迭代都会自动分离出一行（效果相当于对readlines结果的for循环遍历）：
            for line in f:
                print(line, end='')
                time.sleep(0.5)
        """
    except LookupError:
        print('Unknown Encoding')
    except UnicodeDecodeError:
        print('Error when reading the file')
    except FileNotFoundError:
        print("No such file or directory")
    # finally:
    #     if f:
    #         f.close()





if __name__ == '__main__':
    main()