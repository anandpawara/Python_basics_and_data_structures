nums = [11, -21, 0, 45, 66, -93] 
#Using lambda function and filter
# n = list(filter(lambda x: x>=0,nums))
# print(n)

#Using list comprehension
n = [n for n in nums if n >= 0]
print(n)