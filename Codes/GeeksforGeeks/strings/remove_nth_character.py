test_str = "GeeksforGeeks"
print("Original string",test_str)
n = 3
new_str = ''

# Using for loop
# for i in range(len(test_str)):
#     if i != n:
#         new_str = new_str + test_str[i]
# print("Updated string",new_str)

# Using replace method replacing e with empty char only for first occurence
# new_str = test_str.replace('e','',1)
# print(new_str)

# Using slice + concatenation
# new_str = test_str[:n] + test_str[n+1:]
# print(new_str)

# Using join and list comprehensions
new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != n])
print(new_str)