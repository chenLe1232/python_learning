while True:
    print("******欢迎使用智能货转换系统*****")
    service_menu = {'1.': "人民币转换美元", "2.": "美元转换人民币", "3.": "人民币转换欧元", "0": "结束程序"}
    for k, v in service_menu.items():
        print(k, v)
    user_menu = input("请您选择需要的服务")
    # 人民币转换美元
    if user_menu == "1":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用人民转换美元服务")
        user_money = int(input("请输入您需要转换的人民币金额"))
        print("您需要转换的人民币为:{}元".format(user_money))
        RMB_to_US =  user_money / 6.72
        print("转换成美元为：{:.2f}$".format(RMB_to_US))
        print("=========================")
    # 美元转换人民币
    elif user_menu  == "2":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用美转换人民币服务")
        user_money = int(input("请输入您需要转换的美元金额"))
        print("您需要转换的美元为:{}元".format(user_money))
        US_to_RMB = user_money * 6.72
        print("转换成人民币为：{:.2f}元".format(US_to_RMB))
        print("=========================")
    # 人民币转换欧元
    elif user_menu == "3":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用人民币转换欧元服务")
        user_money = int(input("请输入您需要转换的人民币金额"))
        print("您需要转换的人民币为:{}元".format(user_money))
        RMB_to_EUR = user_money * 0.13
        print("兑换成欧元为:{:.2f}欧元".format(RMB_to_EUR))
        print("=========================")
    # 退出程序
    elif user_menu == "0":
        print("退出货币转换服务系统")
        break
    # 输入其他字符，则提示输入有误
    else:
        print("您输入的信息有误，请重新输入!!!")

