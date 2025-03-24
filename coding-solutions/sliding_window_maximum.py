from collections import deque


def sliding_window_maximum(nums: list[int], k: int):
    output = []
    queue = deque() #index
    l=r=0
    
    while r < len(nums):
        
        # pop smaller values then num[r] from queue
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)
        
        if l > queue[0]:
            queue.popleft()
            
        if (r+1) >= k:
            output.append(nums[queue[0]])
            l+=1

        r+=1
        
    
    return output