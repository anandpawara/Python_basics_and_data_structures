# list = [8,6,8,10,8,20,10,8,8]
# num = 10
# print(list.count(num))

from collections import Counter
list = [8,6,8,10,8,20,10,8,8]
x = 8
d = Counter(list)
print("{} has occured {} times".format(x,d[x]))