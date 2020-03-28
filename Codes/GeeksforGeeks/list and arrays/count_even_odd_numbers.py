nums = [10,21,4,45,66,93,1]

#Using lamba function 
# odd_count = len(list(filter(lambda x: x%2 != 0,nums )))
# even = len(nums) - odd_count
# print("The even numbers count is {} and odd number count is {} ".format(even,odd_count))

# Using list comprehension
odd_count = len([n for n in nums if n %2 != 0])
even = len(nums) - odd_count
print("The even numbers count is {} and odd number count is {} ".format(even,odd_count))