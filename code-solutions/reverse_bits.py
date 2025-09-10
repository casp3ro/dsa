def reverse_bits(n: int) -> int:
    """
    Reverses the bits of a 32-bit unsigned integer.
    
    Interview Tips:
    - Extract each bit using right shift and AND
    - Place bit in reversed position using left shift and OR
    - Process all 32 bits
    - Key insight: bit at position i goes to position (31-i)
    
    Complexity: O(1) time, O(1) space (always 32 iterations)
    """
    res = 0
    
    for i in range(32):
        bit = (n >> i) & 1
        res |= bit << (31 - i)
    
    return res


def test_reverse_bits():
    """Test function that can be run from terminal."""
    # Test: 43261596 (00000010100101000001111010011100) -> 964176192
    n = 43261596
    result = reverse_bits(n)
    print(f"Input: {n} (binary: {bin(n)})")
    print(f"Reversed: {result} (binary: {bin(result)})")


if __name__ == "__main__":
    test_reverse_bits()