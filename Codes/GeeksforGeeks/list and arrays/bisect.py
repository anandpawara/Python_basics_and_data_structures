import bisect
li = [1,3,4,4,4,6,7]

print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect(li, 3)) 

print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_right(li, 3)) 