#Using recursice method
# list = [11,5,17,18,23]

# def SumOfList(list,size):
#     if(size == 0):
#         return 0
#     else:
#         return list[size -1] + SumOfList(list,size-1)

# total = SumOfList(list,len(list))
# print(total)

list = [11,5,17,18,23]

total = sum(list)
print(total)