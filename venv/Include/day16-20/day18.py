"""

Written by: Jack Lee                                                   
Time: 2020/5/25 21:02                                                  

Function:   

                                                           
"""

"""面向对象进阶"""

# 工资结算系统


from abc import ABCMeta, abstractmethod

#实现抽象类 员工抽象类
class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        # 结算工资（抽象方法）
        pass

# 部门经理
class Manager(Employee):

    def get_salary(self):
        return 15000.0


# 程序员
class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200.0 * self.working_hour

# 销售员
class Salesman(Employee):
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


# 创建员工的工厂（工厂模式 - 通过工厂模式实现对象使用者和对象之间解耦合）
class EmployeeFactory:

    @staticmethod
    def create(emp_type, *args, **kwargs):
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():

    emps = [
        EmployeeFactory.create('M', 'Jack'),
        EmployeeFactory.create('P', 'Pony', 120),
        EmployeeFactory.create('P', 'Musk', 85),
        EmployeeFactory.create('S', 'Jobs', 123000),
    ]

    for emp in emps:
        # print(f'')中的：后表示格式化变量
        print(f'{emp.name}: {emp.get_salary():.2f} Yuan')



"""混入Mixin 设计 参考廖雪峰教程多重继承部分   混入实际上是通过多重继承来实现混入额外的功能"""
# 例子1
class Animal(object):
    pass

class Mammal(object):
    pass

class Bird(object):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass


# 给动物再加上Runable和Flyable的功能， 只需要先定义好Runable和Flyable类
class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')

# 对于需要继承Runable功能的动物，就多继承一个Runable
# 通过多重继承，一个子类可以获得多个父类的所有功能
class Dog(Mammal, Runnable):
    pass

# 为了更好地看出继承关系 把Runnable和Flyable改为 RunableMixIn 和 FlyableMixIn
class RunnableMixIn(object):
    pass

class FlyableMixIn(object):
    pass

class NewDog(RunnableMixIn, FlyableMixIn):
    pass

# MixIn的目的就是给一个类增加多个功能，在设计类的时候，我们通常优先考虑通过多重继承来组合多个Mixin的功能
# 而不是设计多层复杂的继承关系



# 例子2 自定义字典限制只有在指定的key不存在时才能在字典中设置键值对
class SetOnceMappingMixin:

    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super().__setitem__(key, value)

# 多重继承 继承SetOnceMappingMixIn dict
class SetOnceDict(SetOnceMappingMixin, dict):
    # 自定义字典
    # SetOnceMappingMixIn会重写掉dict中的 __setitem__ 方法 重写如何设置键值对

    pass

my_dict = SetOnceDict()

try:
    my_dict['username'] = 'jacklee'
    my_dict['username'] = 'helloJack'

except KeyError:
    pass

print(my_dict)

dict1 = dict()
dict1['name'] = 'Jack'
print(dict1)








