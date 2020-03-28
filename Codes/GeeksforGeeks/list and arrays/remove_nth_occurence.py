# def RemoveNthWord(list, word, N):
#     newList = []
#     count = 0

#     for i in list:
#         if(i == word):
#             count = count + 1
#             if (count != N):
#                 newList.append(i)
#         else:
#             newList.append(i)
#     list = newList

#     if(count == 0):
#         print("Item not found")
#     else:
#         print("Update list is", list)
#     return newList
# list = ["geeks", "for", "geeks"]
# word = 'geeks'
# N = 2
# RemoveNthWord(list, word, N)


def RemoveNthWord(list, word, N):
    count = 0
    for i in range(len(list)):
        if(list[i] == word):
            count = count + 1
            if (count == N):
                del(list[i])
                return True
    return False

list = ["geeks","for","geeks"]
word = "geeks"
N = 2
flag = RemoveNthWord(list,word,N)
if(flag == True):
    print("Update list is",list)
else:
    print("Item not found")    


