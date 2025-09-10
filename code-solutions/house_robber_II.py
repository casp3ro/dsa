def house_robber_II(nums: list[int]) -> int:
    """
    Finds maximum money that can be robbed from houses in a circle using dynamic programming.
    
    Interview Tips:
    - Houses are in a circle, so first and last are adjacent
    - Consider two cases: rob first house (exclude last) or rob last house (exclude first)
    - Use same DP as house_robber for each case
    - Key insight: break the circle by considering two linear subproblems
    
    Complexity: O(n) time, O(1) space
    """
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]
    
    def house_rob(arr: list[int]) -> int:
        prevRob, currRob = 0, 0
        
        for val in arr:
            newRob = max(prevRob + val, currRob)
            prevRob = currRob
            currRob = newRob
        
        return currRob
    
    return max(house_rob(nums[1:]), house_rob(nums[:-1]))


def test_house_robber_II():
    """Test function that can be run from terminal."""
    # Test: [2,3,2] -> 3 (rob house 1, skip house 0 and 2)
    nums = [2, 3, 2]
    result = house_robber_II(nums)
    print(f"Houses: {nums}")
    print(f"Maximum money: {result}")


if __name__ == "__main__":
    test_house_robber_II()