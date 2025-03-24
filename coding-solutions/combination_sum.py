# O(2^(t/m))

def combination_sum(nums: list[int],target: int) -> list[int]:
    
    output = []
    
    def dfs(index,current,value):
        
        if index >= len(nums) or value > target:
            return
        
        if value == target:
            output.append(current.copy())
            return
        
        current.append(nums[index])
        dfs(index,current,value + nums[index])
        
        current.pop()
        dfs(index+ 1, current, value)
            
    
    dfs(0,[],0)
    
    return output