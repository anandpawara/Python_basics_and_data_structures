my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 

# def divide_chunks(l,n):
#     for i in range(0,len(l),n):
#         yield l[i:i+n]

# n = 5
# x = list(divide_chunks(my_list,n))
# print(x)

n  = 5
# Working
final = [my_list[i*n:(i+1)*n] for i in range((len(my_list) + n -1 )//n)]
print(final)