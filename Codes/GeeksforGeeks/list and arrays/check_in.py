# Using (element in list) format 
# test_list = [1,6,3,5,3,4]

# if(2 in test_list):
#     print("Element exists")
# else:
#     print("Element not present")

from bisect import bisect_left

test_list_set = [1,6,3,5,3,4]
test_list_bisect = [1,6,3,5,3,10]

test_list_set = set(test_list_set)
print("List in test_list_set",test_list_set)

num = 2
if num in test_list_set:
    print("Element is present")
else:
    print("Element is not present")

