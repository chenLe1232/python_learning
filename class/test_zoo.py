class Cat(object):
    """猫科动物类"""

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def set_age(self, age):
        """
        改变猫的年龄
        :param age: int年龄
        :return: 更改后的年龄
        """
        self.__age = age

    def show_info(self):
        rest = '我叫{0},今年{1}岁'.format(self.name, self.__age)
        print(rest)
        return rest
    def eat(self):
        print("猫爱吃鱼")

    def catch(self):
        print("猫会抓老鼠")


if __name__ == '__main__':
    # 实例化你家的小黑
    cat_black = Cat('小黑', 3)
    cat_black.eat()
    cat_black.name = '小白'
    cat_black.set_age(14)
    cat_black.show_info()
