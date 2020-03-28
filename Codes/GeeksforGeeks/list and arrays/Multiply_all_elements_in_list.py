# import numpy
# list1 = [1,2,3]
# list2 = [2,3,4]
# print(numpy.prod(list1))
# print(numpy.prod(list2))

from functools import reduce

list1 = [1,2,3]
list2 = [3,2,4]

result1 = reduce(lambda a,b: a*b,list1)
result2 = reduce(lambda a,b: a*b,list2)
print(result1,result2)