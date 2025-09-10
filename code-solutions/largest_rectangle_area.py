def largest_rectangle_area(heights: list[int]) -> int:
    """
    Finds the largest rectangle area in a histogram using a monotonic stack.
    
    Interview Tips:
    - Use monotonic increasing stack
    - When current height < stack top, calculate area
    - Area = height * (current_index - start_index)
    - Process remaining elements in stack
    - Key insight: stack maintains bars that can extend right
    
    Complexity: O(n) time, O(n) space
    """
    maxArea = 0
    stack = []  # (index, height)
    
    for index, height in enumerate(heights):
        start_index = index
        while stack and stack[-1][1] > height:
            last_index, last_height = stack.pop()
            maxArea = max(maxArea, last_height * (index - last_index))
            start_index = last_index
        stack.append((start_index, height))
        
    for index, height in stack:
        maxArea = max(maxArea, height * (len(heights) - index))
    
    return maxArea


def test_largest_rectangle_area():
    """Test function that can be run from terminal."""
    # Test: [2,1,5,6,2,3] -> 10 (rectangle with height 5, width 2)
    heights = [2, 1, 5, 6, 2, 3]
    result = largest_rectangle_area(heights)
    print(f"Heights: {heights}")
    print(f"Largest rectangle area: {result}")


if __name__ == "__main__":
    test_largest_rectangle_area()
            