def longest_consecutive(nums:list[int])-> int:
    numSet = set(nums)
    output = 0
    
    for num in numSet:
        if (num - 1) not in numSet:
            longest = 1
            while num + longest in numSet:
                longest +=1
            output = max(output,longest)
    
    return output 