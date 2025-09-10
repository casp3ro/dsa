def count_bits(n: int) -> list[int]:
    """
    Counts the number of 1 bits for each number from 0 to n using dynamic programming.
    
    Interview Tips:
    - Use DP: count[i] = count[i>>1] + (i&1)
    - Right shift removes last bit, i&1 gets last bit
    - Key insight: count of 1s = count without last bit + last bit value
    
    Complexity: O(n) time, O(1) space (excluding output)
    """
    dp = [0] * (n + 1)
    
    for num in range(n + 1):
        dp[num] = dp[num >> 1] + (num & 1)
    
    return dp


def test_count_bits():
    """Test function that can be run from terminal."""
    # Test: n=5 -> [0,1,1,2,1,2]
    n = 5
    result = count_bits(n)
    print(f"n: {n}")
    print(f"Bit counts: {result}")


if __name__ == "__main__":
    test_count_bits()