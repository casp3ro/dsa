def longest_consecutive(nums: list[int]) -> int:
    """
    Finds the length of the longest consecutive sequence in an unsorted array.
    
    Interview Tips:
    - Use set for O(1) lookup
    - Only start counting from beginning of sequence (num-1 not in set)
    - Count consecutive numbers from each starting point
    - Key insight: only count from sequence starts to avoid O(n²) complexity
    
    Complexity: O(n) time, O(n) space
    """
    numSet = set(nums)
    output = 0
    
    for num in numSet:
        if (num - 1) not in numSet:
            longest = 1
            while num + longest in numSet:
                longest += 1
            output = max(output, longest)
    
    return output


def test_longest_consecutive():
    """Test function that can be run from terminal."""
    # Test: [100,4,200,1,3,2] -> 4 (sequence: 1,2,3,4)
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive(nums)
    print(f"Array: {nums}")
    print(f"Longest consecutive sequence length: {result}")


if __name__ == "__main__":
    test_longest_consecutive() 