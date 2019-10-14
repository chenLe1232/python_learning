# 利用range遍历其他序列
# c = "abcdefghi"
# for i in range(0,len(c)):
#     letter = c[i]
#     print(letter)
# 创建斐波那契数列
result = []
for i in range(0, 50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i - 1] + result[i - 2])
print(result)