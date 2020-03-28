list1 = [11,5,17,18,23,50]

# new_list = [n for n in list1 if n %2 != 0]
# print(new_list)

# deleting element from range
# del list1[1:5]
# print(list1)

# Using list comprehensions
# unwanted_num = {11,5}
# nums = [ele for ele in list1 if ele not in unwanted_num]
# print(nums)

# Removes the value at the indices of 0,3,4
unwanted = [0,3,4]

for ele in sorted(unwanted,reverse = True):
    del list1[ele]
print(list1)