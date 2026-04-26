def findduplicate(nums):
    seen = set()
    result = []
    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)
    return result
print(findduplicate([0,1,1,0]))        
print(findduplicate([0,3,2,1,3,2]))    