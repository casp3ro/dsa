# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
#
# Time Complexity: O(n), where n is the length of nums.
#   Each element is visited at most twice (once by right pointer, once by left pointer).
# Space Complexity: O(1), constant space is used.
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

target = 7
nums = [2, 3, 1, 2, 4, 3]

def minimumSizeSubarraySum(nums, target):
    """
    Returns the minimal length of a contiguous subarray of which the sum is at least target.
    If there is no such subarray, returns 0.

    :param nums: List[int] -- list of positive integers
    :param target: int -- positive integer target
    :return: int -- minimal length of such subarray, or 0 if none
    """
    min_len = float('inf')
    total = 0
    left = 0

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

print(minimumSizeSubarraySum(nums, target))