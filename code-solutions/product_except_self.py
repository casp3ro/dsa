def product_except_self(nums: list[int]) -> list[int]:
    """
    Returns an array where each element is the product of all other elements.
    
    Interview Tips:
    - Use two passes: left products, then right products
    - First pass: store left products in result array
    - Second pass: multiply by right products using post variable
    - Key insight: avoid division by using prefix and suffix products
    
    Complexity: O(n) time, O(1) space (excluding output array)
    """
    result = [1] * len(nums)
    pre = 1
    post = 1
    
    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= post
        post *= nums[i]
        
    return result


def test_product_except_self():
    """Test function that can be run from terminal."""
    # Test: [1,2,3,4] -> [24,12,8,6]
    nums = [1, 2, 3, 4]
    result = product_except_self(nums)
    print(f"Array: {nums}")
    print(f"Product except self: {result}")


if __name__ == "__main__":
    test_product_except_self()