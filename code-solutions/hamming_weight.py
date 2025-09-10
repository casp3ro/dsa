def hamming_weight(n: int) -> int:
    """
    Counts the number of 1 bits in a binary representation of an integer.
    
    Interview Tips:
    - Use bit manipulation: n & 1 checks if last bit is 1
    - Right shift n >> 1 to check next bit
    - Continue until n becomes 0
    - Alternative: use n &= n-1 to remove rightmost 1 bit
    
    Complexity: O(1) time, O(1) space (at most 32 iterations for 32-bit int)
    """
    output = 0
    
    while n:
        output += n & 1
        n = n >> 1
    
    return output


def test_hamming_weight():
    """Test function that can be run from terminal."""
    # Test: 11 (binary: 1011) -> 3 ones
    n = 11
    result = hamming_weight(n)
    print(f"Number: {n} (binary: {bin(n)})")
    print(f"Number of 1 bits: {result}")


if __name__ == "__main__":
    test_hamming_weight()