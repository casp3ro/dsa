def climb_stairs(n: int) -> int:
    """
    Counts the number of ways to climb n stairs (can take 1 or 2 steps at a time).
    
    Interview Tips:
    - This is Fibonacci sequence: ways(n) = ways(n-1) + ways(n-2)
    - Use two variables to track previous two values
    - Start with base cases: 1 way for 0 or 1 stairs
    - Key insight: each step depends on previous two steps
    
    Complexity: O(n) time, O(1) space
    """
    if n <= 1:
        return 1
    
    p1, p2 = 1, 1
    
    for _ in range(n - 1):
        p1, p2 = p1 + p2, p1
    
    return p1


def test_climb_stairs():
    """Test function that can be run from terminal."""
    # Test: n=5 -> 8 ways (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 1+2+2, 2+1+1+1, 2+1+2, 2+2+1)
    n = 5
    result = climb_stairs(n)
    print(f"Stairs: {n}")
    print(f"Ways to climb: {result}")


if __name__ == "__main__":
    test_climb_stairs()