list = [10,21,4,45,66,93]
#Using list comprehension
# even_nos = [num for num in list if num %2 == 0]
# print(even_nos)

#Using lambda and filter function
even_nos = list(filter(lambda x: x % 2, list1)) 

print(even_nos)