# Using counter and pointer in the str1
# def count(str1,str2):
#     c,j = 0,0
#     for i in str1:
#         if str2.find(i) >=0 and j == str1.find(i):
#             c += 1
#         j += 1
#     print("No of matching character are: {}".format(c))

def count (str1,str2):
    set_string1 = set(str1)
    set_string2 = set(str2)
    matched_characters = set_string1 & set_string2
    print("No of matching pair are : {}".format(len(matched_characters))) 

def main():  
    str1 ='bfghbfh' # first string 
    str2 ='bb22fsdf11@55k' # second string 
    count(str1, str2) # calling count function  

# Driver Code 
if __name__=="__main__": 
    main() 

