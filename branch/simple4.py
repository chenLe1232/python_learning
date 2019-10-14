class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def speak(self):
        print("hello! 我是{}".format(self.name))

    def relation(self):
        pass


class Student(Person):

    def __init__(self, name, sex,score, major,stu_num):
        self.score = score
        self.major = major
        super(Student,self).__init__(name,sex)
        self._stu_num = stu_num

    def get_stunum(self):
        print("我的学号是为{},很高兴认识大家".format(self._stu_num))

    def identify_stu(self):
        if self._stu_num == 2018014002:
            print("我的分组已经完成")
        else:
            print("请稍后，马上为你自动分组")

    def set_num(self):
        self._stu_num = 13131349

    def relation(self):
        rclass = issubclass(Student, Person)
        if rclass:
            print("我的父类是Person")
        else:
            print("父类正在查询中·····")


if __name__ == '__main__':
    stu = Student('小明', '男', 90, '数学',2018014002)
    stu.speak()
    stu.get_stunum()
    stu.identify_stu()
    stu.relation()
    print('*'*17)

    stu2 = stu_2 = Student('小红', '女', 89, '英语',9879797)
    stu2.speak()
    stu2.set_num()
    stu2.get_stunum()
    stu2.identify_stu()


aaa = 'aaa'  \
            'aaa'
print(aaa)






