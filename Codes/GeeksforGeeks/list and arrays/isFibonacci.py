import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(x):
    return isPerfectSquare(5*x*x + 4) or isPerfectSquare(5*x*x - 4)


for i in range(1, 11):
    if(isFibonacci(i) == True):
        print(i," is fibonacci number")
    else:
        print(i," is not a fibonacci number")
