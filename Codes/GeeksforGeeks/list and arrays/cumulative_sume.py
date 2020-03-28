def Cumulative(list):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[:x+1]) for x in range(length)]
    return cu_list


  
# Driver Code 
lists = [10, 20, 30, 40, 50] 
print (Cumulative(lists)) 