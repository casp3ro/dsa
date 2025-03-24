def container_with_most_water(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    maximum = 0

    while l < r:
        left_height, right_height = heights[l], heights[r]

        depth = min(left_height, right_height)
        distance = r - l

        curr_max = depth * distance
        maximum = max(curr_max, maximum)

        if left_height < right_height:
            l += 1
        else:
            r -= 1

    return maximum