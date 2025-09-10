def find_duplicate(nums: list[int]) -> int:
    """
    Finds the duplicate number in an array using Floyd's cycle detection.
    
    Interview Tips:
    - Use Floyd's algorithm (tortoise and hare)
    - Phase 1: Find intersection point in cycle
    - Phase 2: Find start of cycle (duplicate number)
    - Key insight: array values form a linked list with cycle
    
    Complexity: O(n) time, O(1) space
    """
    if not nums or len(nums) < 2:
        return None
    
    # Floyd's algorithm, fast and slow pointer
    slow, fast = 0, 0
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]  # 2k steps
        
        if slow == fast:
            break
        
    pointer = 0
    
    while True:
        pointer = nums[pointer]
        slow = nums[slow]
        
        if pointer == slow:
            return pointer


def test_find_duplicate():
    """Test function that can be run from terminal."""
    # Test: [1,3,4,2,2] -> 2 (duplicate number)
    nums = [1, 3, 4, 2, 2]
    result = find_duplicate(nums)
    print(f"Array: {nums}")
    print(f"Duplicate number: {result}")


if __name__ == "__main__":
    test_find_duplicate()