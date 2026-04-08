def minimumoperation(nums):
    count = 0
    for num in nums:
        if num % 3 != 0:
            count +=1
    return count
print(minimumoperation([1,2,3,4]))  
print(minimumoperation([3,6,9]))    
