l = 7
flag = True
for i in range(2, l):
    if l % i == 0:
        print(i)
        flag = False
        break
if flag == True:
    print("{0}是质数".format(l))
else:
    print("{0}不是质数".format(l))

i = 3
j = 4
ll = str(i) + str(j)
print(type(ll))
