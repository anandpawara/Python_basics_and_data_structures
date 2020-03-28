# def swapPositions(list,pos1,pos2):
#     list[pos1] ,list[pos2] = list[pos2],list[pos1]
#     return list

# def swapPositions(list,pos1,pos2):
#     first_ele = list.pop(pos1)
#     second_ele = list.pop(pos2 -1)
#     list.insert(pos1,second_ele)
#     list.insert(pos2,first_ele)
#     return list


def swapPositions(list, pos1, pos2):
    get = list[pos1], list[pos2]
    list[pos2], list[pos1] = get
    return list


List = [23, 65, 19, 90]
print(swapPositions(List, 0, 2))
