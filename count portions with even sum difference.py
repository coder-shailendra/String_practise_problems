def countevenPartitions(nums):
    total = sum(nums)
    if total % 2 != 0:
        return 0
    return len(nums) - 1
nums = [10,10,3,7,6]
print(countevenPartitions(nums))
nums = [1,2,2]
print(countevenPartitions(nums))