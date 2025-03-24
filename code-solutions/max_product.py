# O(n)
def max_product(nums:list[int]):
    res= max(nums)
    currMax, currMin = 1,1
    
    for num in nums:
        if num == 0:
            currMax, currMin = 1,1
            continue
        
        tmpMax = currMax * num
        currMax = max(tmpMax, currMin * num, num)
        currMin = min(tmpMax, currMin * num, num)
        res = max(currMax,currMin,res)
        
    return res