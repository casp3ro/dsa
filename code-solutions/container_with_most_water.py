def container_with_most_water(heights: list[int]) -> int:
    """
    Finds the maximum area of water that can be contained between two lines.
    
    Interview Tips:
    - Use two pointers from both ends
    - Area = min(height[l], height[r]) * (r - l)
    - Move pointer with smaller height inward
    - Key insight: moving larger height won't increase area
    
    Complexity: O(n) time, O(1) space
    """
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


def test_container_with_most_water():
    """Test function that can be run from terminal."""
    # Test: [1,8,6,2,5,4,8,3,7] -> 49 (height 7, width 7)
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(heights)
    print(f"Heights: {heights}")
    print(f"Maximum water area: {result}")


if __name__ == "__main__":
    test_container_with_most_water()