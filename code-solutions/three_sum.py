def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Finds all unique triplets that sum to zero.
    
    Interview Tips:
    - Sort array first to enable two-pointer technique
    - Fix first number, use two pointers for remaining two
    - Skip duplicates for first number and two pointers
    - When sum = 0, skip duplicates before moving pointers
    
    Complexity: O(n²) time, O(1) space (excluding output)
    """
    nums.sort()
    results = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        
        while l < r:
            total = nums[l] + nums[r] + nums[i]
            
            if total == 0:
                results.append([nums[i], nums[l], nums[r]])
                
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                
                l += 1
                r -= 1
                
            elif total < 0:
                l += 1
            else:
                r -= 1
    
    return results


def test_three_sum():
    """Test function that can be run from terminal."""
    # Test: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print(f"Array: {nums}")
    print(f"Triplets that sum to 0: {result}")


if __name__ == "__main__":
    test_three_sum()
    