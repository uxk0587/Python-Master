"""

author: Jack Lee
time: 2020/4/11 0:01

"""
"""继承"""
class Person(object):

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

    def watch_movie(self):
        if self._age <= 16:
            print("%s is watching action movies" % self._name)
        else:
            print("%s is watching cartoon" % self._name)


class Student(Person):


    # 重新定义构造器，添加子类的新属性
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s is %s and is studing %s" % (self._name, self._grade, course))


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print("%s is %s and is teaching %s" % (self._name, self._title, course))


def main():
    student = Student('Jack', 22, 'grade 6')
    print(student.name)
    print(student.age)
    student.study('English')
    student.watch_movie()


    teacher = Teacher('Pony', 49, 'Professor')
    print(teacher.name)
    print(teacher.age)
    teacher.teach("Python")

if __name__ == '__main__':
    main()
