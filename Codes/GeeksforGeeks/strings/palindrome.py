s = "abba"

# Using sliing
# if s == s[::-1]:
#     print("True")
# else:
#     print("False")


# Traversing the string till half the length and check first and last element and then increasing from left side and decreasing from right side till len(str) // 2
# // return integer value
# def isPalindrome(str):
#     for i in range(len(str)//2):
#         if str[i] != str[len(str) - i - 1]:
#             return False
#     return True


# if(isPalindrome(s)):
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")


# Creating new string joining to empty string and then checking 
# def isPalindrome(str):
#     rev = ''.join(reversed(str))
#     return s == rev

# if isPalindrome(s):
#     print("The string is Palindrome")
# else:
#     print("The string is not Palindrome")

w = ''
for i in s:
    w = i + w
    if(s == w):
        print("The string is palindrome")
    else:
        print("The string is not palindrome")
