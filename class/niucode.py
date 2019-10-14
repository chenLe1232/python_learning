import re
str1 = "Python's features"
str2 = re.match( r'(.*)on(.*?) .*', str1, re.M|re.I)
print (str2.group(1))

a = range(100)
print(a[-3])
print(a[2:13])
print(a[::3])
print(a[2-3])