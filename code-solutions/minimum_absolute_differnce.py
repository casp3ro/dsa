"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order (with respect to pairs), each pair [a, b] follows:
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Examples:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]

Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
"""

from typing import List

def minimum_absolute_difference(arr: List[int]) -> List[List[int]]:
    """
    Returns all pairs with the minimum absolute difference in ascending order.
    """
    arr.sort()
    min_diff = float('inf')
    result = []

    # First pass: find the minimum absolute difference
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < min_diff:
            min_diff = diff

    # Second pass: collect all pairs with this minimum difference
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == min_diff:
            result.append([arr[i-1], arr[i]])

    return result

if __name__ == "__main__":
    # Example input
    test_cases = [
        ([4,2,1,3], [[1,2],[2,3],[3,4]]),
        ([1,3,6,10,15], [[1,3]]),
        ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]])
    ]
    for idx, (nums, expected) in enumerate(test_cases, 1):
        output = minimum_absolute_difference(nums)
        print(f"Test case {idx}: Input = {nums}")
        print(f"Output: {output}")
        print(f"Expected: {expected}")
        print(f"{'Pass' if output == expected else 'Fail'}\n")
