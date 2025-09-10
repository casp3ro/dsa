def length_of_the_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    
    Interview Tips:
    - Use sliding window with two pointers (left, right)
    - Use set to track characters in current window
    - When duplicate found, shrink window from left until no duplicates
    - Always update max length when expanding window
    
    Complexity: O(n) time, O(min(m,n)) space where m is charset size
    """
    unique = set()
    longest = 0
    l = 0
    
    for r in range(len(s)):
        while s[r] in unique:
            unique.remove(s[l])
            l += 1
        
        unique.add(s[r])
        longest = max(longest, r - l + 1)
    
    return longest


def test_length_of_the_longest_substring():
    """Test function that can be run from terminal."""
    # Test: "abcabcbb" -> 3 (substring "abc")
    test_str = "abcabcbb"
    result = length_of_the_longest_substring(test_str)
    print(f"String: '{test_str}'")
    print(f"Longest substring length: {result}")


if __name__ == "__main__":
    test_length_of_the_longest_substring()
        