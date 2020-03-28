# def leftRotate(arr,d,n):
#     for i in range(d):
#         leftRotatebyOne(arr,n)

# def leftRotatebyOne(arr,n):
#     temp  = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp

# def printArray(arr,size):
#     for i in range(size):
#         print("%d"% arr[i],end=" ")
#     print("\n")

# arr = [1,2,3,4,5,6,7]
# printArray(arr,7)
# leftRotate(arr,2,7)
# printArray(arr,7)


def leftRotate(arr, d, n):
    for i in range(gcd(n, d)):
        temp = arr[i]
        j = i
        while 1:
            k = j+d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")
    print("\n")


def gcd(n, d):
    if d == 0:
        return n
    else:
        return gcd(d, n % d)


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)
