def largest_rectangle_area(heights:list[int])->int:
    maxArea = 0
    stack = [] #(index, height)
    
    for index, height in enumerate(heights):
        start_index = index
        while stack and stack[-1][1] > height:
            last_index, last_height = stack.pop()
            maxArea = max(maxArea, last_height * (index - last_index))
            start_index  = last_index
        stack.append((start_index, height))
        
    for index, height in stack:
        maxArea = max(maxArea, height * (len(heights) - index))
    
    return maxArea
            