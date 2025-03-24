def three_sum(nums:list[int])->list[list[int]]:
    nums.sort()
    results =[]
    
    for i in range(len(nums) -2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i +1, len(nums) -1
        
        while l <r:
            total = nums[l] + nums[r] + nums[i]
            
            if total == 0:
                results.append([nums[l] ,nums[r] ,nums[i]])
                
                while l<r and nums[l] == nums[l+1]:
                    l+=1
                while l<r and nums[r] == nums[r-1]:
                    r-=1
                
                l+=1
                r-=1
                
            elif total <0:
                l+=1
            else:
                r-=1
    
    return results
    