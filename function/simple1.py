# 函数的基本使用
# def hello_python():
#     print("hello python")
#
#
# hello_python()

# 序列传参
# def sum_add(a, b, c):
#     return a + b + c
#
#
# L = [1, 2, 3]
# print(sum_add(*L))

def fun_dict(name, hiredate1, tel, dept):
    # 使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23,并向控制台输出结果
    print("{p1}隶属于{p4},电话:{p3},入职日期:{p2}".format(p1=name,p2=hiredate1,p3=tel,p4=dept))

# 创建字典dict1为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}


dict1 = {'name':'小葫芦','hiredate1':'2017-9-23','tel':18795642135,'dept':'技术部'}
# 使用字典dict1作为参数传入函数fun_dict
# fun_dict(**dict1)
