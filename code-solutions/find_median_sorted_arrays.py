def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """
    Finds the median of two sorted arrays using binary search.
    
    Interview Tips:
    - Use binary search on smaller array
    - Partition both arrays such that left half <= right half
    - Check if partition is correct: maxLeft <= minRight
    - Median = max(left elements) or average of max(left) and min(right)
    - Key insight: binary search on partition point, not values
    
    Complexity: O(log(min(m,n))) time, O(1) space
    """
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A

    l, r = 0, len(A) - 1

    while True:
        i = (l + r) // 2
        j = half - i - 2

        aLeft = A[i] if i >= 0 else float('-inf')
        aRight = A[i + 1] if i + 1 < len(A) else float('inf')

        bLeft = B[j] if j >= 0 else float('-inf')
        bRight = B[j + 1] if j + 1 < len(B) else float('inf')

        if aLeft <= bRight and bLeft <= aRight:
            if total % 2:
                return min(aRight, bRight)
            return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
        
        elif aLeft > bRight:
            r = i - 1
        else:
            l = i + 1


def test_find_median_sorted_arrays():
    """Test function that can be run from terminal."""
    # Test: [1,3] and [2] -> median = 2.0
    nums1 = [1, 3]
    nums2 = [2]
    result = find_median_sorted_arrays(nums1, nums2)
    print(f"Array 1: {nums1}")
    print(f"Array 2: {nums2}")
    print(f"Median: {result}")


if __name__ == "__main__":
    test_find_median_sorted_arrays()