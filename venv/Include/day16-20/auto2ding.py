"""

Written by: Jack Lee                                                   
Time: 2020/9/5 8:39                                                  

Function:  自动化钉钉打卡

                                                           
"""

import os
import time


# import pyautogui
def auto2ding():
    time.sleep(1)
    # 唤醒屏幕
    os.system('adb shell input keyevent 3')
    # 上拉解锁
    os.system('adb shell input swipe 500 900 500 300')
    # 进入钉钉
    os.system('adb shell input tap 417 1754')
    # 进入DING
    os.system('adb shell input tap 874 427')
    # 等待加载
    time.sleep(5)
    # 开始填写
    os.system('adb shell input tap 553 1068')
    # 等待加载
    time.sleep(10)
    os.system('adb shell input swipe 536 1300 536 374')
    # 获取定位
    os.system('adb shell input tap 1025 1252')
    # 下滑至最底部
    for i in range(5):
        os.system('adb shell input swipe 536 1300 536 274')
    # 提交
    os.system('adb shell input tap 620 1580')
    # print(os.system('adb shell input tap 430 1780'))
    # 返回
    os.system('adb shell input tap 80 148')
    for i in range(2):
        os.system('adb shell input keyevent 3')
    # time.sleep(3)
    # # 点击工作通知 置顶
    # print(os.system('adb shell input tap 535 888'))
    # # time.sleep(2)
    # # 开始填写
    # print(os.system('adb shell input tap 543 2145'))
    # time.sleep(5)


def get_second(hour, min=0, second=0):
    return hour * 3600 + min * 60 + second


def main():
    sleep_second = get_second(6)
    while True:
        time.sleep(1)
        sleep_second -= 1
        print(f'{sleep_second}s later will auto to ding...')
        if sleep_second == 0:
            break
    auto2ding()

    # time.sleep(sleep_second)
    # auto2ding()


# # version 2
# def main():
#     time.sleep(3)
#     # pyautogui.alert("this is an alert box")
#     currentMouseX, currentMouseY =pyautogui.position()
#     print(currentMouseX, currentMouseY)
#     # 进入模拟器
#
#     pyautogui.moveTo(1136,1071)
#     pyautogui.click()
#     time.sleep(1)
#     # 进入钉钉
#     pyautogui.moveTo(1445,567)
#     time.sleep(1)
#     pyautogui.click()
#     # 等待进入钉钉
#     time.sleep(5)
#     # 点击工作通知
#     pyautogui.moveTo(1506,391)
#     time.sleep(1)
#     pyautogui.click()
#     time.sleep(2)
#     # 点击填写
#     pyautogui.moveTo(1516, 940)
#     time.sleep(1)
#     pyautogui.click()


if __name__ == "__main__":
    main()
