def find_duplicate(nums:list[int]):
    if not nums or len(nums) < 2:
        return None
    
    # Floyd's algorithm, fast and slow pointer
    
    slow,fast = 0,0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]] #2k steps
        
        if slow == fast:
            break
        
    pointer = 0
    
    while True:
        pointer = nums[pointer]
        slow = nums[slow]
        
        if pointer == slow:
            return pointer