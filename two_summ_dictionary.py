def twoSum(nums, target):
    diction = {}
    for i, num in enumerate(nums):
        m = target - num
        if m in diction:
            return print([diction[m],i])
        else:
            diction[num]=i


twoSum([1, 2, 3], 4)        # [0, 2]
twoSum([2, 7, 11, 15], 9)   # [0, 1]
twoSum([3, 2, 4], 6)        # [1, 2]
twoSum([3, 3], 6)           # [0, 1]
