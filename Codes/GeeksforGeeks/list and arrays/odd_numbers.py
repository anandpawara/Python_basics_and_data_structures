nums = [2,7,5,64,14]

#Method using lambda + filter 
# new_list = list(filter(lambda x: x%2 != 0,nums))

#Method using list comprehensions

new_list = [n for n in nums if n % 2 != 0]
print(new_list)