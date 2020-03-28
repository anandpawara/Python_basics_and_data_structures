
def order(x):
    n = 0
    while (int(x) != 0):
        n = n+1
        x = x/10
    return n


def pow(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return pow(x, int(y/2)) * pow(x, int(y/2))
    return x * pow(x, int(y/2)) * pow(x, int(y/2))


def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while(int(temp) != 0):
        r = int(temp % 10)
        sum1 = sum1 + pow(r, n)
        temp /= 10
    return (sum1 == x)


x = 153
print(isArmstrong(x))

