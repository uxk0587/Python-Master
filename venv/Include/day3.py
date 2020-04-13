"""

author: Jack Lee
time: 2020/1/3 23:08

""" 

#英制单位和公制单位厘米转换
value = float(input('请输入长度：'))
unit = input('请输入单位：')

if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')


# 百分制成绩转换成等级
score = int(input('请输入分数：'))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('%d 对应的等级是 %s' % (score, grade))

# 判断输入的边长能否组成三角形， 如果能则计算出三角形的周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and a + c > b:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：%f' % area)
else:
    print('不能构成三角形')



