list = [10,20,4,45,99]
#Method 1
# max = max(list[0],list[1])
# secondmax = min(list[0],list[1])

# for i in range(2,len(list)):
#     if list[i] > max:
#          secondmax = max
#          max = list[i]
#     else:
#         if list[i] > secondmax:
#             secondmax = list[i]
# print("Max number is {} and second max number is {}".format(max,secondmax),end = " ")

# Method 2
# list.sort()
# print("Max number is {} and second max number is {}".format(list[-1],list[-2]),end = " ")

# Method 3
# Using set data stucture
# new_list = set(list)
# new_list.remove(max(new_list))
# print(max(new_list))


