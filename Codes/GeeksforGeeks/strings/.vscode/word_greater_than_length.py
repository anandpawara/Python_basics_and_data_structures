def Func(str,k):
    result = ''
    for word in str.split(' '):
        if len(word) >= k:
            result = result + word
    print(result)

Func("String is fun in python",4) 