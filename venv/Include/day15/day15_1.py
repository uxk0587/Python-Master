"""
auto2code@1.1.1.20200902-release
author: Jack Lee
time: 2020/9/2 10:30

"""


# import sys
# import os
#
# current_path = os.getcwd()
# sys.path.append(current_path)

import time
from PIL import Image, ImageDraw, ImageFont

def generate_reser_code(name, college,  area="north",
                        img_path="./bath/bath1.jpg", gender="male", text_color="#969799", text_size=42, time_option='4'):

    if time_option == '1':
        img_path= "./bath/bath1.jpg"
    elif time_option == '2':
        img_path= "./bath/bath2.jpg"
    if time_option == '3':
        img_path= "./bath/bath3.jpg"
    elif time_option == '4':
        img_path= "./bath/bath4.jpg"
    elif time_option == '5':
        img_path= "./bath/bath5.jpg"
    elif time_option == '6':
        img_path= "./bath/bath6.jpg"
    elif time_option == '7':
        img_path= "./bath/bath7.jpg"
    elif time_option == '8':
        img_path= "./bath/bath8.jpg"



    reser_code = Image.open(img_path)
    draw = ImageDraw.Draw(reser_code)
    chinese_fontstyle = ImageFont.truetype("./font/ARIALUNI.TTF", text_size, encoding="unic")
    bathroom_fontstyle, name_fontstyle, college_fontstyle, type_fontsytle = [chinese_fontstyle] * 4
    date_fontstyle = ImageFont.truetype("./font/arial.ttf", text_size)

    if len(name) == 2:
        draw.text((893, 658), name, text_color, font=name_fontstyle)
    elif len(name) == 3:
        draw.text((850, 658), name, text_color, font=name_fontstyle)
    elif len(name) == 4:
        draw.text((808, 658), name, text_color, font=name_fontstyle)

    college_dict = {
        '1': '计算机科学与技术学院',
        '2': '航空工程学院',
        '3': '空中交通管理学院',
        '4': '电子信息与自动化学院',
        '5': '经济与管理学院',
        '6': '法学院',
        '7': '理学院',
        '8': '飞行技术学院',
        '9': '外国语学院',
        '10': '机场学院',
        '11': '中欧航空工程师学院',
        '12': '通航学院'
    }

    # if len(college) == 3:
    if college == '6' or college == '7':
        college = college_dict[college]
        draw.text((847, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 5:
    elif college == '9':
        college = college_dict[college]
        draw.text((765, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 6:
    elif college == '2' or college == '8':
        college = college_dict[college]
        draw.text((722, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 7:
    elif college == '5':
        college = college_dict[college]
        draw.text((682, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 8:
    elif college == '3':
        college = college_dict[college]
        draw.text((638, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 9:
    elif college == '11':
        college = college_dict[college]
        draw.text((597, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 10:
    elif college == '4' or college == '1':
        college = college_dict[college]
        draw.text((555, 758), college, text_color, font=college_fontstyle)
    # elif len(college) == 4:
    elif college == '10' or college == '12':
        college = college_dict[college]
        draw.text((808, 758), college, text_color, font=college_fontstyle)
    draw.text((808, 858), "洗浴服务", text_color, font=type_fontsytle)

    bathroom = ''
    if gender == '1':
        if area == '1':
            bathroom = u"北院男浴室"
        elif area == '2':
            bathroom = u"南院男浴室"
    elif gender == '2':
        if area == '1':
            bathroom = u"北院女浴室"
        elif area == '2':
            bathroom = u"南院女浴室"

    draw.text((764, 965), bathroom, text_color, font=bathroom_fontstyle)
    struct_date = time.strftime("%Y-%m-%d", time.localtime())
    draw.text((760, 1070), struct_date, text_color, font=date_fontstyle)
    print("Reservation code generated, auto2code exit")
    return reser_code


if __name__ == '__main__':
    print("auto2code@1.1.1.20200902-release developed by Jack Lee")
    print("+------------------+\n" +
          "  直接回车为默认值   \n" +
          "+------------------+")
    name = input('Input Name: ')
    if len(name) == 0:
        name = "马化腾"
    print("Name: " + name)
    print("\n")
    gender = input(
                   "+-----------------+\n" +
                   "|  Select Gender: |\n" +
                   "+-----------------+\n" +
                   "| Option | Gender |\n" +
                   "+-----------------+\n" +
                   "|    1   |  Male  |\n" +
                   "+-----------------+\n" +
                   "|    2   | Female |\n" +
                   "+-----------------+\n:")
    if len(gender) == 0:
        gender =  "1"
    print("Gender option selected: " + gender)
    print("\n")
    area = input(
                 "+----------------+\n" +
                 "|  Select Area:  |\n" +
                 "+----------------+\n" +
                 "| Option | Area  |\n" +
                 "+----------------+\n" +
                 "|    1   | North |\n" +
                 "+----------------+\n" +
                 "|    2   | South |\n" +
                 "+----------------+\n:")
    if len(area) == 0:
        area = "1"
    print("Area option selected: " + area)
    print("\n")
    college = input(
                    "+--------------------------------------------+\n" +
                    "|               Select College:              |\n"
                    "+--------------------------------------------+\n" +
                    "|  Option  |          College                |\n" +
                    "+--------------------------------------------+\n" +
                    "     1     |       计算机科学与技术学院          \n" +
                    "     2     |           航空工程学院              \n" +
                    "     3     |         空中交通管理学院           \n" +
                    "     4     |       电子信息与自动化学院          \n" +
                    "     5     |         经济与管理学院             \n" +
                    "     6     |            法学院                \n" +
                    "     7     |            理学院                \n" +
                    "     8     |          飞行技术学院              \n" +
                    "     9     |           外国语学院               \n" +
                    "    10     |            机场学院                \n" +
                    "    11     |        中欧航空工程师学院           \n" +
                    "    12     |            通航学院                \n" +
                    "+-------------------------------------------+\n:")

    if len(college) == 0:
        college = "1"
    print("College option selected: " + college)
    print("\n")
    time_option = input(
                 "+----------------------+\n" +
                 "|     Select Time:     |\n" +
                 "+----------------------+\n" +
                 "| Option |    Time     |\n" +
                 "+----------------------+\n" +
                 "|    1   | 15:30-15:35 |\n" +
                 "+----------------------+\n" +
                 "|    2   | 16:00-16:05 |\n" +
                 "+----------------------+\n" +
                 "|    3   | 16:30-16:35 |\n" +
                 "+----------------------+\n" +
                 "|    4   | 19:00-19:05 |\n" +
                 "+----------------------+\n" +
                 "|    5   | 19:30-19:35 |\n" +
                 "+----------------------+\n" +
                 "|    6   | 20:00-20:05 |\n" +
                 "+----------------------+\n" +
                 "|    7   | 20:30-20:35 |\n" +
                 "+----------------------+\n" +
                 "|    8   | 21:00-21:05 |\n" +
                 "+----------------------+\n:")


    if len(time_option) == 0:
        time_option = "4"
    print("Time option selected:" + time_option)
    print("...")
    reser_code = generate_reser_code(name, gender=gender, area=area, college=college, time_option=time_option)
    reser_code.save('reser_code.jpg')
    reser_code.show()
