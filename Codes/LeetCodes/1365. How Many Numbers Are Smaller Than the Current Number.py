def countNumbers(nums,number):
    count = 0
    for item in nums:
        if item < number:
            count += 1
    return count


nums = [8,1,2,2,3]
result = []
for i in range(len(nums)):
   result.append(countNumbers(nums,nums[i]))
print(result)
