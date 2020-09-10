"""

Written by: Jack Lee                                                   
Time: 2020/9/5 8:39                                                  

Function:  自动化钉钉打卡

                                                           
"""

import os
import time
# import pyautogui
def main():
    # 进入dingding
    time.sleep(10)
    print(os.system('adb shell input tap 130 2100'))
    time.sleep(3)
    # 点击工作通知 置顶
    print(os.system('adb shell input tap 535 888'))
    time.sleep(2)
    # 开始填写
    print(os.system('adb shell input tap 543 2145'))
    time.sleep(5)


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