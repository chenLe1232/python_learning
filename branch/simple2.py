high = input("请输入您测量的高血压值：")
lower = input("请输入您测量的低压值：")
testA = int(input("测试数值"))
high = int(high)
lower = int(lower)
if (lower <= 60 or lower >= 90) or (high >= 140 or high <=90):
    print("您的血压出现异常，请尽快就医")
else:
    print("您的身体状况良好")
