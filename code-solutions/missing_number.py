def missing_number(nums: list[int]) -> int:
    """
    Finds the missing number in an array containing n distinct numbers from 0 to n.
    
    Interview Tips:
    - Use mathematical approach: sum of 0 to n minus sum of array
    - Alternative: XOR all numbers 0 to n with all array elements
    - Key insight: missing number = expected sum - actual sum
    
    Complexity: O(n) time, O(1) space
    """
    res = len(nums)
    
    for i in range(len(nums)):
        diff = nums[i] - i
        res -= diff
    
    return res


def test_missing_number():
    """Test function that can be run from terminal."""
    # Test: [3,0,1] -> 2 (missing number)
    nums = [3, 0, 1]
    result = missing_number(nums)
    print(f"Array: {nums}")
    print(f"Missing number: {result}")


if __name__ == "__main__":
    test_missing_number()
