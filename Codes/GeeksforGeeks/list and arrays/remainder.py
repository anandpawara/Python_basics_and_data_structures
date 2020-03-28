def findremainder(arr, len, n):
    mul = 1
    for i in range(len):
        mul = (mul * (arr[i] % n)) % n
    return mul % n
arr = [100,10,5,25,35,14]
n = 11
print(findremainder(arr,len(arr),n))