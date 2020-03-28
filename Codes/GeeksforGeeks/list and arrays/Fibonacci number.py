# Method 1
# def fibonacci(n):
#     if n < 0:
#         print("Incorrect Number")
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# Method 2 (Dynamic programming solution)
# def fibonacci(n):
#     FibArray = [0, 1]
#     if n < 0:
#         print("Incorrect input")
#     elif n <= len(FibArray):
#         return FibArray[n-1]
#     else:
#         temp_fib = fibonacci(n-1) + fibonacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib


# Method 3 (Dynamic programming and space optimization)


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a+b
            a = b
            b = c
        return c


print(fibonacci(9))
