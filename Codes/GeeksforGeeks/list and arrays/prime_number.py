# num = 11
# if num > 1:
#     for i in range(2,num//2):
#         if(num % i == 0):
#             print(num," is not a prime number")
#             break
#     else:
#         print(num," is a prime number")
# else:
#     print(num," is not a prime number")


def isPrime(n):
    if(n <= 1):
        return False
    if(n <= 3):
        return True

    if(n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i*i <= n):
        if(n %i == 0 or n % (i + 2) == 0):
            return False
        i = i+6
    return True

print(isPrime(11))
print(isPrime(35))
print(isPrime(36))
