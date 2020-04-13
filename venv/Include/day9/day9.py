"""
面向对象进阶
author: Jack Lee
time: 2020/4/9 22:47

"""
"""
__slots__魔法

@property装饰器 
@setter修改器
"""
class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def watch(self):
        if self._age < 16:
            print('%s is watching cartoon' % self._name)
        else:
            print('%s is watching action movie' % self._name)



def main():
    person = Person('Jack', 23)
    person.watch()
    person.age = 14
    print(person.age)
    print(person.name)
    person.watch()
    # person.name = 'Pony'
    print(person.name)
    # person._is_handsome = True # Python对象动态添加属性 但是添加__slot__魔法后不能只能绑定特定属性
    # print(person._is_handsome)

    person._gender = 'Male'
    print(person._gender)

    """python 对象动态添加方法
    import types
    def show(self):
        print("I'm showing")
    person.show = types.MethodType(show, person)
    person.show()
    """


if __name__ == '__main__':
    main()


