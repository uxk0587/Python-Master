"""
工资管理系统
Written by: Jack Lee                                                   
Time: 2020/4/24 21:20                                                  

Function:  某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成

                                                           
"""

from abc import ABCMeta, abstractclassmethod


class Employee(object, metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractclassmethod
    def get_salary(self):
        pass


class Manager(Employee):

    # 继承父类不重新生成器会默认继承父类的属性
    # def __init__(self):
    #     super().__init__()

    def get_salary(self):
        return 15000.0


class Programmer(Employee):

    # 继承父类重写的生成器会覆盖父类生成器，内部必须调用父类生成器来继承父类的属性
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self.sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('Jack'), Programmer('Musk'), Salesman('Jobs')
    ]

    for emp in emps:
        if isinstance(emp, Manager):
            print("%s's salary of this month : %s" % (emp.name, emp.get_salary()))
        elif isinstance(emp, Programmer):
            working_hour = int(input("Input the Programmer : %s's working time of this month: " % emp.name))
            emp.working_hour = working_hour
            print("%s 's salary of this month is %s" % (emp.name, emp.get_salary()))
        else:
            sales = int(input("Input the Salesman : %s's sale of this month: " % emp.name))
            emp.sales = sales
            print("%s 's salary of this month is %s" % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
