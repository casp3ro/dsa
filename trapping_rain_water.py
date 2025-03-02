def trapping_rain_water(height:list[int]):
    if not height:
        return 0
    
    output = 0
    l,r = 0, len(height) -1
    max_left, max_right = height[l], height[r]
    
    while l < r:
        if max_left < max_right:
            l+=1
            max_left = max(max_left,height[l])
            output += max_left - height[l]
            
        else:
            r-=1
            max_right = max(max_right,height[r])
            output += max_right - height[r]
            

    return output