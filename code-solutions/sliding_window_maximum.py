from collections import deque


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in each sliding window of size k.
    
    Interview Tips:
    - Use deque to maintain indices of elements in decreasing order
    - Remove indices of elements smaller than current element
    - Remove indices outside current window from front
    - Front of deque always contains index of maximum element
    
    Complexity: O(n) time, O(k) space
    """
    output = []
    queue = deque()  # stores indices
    l = r = 0
    
    while r < len(nums):
        # Remove indices of elements smaller than current element
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)
        
        # Remove indices outside current window
        if l > queue[0]:
            queue.popleft()
            
        # Add maximum to result when window is complete
        if (r + 1) >= k:
            output.append(nums[queue[0]])
            l += 1

        r += 1
        
    return output


def test_sliding_window_maximum():
    """Test function that can be run from terminal."""
    # Test: nums=[1,3,-1,-3,5,3,6,7], k=3 -> [3,3,5,5,6,7]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_maximum(nums, k)
    print(f"Array: {nums}, k: {k}")
    print(f"Max in each window: {result}")


if __name__ == "__main__":
    test_sliding_window_maximum()