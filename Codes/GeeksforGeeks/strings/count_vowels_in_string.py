def vowel_count(str):
    count = 0
    vowel = set("aeiouAEIOU")

    for alphabet in str:
        if alphabet in vowel:
            count += 1
    print("No of vowels in strings are : {}".format(count))

str = "GeeksforGeeks"

vowel_count(str)