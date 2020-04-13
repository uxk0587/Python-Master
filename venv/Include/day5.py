"""

author: Jack Lee
time: 2020/2/26 18:51

"""
"""
寻找水仙花数：
水仙花数也被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，
它是一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
"""
import math

for number in range(100,1000):
    single_digit = number % 10
    # ten_digit = number % 100 //10
    ten_digit = int(number % 100 / 10)
    # hubdred_digit = number // 100
    hundred_digit = int(number / 100)
    # if number == single_digit ** 3 + ten_digit ** 3 + hundred_digit ** 3:
    if number == pow(single_digit, 3) + pow(ten_digit, 3) + pow(hundred_digit, 3):
        print("{} is Armstrong number".format(number))


"""
百钱百鸡的问题：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
"""
for x in range(101):
    for y in range(34):
        for z in range(300):
            if x + y + z == 100 and 5*x + 3*y + z/3 == 100:
                print("x is %s, y is %s, y is %s" % (x, y, z))



"""
CRAPS赌博问题：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。

Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""


from random import randint

money = 1000
game_round = 1
while money > 0 :
    print("Round: %d" % game_round)
    print("your money is %d" % money)
    needs_go_on = False
    stake = 10
    if stake > money:
        print("you don't have so much money")
        break
    first_rock = randint(1,6) + randint(1,6)
    if first_rock == 7 or first_rock == 11:
        print("Player Win! ")
        money += stake
    elif first_rock == 2 or first_rock == 3 or first_rock == 12:
        print("Banker Win!")
        money -= stake
    else:
        needs_go_on = True
    while needs_go_on == True:
        this_rock = randint(1,6) + randint(1,6)
        if this_rock == first_rock:
            print("Player Win!")
            money += stake
            needs_go_on = False
            game_round += 1
        elif this_rock == 7:
            print("Banker Win!")
            money -= stake
            needs_go_on = False
            game_round += 1
print("you are bankrupt")