def missing_number(nums:list[int]) -> int:
    res = len(nums)
    
    for i in range(len(nums)):
        diff = nums[i] - i
        res-=diff
    
    return res
