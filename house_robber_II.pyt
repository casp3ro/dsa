def house_robber_II(nums:list[int]):
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]
    
    def house_rob(arr:list[int]):
        prevRob, currRob = 0, 0
        
        for val in arr:
            newRob  = max(prevRob + val, currRob)
            prevRob = currRob
            currRob = newRob
        
        return newRob
    
    return max(house_rob(nums[1:]), house_rob(nums[:-1]))