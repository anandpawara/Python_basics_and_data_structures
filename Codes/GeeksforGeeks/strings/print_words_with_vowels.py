def check(string):
    vowels = set('aeiou')

    for char in string:
        if char in vowels:
            return True
    return False

string = "qwrtpsdg"
if check(string) == True:
    print("contains vowels")
else:
    print("does not contains vowels")