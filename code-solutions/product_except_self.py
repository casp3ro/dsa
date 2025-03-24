def product_except_self(nums:list[int])-> list[int]:
    result = [1] * len(nums)
    pre = 1
    post = 1
    
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    
    for i in range(len(nums) -1, -1, -1):
        result[i] *=post
        post *=nums[i]
        
    return result