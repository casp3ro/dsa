def max_product(nums: list[int]) -> int:
    """
    Finds the maximum product of a contiguous subarray using dynamic programming.
    
    Interview Tips:
    - Track both max and min product ending at current position
    - Handle negative numbers by swapping max/min
    - Reset on encountering 0
    - Key insight: negative * negative = positive, so track both extremes
    
    Complexity: O(n) time, O(1) space
    """
    res = max(nums)
    currMax, currMin = 1, 1
    
    for num in nums:
        if num == 0:
            currMax, currMin = 1, 1
            continue
        
        tmpMax = currMax * num
        currMax = max(tmpMax, currMin * num, num)
        currMin = min(tmpMax, currMin * num, num)
        res = max(currMax, currMin, res)
        
    return res


def test_max_product():
    """Test function that can be run from terminal."""
    # Test: [2,3,-2,4] -> 6 (subarray [2,3])
    nums = [2, 3, -2, 4]
    result = max_product(nums)
    print(f"Array: {nums}")
    print(f"Maximum product: {result}")


if __name__ == "__main__":
    test_max_product()