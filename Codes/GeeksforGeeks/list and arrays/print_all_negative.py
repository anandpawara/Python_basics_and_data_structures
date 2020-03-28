nums = [11,-21,0,45,66,-93]

#Using filter and lambda expression
# num_list = list(filter(lambda x:x<0,nums))
# print(num_list)

# Using list comprehensions
num_list = [n for n in nums if n < 0]
print(num_list)