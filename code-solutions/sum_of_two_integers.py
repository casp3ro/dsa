def sum_of_two_integers(a: int, b: int) -> int:
    """
    Adds two integers without using + or - operators using bit manipulation.
    
    Interview Tips:
    - Use XOR for sum without carry
    - Use AND and left shift for carry
    - Handle 32-bit overflow with masks
    - Key insight: addition = sum without carry + carry shifted left
    
    Complexity: O(1) time, O(1) space (at most 32 iterations)
    """
    MASK = 0xFFFFFFFF
    MASK_MAX_INT = 0x7FFFFFFF
    
    while b != 0:
        carry = a & b
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK
    
    if a <= MASK_MAX_INT:
        return a
    else:
        return a - (MASK + 1)


def test_sum_of_two_integers():
    """Test function that can be run from terminal."""
    # Test: 1 + 2 = 3
    a, b = 1, 2
    result = sum_of_two_integers(a, b)
    print(f"{a} + {b} = {result}")


if __name__ == "__main__":
    test_sum_of_two_integers()
        
        